#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from dispatcher.task import ProblemTask
import program
import codecs
import os


class TestProgram(unittest.TestCase):
    def test_status(self):
        status = ['AC', 'CE', 'DSC', 'MLE',
                  'MLE(stack)', 'OLE', 'RE', 'TLE', 'WA']
        for i in status:
            with codecs.open(os.path.join('test_dir', i, 'test.cpp'), 'r', 'utf-8') as f:
                code = f.read()
            p = program.Program(ProblemTask(
                id='test_status', user_id=i, language='C++', code=code))
            print(p.run().__dict__)

    def test_languages(self):
        languages = ['C', 'C++', 'C#', 'Go', 'Java', 'Python3',
                     'Ruby', 'JavaScript']  # ruby and js error output
        user_id = 'Languages'
        for i in languages:
            with codecs.open(os.path.join('test_dir', user_id, i), 'r', 'utf-8') as f:
                code = f.read()
            p = program.Program(ProblemTask(
                id='test_languages', user_id=i, language=i, code=code))
            print(p.run().__dict__)


if __name__ == '__main__':
    unittest.main()
