#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import time
import re
import os
import pickle
import threading
import mysql.connector.pooling
import aiohttp


def create_table():
    connection = pool.get_connection()
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS `problems`')
    cursor.execute('''CREATE TABLE `problems` (
                          `id` int(11) NOT NULL AUTO_INCREMENT,
                          `title` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
                          `description` text NOT NULL,
                          `level` int(11) NOT NULL,
                          `tag` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
                          `accepted` int(11) DEFAULT '0',
                          `submitted` int(11) DEFAULT '0',
                          `template` text,
                          `solution` text,
                          PRIMARY KEY (`id`),
                          UNIQUE KEY `id` (`id`),
                          UNIQUE KEY `ix_problems_title` (`title`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4''')
    print('[!]Table `problems` created successfully')
    cursor.close()
    connection.close()


def mysql_pool():
    dbconfig = {
        'host': 'localhost',
        'port': '3306',
        'database': 'codenut',
        'user': 'root',
        'password': 'root',
        'charset': 'utf8',
        'collation': 'utf8_bin',
    }
    return mysql.connector.pooling.MySQLConnectionPool(pool_name='codepool', pool_size=30, **dbconfig)


def write_problems_status():
    response = requests.get('https://leetcode.com/api/problems/all/')
    text = json.loads(response.text)

    problems_list = [i for i in text['stat_status_pairs'] if not i['paid_only']]
    useful_list = [{'title': i['stat']['question__title'],
                    'url_title': i['stat']['question__title_slug'],
                    'level': i['difficulty']['level']} for i in problems_list]

    with open('problems_status', 'wb') as f:
        pickle.dump(useful_list, f)

    print('[*]Total free problems: ' + str(len(useful_list)))


# multithreading
class DownloadProblems(threading.Thread):
    def __init__(self, p_list):
        threading.Thread.__init__(self)
        self.p_list = p_list

    def download(self):
        for i in self.p_list:
            if os.path.exists('pages/{}'.format(i['url_title'])):
                continue
            try:
                response = requests.get('https://leetcode.com/problems/{}/description/'.format(i['url_title']),
                        timeout=100)
                if response.status_code == 200:
                    with open('pages/{}'.format(i['url_title']), 'w+') as f:
                        f.write(response.text)
                    print('[*]Get: {}'.format(i['url_title']))
                else:
                    print('[!]Failed: {}'.format(i['url_title']))
            except Exception as e:
                print('[!]Request error: {}'.format(e))

    def run(self):
        self.download()


