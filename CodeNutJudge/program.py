#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import codecs
import logging
from dispatcher.task import ResultTask
import CodeNutJudge
import shlex
import linecache


logging.basicConfig(level=logging.WARNING,
                    filename='program.log',
                    format='%(asctime)s %(levelname)s: [line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Config:
    program = {
        'work_dir': 'test_dir',
        'answer_dir': 'answer_dir',
    }


class ResultStatus:
    RS = 'Run Successfully'
    AC = 'Accepted'
    TLE = 'Time Limit Exceeded'
    MLE = 'Memory Limit Exceeded'
    WA = 'Wrong Answer'
    RE = 'Runtime Error'
    OLE = 'Output limit'
    CE = 'Compile Error'
    PE = 'Presentation Error'


class Program:

    def __init__(self, problem):
        self.problem = problem
        self.result = ResultTask(user_id=self.problem['user_id'])
        self.user_dir = os.path.join(Config.program['work_dir'], self.problem['user_id'])
        # make a directory for user
        if not os.path.exists(self.user_dir):
            os.mkdir(self.user_dir)
        self.__store()

    def __store(self):
        file_name = {
            'C': 'Solution.c',
            'C++': 'Solution.cpp',
            'C#': 'Solution.cs',
            'Go': 'Solution.go',
            'Java': 'Solution.java',
            'Python3': 'Solution.py',
            'Ruby': 'Solution.rb',
            'JavaScript': 'Solution.js',
        }
        file_path = os.path.join(self.user_dir, file_name[self.problem['language']])
        with codecs.open(file_path, 'w+', 'utf-8') as f:
            f.write(self.problem['code'])

    def __compile(self):
        command = {
            'C': 'gcc Solution.c -o Solution -Wall -lm -O2 -std=c11 -lseccomp --static -DONLINE_JUDGE',
            'C++': 'g++ Solution.cpp -o Solution -Wall -lm -O2 -lseccomp --static -DONLINE_JUDGE',
            'C#': 'mcs Solution.cs',
            'Go': 'go build -ldflags "-s -w" Solution.go',
            'Java': 'javac Solution.java -encoding UTF8',
            'Python3': 'python3 -m pycompile Solution.py',
            'Ruby': 'ruby Solution.rb',
            'JavaScript': 'nodejs Solution.js',
        }

        sub = subprocess.Popen(command[self.problem['language']],
                               shell=True,
                               cwd=self.user_dir,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output, error = sub.communicate()
        out_path = os.path.join(self.user_dir, 'out')
        err_path = os.path.join(self.user_dir, 'err')
        with codecs.open(out_path, 'a+', 'utf-8') as f:
            f.write(output.decode())
        with codecs.open(err_path, 'a+', 'utf-8') as f:
            f.write(error.decode())

        if sub.returncode == 0:  # compile success
            logging.info('problem: {}-{} __compiled by user: {}'.format(self.problem['id'],
                         self.problem['language'], self.problem['user_id']))
            return True
        else:
            return False

    def __get_program_argv(self, dir):
        command = {
            'C': '{}/Solution'.format(dir),
            'C++': '{}/Solution'.format(dir),
            'Go': '{}/Solution'.format(dir),
            'C#': '/usr/bin/mono {}/Solution.exe'.format(dir),
            'Java': '/usr/bin/java -cp {}/ Solution'.format(dir),
            'Python3': '/usr/bin/python3 {}/__pycache__/Solution.cpython-35.pyc'.format(dir),
            'Ruby': '/usr/bin/ruby {}/Solution.rb'.format(dir),
            'JavaScript': '/usr/bin/nodejs {}/Solution.js'.format(dir),
        }
        # get exe like: ['go','run', '123/Solution.go']
        program = shlex.split(command[self.problem['language']])

        # limit time and memory size
        if self.problem['language'] in ['C', 'C++', 'C#', 'Go']:
            time_limit, mem_limit = 1000, 32768
        else:
            time_limit, mem_limit = 2000, 65536
        return program, time_limit, mem_limit

    def __run_program(self, args, out_file, time_limit, memory_limit):
        cfg = {
            'args': args,
            'output': out_file,
            'language': self.problem['language'],
            'time_limit': time_limit,  # in MS
            'memory_limit': memory_limit,  # in KB
        }
        return CodeNutJudge.run(cfg)

    def __judge(self, choice):
        if self.problem['custom_input']:
            # user input
            in_path = os.path.join(self.user_dir, 'custom_input')
            official_out_path = os.path.join(self.user_dir, 'official_out')
            with codecs.open(in_path, 'w+', 'utf-8') as f:  # write before read
                f.write(self.problem['custom_input'])
            official_program, _, _ = self.__get_program_argv(os.path.join(Config.program['answer_dir'], str(self.problem.id)))
        else:
            # official input
            in_path = os.path.join(Config.program['answer_dir'], str(self.problem['id']), 'in')
            official_out_path = os.path.join(Config.program['answer_dir'], str(self.problem['id']), 'out')

        in_list = linecache.getlines(in_path)

        user_out_path = os.path.join(self.user_dir, 'out')
        # run program
        user_program, time_limit, memory_limit = self.__get_program_argv(self.user_dir)
        count = 1 if choice == 'one' else len(in_list)
        time_used, memory_used = 0.0, 0.0
        for i in range(count):
            input = in_list[i].replace('\r', '').rstrip().split()
            result = self.__run_program(user_program + input, user_out_path, time_limit, memory_limit)
            self.result.status = result['status']
            if self.result.status != ResultStatus.RS:
                break
            # run official program
            if self.problem['custom_input']:
                self.__run_program(official_program + input, official_out_path, time_limit, memory_limit)

            time_used += result['time_used']
            memory_used += result['memory_used']
        # judge
        if self.result.status == ResultStatus.RS:
            official_out_list = linecache.getlines(official_out_path)
            self.result.status = self.__judge_result(official_out_list)
            with codecs.open(user_out_path, 'r', 'utf-8') as f:
                self.result.output = f.read()
            self.result.time_used = round(time_used / count, 2)
            self.result.memory_used = round(memory_used / count, 2)
        logging.info(self.result.__dict__)
        return self.result

    def __judge_result(self, official_out_list):
        user_out_path = os.path.join(self.user_dir, 'out')
        user_out_list = linecache.getlines(user_out_path)
        for i in range(len(user_out_list)):
            user_out = user_out_list[i].replace('\r', '').rstrip()
            official_out = official_out_list[i].replace('\r', '').rstrip()
            if user_out == official_out:
                continue
            elif user_out.split() == official_out.split():
                return ResultStatus.PE
            elif official_out in user_out:
                return ResultStatus.OLE
            else:
                return ResultStatus.WA
        return ResultStatus.AC

    def run(self, choice='many'):
        if self.__compile() is False:
            self.result.status = ResultStatus.CE
            return self.result
        return self.__judge(choice)

    def __del__(self):  # clear user dir
        __import__("shutil").rmtree(self.user_dir)
