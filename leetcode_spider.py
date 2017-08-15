#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import time
import re
import os


def create_table():
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS problems")
        cursor.execute('''CREATE TABLE `problems`(
                            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            `title` VARCHAR(512) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
                            `description` TEXT NOT NULL,
                            `level` TINYINT NOT NULL,
                            `tag` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
                            `accepted` BIGINT DEFAULT 0,
                            `submitted` BIGINT DEFAULT 0,
                            `solution` TEXT DEFAULT NULL,
                            PRIMARY KEY (`id`),
                            UNIQUE KEY `id` (`id`)
                    ) ENGINE=InnoDB AUTO_INCREMENT=500 DEFAULT CHARSET=utf8 COLLATE=utf8_bin''')
    print("[!]Table 'problems' created successfully")


def get_problem_list():
    response = requests.get('https://leetcode.com/api/problems/all/')
    text = json.loads(response.text)
    problem_list = []
    for i in text['stat_status_pairs']:
        if not i['paid_only']:
            problem_list.append(i)
    print('[*]total free problems: ' + str(len(problem_list)))
    return problem_list


def get_problems_page():
    count = 0
    problem_list = get_problem_list()
    total = len(problem_list)
    for i in problem_list:
        response = requests.get('https://leetcode.com/problems/{}'.format(i['stat']['question__title_slug']), timeout=100)

        if response.status_code == 200:
            count += 1
            with open("page/{}.html".format(str(count)), 'w+') as f:
                f.write(response.text)
            print('[*]rest: %s' % str(total - count))
        else:
            print('[!]failed to get "%s" ' % i['stat']['question__title_slug'])


def get_problems():
    pages = sum([len(x) for _, _, x in os.walk(os.path.dirname("page/"))])
    for count in range(1, pages + 1):
        with open("page/{}.html".format(str(count)), 'r') as f:
            soup = BeautifulSoup(f.read(), "lxml")
        title = soup.find(attrs={"property": "og:title"})['content']

        # description = soup.find(attrs={"name": "description"})['content']
        description = []
        for i in soup.find(class_="question-description").contents:
            description.append(str(i))
        description = ''.join(list(filter(lambda x: x != '\n', description)))

        level = soup.find('span', attrs={"class": re.compile("difficulty-label")}).get_text()
        if level == 'Easy':
            level = 1
        elif level == 'Medium':
            level = 2
        else:
            level = 3

        tag = []
        for a in soup.select('#tags-topics > a'):
            tag.append(a.get_text())
        time.sleep(0.1)

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `problems` (`id`, `title`, `description`, `level`, `tag`) VALUES(%s, %s, %s, %s, %s)'
                cursor.execute(sql, (count, title, description, level, ','.join(tag)))
                connection.commit()

            time.sleep(0.1)
            print('[*]rest: %s' % str(pages - count))
            # get solution
            response = requests.get('https://leetcode.com/problems/api/{}/solution/'.format('-'.join(title.split(' '))), timeout=10)
            if response.status_code == 200:
                try:
                    with connection.cursor() as cursor:
                        sql = 'UPDATE `problems` SET `solution`=%s WHERE `id`=%s'
                        cursor.execute(sql, (response.json()['solutionHTML'], str(count)))
                        connection.commit()
                except Exception as e:
                    connection.rollback()
                    print('[!]insert solution error, ' + str(e))

        except Exception as e:
            connection.rollback()
            print('[!]insert problems error, ' + str(e))


if __name__ == '__main__':
    connection = pymysql.connect(host='localhost', user='root', password='root', db='leetcode', charset='utf8')
    create_table()
    # get_problems_page()
    get_problems()
    connection.close()