def run_download():
    print('[*]Starting download these problems pages...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)
    nums = 25
    x = int(len(useful_list) / nums)
    threads = [DownloadProblems(useful_list[x * i:x * (i + 1)]) for i in range(nums)]
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()


class InsertProblems(threading.Thread):
    def __init__(self, p_list):
        threading.Thread.__init__(self)
        self.p_list = p_list

    def insert(self):
        connection = pool.get_connection()
        for i in self.p_list:
            with open('pages/{}'.format(i['url_title']), 'r') as f:
                soup = BeautifulSoup(f.read(), 'lxml')
            # title = soup.find(attrs={'property': 'og:title'})['content']
            title = i['title']

            # no <p>... tag
            # description = soup.find(attrs={'name': 'description'})['content']
            description = [str(i) for i in soup.find(class_='question-description').contents]
            description = ''.join(list(filter(lambda x: x != '\n', description)))

            # level = soup.find('span', attrs={'class': re.compile('difficulty-label')}).get_text()
            # if level == 'Easy': level = 1
            # elif level == 'Medium': level = 2
            # else: level = 3
            level = i['level']

            tag = ','.join([a.get_text() for a in soup.select('#tags-topics > a')])

            try:
                cursor = connection.cursor()
                sql = 'INSERT INTO `problems` (`title`, `description`, `level`, `tag`) VALUES(%s, %s, %s, %s)'
                cursor.execute(sql, (title, description, level, tag))
                connection.commit()
                cursor.close()
                print('[*]Insert: {}'.format(title))
            except Exception as e:
                connection.rollback()
                print('[!]Insert problem error, {}'.format(e))
        connection.close()

    def run(self):
        self.insert()


def run_insert_problems():
    print('[*]Starting insert these problems...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)
    nums = 20
    x = int(len(useful_list) / nums)
    threads = [InsertProblems(useful_list[x * i:x * (i + 1)]) for i in range(nums)]
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()


class UpdateSolutions(threading.Thread):
    def __init__(self, p_list):
        threading.Thread.__init__(self)
        self.p_list = p_list

    def update(self):
        connection = pool.get_connection()
        for i in self.p_list:
            cursor = connection.cursor()
            sql = 'SELECT solution FROM `problems` WHERE `title`=%s'
            cursor.execute(sql, (i['title'],))
            if [i for i in cursor][0][0] is not None:
                continue
            cursor.close()
            try:
                response = requests.get('https://leetcode.com/problems/api/{}/solution/'.format(i['url_title']))
                if response.status_code == 200:
                    try:
                        cursor = connection.cursor()
                        sql = 'UPDATE `problems` SET `solution`=%s WHERE `title`=%s'
                        cursor.execute(sql, (response.json()['solutionHTML'], i['title']))
                        connection.commit()
                        cursor.close()
                        print('[*]Get: {}'.format(i['title']))
                    except Exception as e:
                        connection.rollback()
                        print('[!]Update solution error, {}'.format(e))
            except Exception as e:
                print('[!]{} request error: {}'.format(i['title'], e))
        connection.close()

    def run(self):
        self.update()


def run_update_solutions():
    print('[*]Start update these problems\'s solutions...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)
    nums = 25
    x = int(len(useful_list) / nums)
    threads = [UpdateSolutions(useful_list[x * i:x * (i + 1)]) for i in range(nums)]
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()


class UpdateTemplates(threading.Thread):
    def __init__(self, p_list):
        threading.Thread.__init__(self)
        self.p_list = p_list

    def update(self):
        connection = pool.get_connection()
        for i in self.p_list:
            with open('pages/{}'.format(i['url_title']), 'r') as f:
                template = re.findall(r'codeDefinition: (.*])', f.read(), re.M | re.I)
            try:
                cursor = connection.cursor()
                sql = 'UPDATE `problems` SET `template`=%s WHERE `title`=%s'
                cursor.execute(sql, (template[0], i['title']))
                connection.commit()
                cursor.close()
                print('[*]Get: {}'.format(i['title']))
            except Exception as e:
                connection.rollback()
                print('[!]Update template error, {}'.format(e))
        connection.close()

    def run(self):
        self.update()


def run_update_templates():
    print('[*]Start update these problems\'s templates...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)
    nums = 25
    x = int(len(useful_list) / nums)
    threads = [UpdateTemplates(useful_list[x * i:x * (i + 1)]) for i in range(nums)]
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()

# async
async def insert_problems():
    print('[*]Start insert these problems...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)

    total = len(useful_list)
    count = 1
    for i in useful_list:
        with open('pages/{}'.format(i['url_title']), 'r') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        # title = soup.find(attrs={'property': 'og:title'})['content']
        title = i['title']

        # no <p>... tag
        # description = soup.find(attrs={'name': 'description'})['content']
        description = [str(i) for i in soup.find(class_='question-description').contents]
        description = ''.join(list(filter(lambda x: x != '\n', description)))

        # level = soup.find('span', attrs={'class': re.compile('difficulty-label')}).get_text()
        # if level == 'Easy': level = 1
        # elif level == 'Medium': level = 2
        # else: level = 3
        level = i['level']

        tag = ','.join([a.get_text() for a in soup.select('#tags-topics > a')])

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `problems` (`title`, `description`, `level`, `tag`) VALUES(%s, %s, %s, %s, %s)'
                cursor.execute(sql, (title, description, level, tag))
                connection.commit()
            print('[*]Total: {} Now: {}'.format(total, count))
            count += 1
        except Exception as e:
            connection.rollback()
            print('[!]Insert problem error, {}'.format(e))


async def update_problems_set_solutions():
    print('[*]Start update these problems\'s solutions...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)

    total = len(useful_list)
    count = 1
    for i in useful_list:
        try:
            response = requests.get('https://leetcode.com/problems/api/{}/solution/'.format(i['url_title']),
                    timeout=100)
            if response.status_code == 200:
                try:
                    with connection.cursor() as cursor:
                        sql = 'UPDATE `problems` SET `solution`=%s WHERE `title`=%s'
                        cursor.execute(sql, (response.json()['solutionHTML'], i['title']))
                        connection.commit()
                    print('[*]Total: {} Now: {}'.format(total, count))
                    count += 1
                except Exception as e:
                    connection.rollback()
                    print('[!]Update solution error, {}'.format(e))
        except Exception as e:
            print('[!]Request error: {}'.format(e))


async def update_problems_set_templates():
    print('[*]Start update these problems\'s templates...')
    with open('problems_status', 'rb') as f:
        useful_list = pickle.load(f)

    total = len(useful_list)
    count = 1
    for i in useful_list:
        with open('pages/{}'.format(i['url_title']), 'r') as f:
            template = re.findall(r'codeDefinition: (.*])', f.read(), re.M | re.I)

        try:
            with connection.cursor() as cursor:
                sql = 'UPDATE `problems` SET `template`=%s WHERE `title`=%s'
                cursor.execute(sql, (template[0], i['title']))
                connection.commit()
            print('[*]Total: {} Now: {}'.format(total, count))
            count += 1
        except Exception as e:
            connection.rollback()
            print('[!]Update template error, {}'.format(e))


if __name__ == '__main__':
    # write_problems_status()
    # run_download()
    #pool = mysql_pool()
    # create_table()
    # run_insert_problems()
    #run_update_solutions()
    # run_update_templates()
    # update_problems_set_solutions()
    # update_problems_set_templates()
    print('[!]All things done')
