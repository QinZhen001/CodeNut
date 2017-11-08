#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is to download answer from database.
"""

import codecs
import pymysql
import base64
import os
import subprocess

answer_dir = 'answer_dir'


def b64_decode(string):
    return (base64.b64decode(string)).decode()


def is_changed(file, content):
    with codecs.open(file, 'r', 'utf-8') as f:
        old = base64.b64encode((f.read().encode()))
    if content == str(old)[2:-1]:
        return False
    print('[*]{} changed'.format(file))
    return True


def compile_answer_cpp(problem_dir):
    command = 'g++ Solution.cpp -o Solution -Wall -lm -O2 -lseccomp --static -DONLINE_JUDGE'
    sub = subprocess.Popen(command,
                           shell=True,
                           cwd=problem_dir,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    output, error = sub.communicate()
    out_file, err_file = os.path.join(
        'log', 'download_out'), os.path.join('log', 'download_err')
    with codecs.open(out_file, 'a+', 'utf-8') as f:
        f.write(output.decode())
    with codecs.open(err_file, 'a+', 'utf-8') as f:
        f.write(error.decode())


def download_answer(dic):
    from json import loads
    code = loads(b64_decode(dic.pop('code')))
    code = {'Solution.' + key: value for (key, value) in code.items()}
    dic.update(code)
    problem_dir = os.path.join(answer_dir, dic.pop('id'))
    if not os.path.exists(problem_dir):
        os.makedirs(problem_dir)
    for key, value in dic.items():
        file = os.path.join(problem_dir, key)
        if not os.path.exists(file) or is_changed(file, value):
            with codecs.open(file, 'w+', 'utf-8') as f:
                f.write(value)
            if key == 'Solution.cpp' and (not os.path.exists(os.path.join(problem_dir, 'Solution')) or is_changed(file, value)):
                compile_answer_cpp(problem_dir)


def select_from_db():
    db = pymysql.connect('appmysql', 'root', 'root', 'codenut')
    print('[!]start download')

    with db.cursor() as cursor:
        sql = 'SELECT * FROM codenut_problems where id <10'

        cursor.execute(sql)
        results = cursor.fetchall()
        for idx, row in enumerate(results):
            download_answer({'id': str(row[0]),
                             'in': row[11],
                             'out': row[12],
                             'code': row[13]})
            if (idx + 1) % 6 == 0:
                print('[*]now is {}'.format(idx))

    print('[!]download ok')
    db.close()


if __name__ == '__main__':
    select_from_db()
