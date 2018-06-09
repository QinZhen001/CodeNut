#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import codecs
from dispatcher.task import ResultTask
import CodeNutJudge
import shlex


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
        logger.debug('arg problem %s', problem)
        self.problem = problem
        self.result = ResultTask(user_id=self.problem['user_id'])
        self.user_dir = os.path.join(
            config['work_dir'], self.problem['user_id'])
        self.user_out_path = os.path.join(self.user_dir, 'out')
        # make a directory for user
        if not os.path.exists(self.user_dir):
            os.makedirs(self.user_dir)
        self.completeCodeFile()

    def completeCodeFile(self):
        def completeCodeFileJavaRemovLastBraces(user_code):
            fixed_code = user_code.rstrip()
            if fixed_code[-1] == '}':
                fixed_code = fixed_code[:-1]
            return fixed_code

        def completeCodeFileInternal(user_code, user_code_type, problem_filepath, output_filepath):
            if user_code_type in ['Java']:
                user_code = completeCodeFileJavaRemovLastBraces(user_code)

            if user_code_type in ['Python3', 'Ruby']:
                delimiter_start = '# ssstart'
                delimiter_end = '# eeend'
            else:
                delimiter_start = '// ssstart'
                delimiter_end = '// eeend'
            with open(problem_filepath) as f:
                text_code = f.read()
            start_index = text_code.find(delimiter_start)
            end_index = text_code.find(delimiter_end)
            result = text_code.replace(text_code[start_index:end_index], user_code)
            logger.saveCodeFile(result)
            with open(output_filepath, 'w') as f:
                f.write(result)
            return

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
        from os.path import join
        logger.debug('problem:%s', self.problem)
        problem_id = str(self.problem['id'])
        problem_type = self.problem['language']
        answer_dir = config['answer_dir']

        output_filepath = join(self.user_dir, file_name[problem_type])
        problem_filepath = join(answer_dir, problem_id, file_name[problem_type])
        user_code = self.problem['code']
        user_code_type = self.problem['language']

        completeCodeFileInternal(user_code, user_code_type, problem_filepath, output_filepath)

    def __compile(self):
        command = {
            'C': 'gcc Solution.c -o Solution -Wall -lm -O2 -std=c11 -lseccomp -DONLINE_JUDGE',
            'C++': 'g++ Solution.cpp -o Solution -std=c++11 -Wall -lm -O2 -lseccomp -DONLINE_JUDGE',
            'C#': 'mcs Solution.cs',
            'Go': 'go build -ldflags "-s -w" Solution.go',
            'Java': 'javac Solution.java -encoding UTF8',
        }

        sub = subprocess.Popen(command[self.problem['language']],
                               shell=True,
                               cwd=self.user_dir,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output, error = sub.communicate()
        logger.debug('err:%s, out:%s, retcode:%s', error, output, sub.returncode)
        if sub.returncode != 0:
            with open(self.user_out_path, 'wb') as f:
                f.write(error)
            return False
        else:
            return True

    def __get_program_argv(self, dir):
        command = {
            'C': '{}/Solution'.format(dir),
            'C++': '{}/Solution'.format(dir),
            'Go': '{}/Solution'.format(dir),
            'C#': '/usr/bin/mono {}/Solution.exe'.format(dir),
            'Java': '/usr/bin/java -cp {}/ Solution'.format(dir),
            'Python3': '/usr/bin/python3 {}/Solution.py'.format(dir),
            'Ruby': '/usr/bin/ruby {}/Solution.rb'.format(dir),
            'JavaScript': '/usr/bin/nodejs --no-deprecation {}/Solution.js'.format(dir),
        }
        # get exe like: ['go','run', '123/Solution.go']
        program = shlex.split(command[self.problem['language']])

        # limit time and memory size
        if self.problem['language'] in ['C', 'C++', 'C#', 'Go']:
            time_limit, mem_limit = 1000, 32768
        else:
            time_limit, mem_limit = 2000, 65536
        return program, time_limit, mem_limit

    def __judge(self, choice):
        if self.problem['custom_input']:
            # user input
            in_path = os.path.join(self.user_dir, 'custom_input')
            official_out_path = os.path.join(self.user_dir, 'official_out')
            with codecs.open(in_path, 'w+', 'utf-8') as f:  # write before read
                f.write(self.problem['custom_input'])
            official_program, _, _ = self.__get_program_argv(
                os.path.join(config['answer_dir'], str(self.problem.id)))
        else:
            # official input
            in_path = os.path.join(
                config['answer_dir'], str(self.problem['id']), 'in')
            official_out_path = os.path.join(
                config['answer_dir'], str(self.problem['id']), 'out')

        with open(in_path) as f:
            in_list = f.readlines()

        # run program
        user_program, time_limit, memory_limit = self.__get_program_argv(
            self.user_dir)
        count = 1 if choice == 'one' else len(in_list)
        time_used, memory_used = 0.0, 0.0
        for i in range(count):
            input = in_list[i].replace('\r', '').rstrip().split()

            logger.debug('args:%s, fp:%s', user_program + input, self.user_out_path)
            result = CodeNutJudge.run({
                'args': user_program + input,
                'output': self.user_out_path,
                'language': self.problem['language'],
                'time_limit': time_limit,  # in MS
                'memory_limit': memory_limit,  # in KB
            })
            logger.debug('result:%s', result)

            with open(self.user_out_path) as f:
                logger.debug('fp:%s', self.user_out_path)
                logger.debug('file:%s', f.read())
            self.result.status = result['status']
            if self.result.status != ResultStatus.RS:
                break
            # run official program
            if self.problem['custom_input']:
                self.__run_program(official_program + input,
                                   official_out_path, time_limit, memory_limit)

            time_used += result['time_used']
            memory_used += result['memory_used']
        # judge
        if self.result.status == ResultStatus.RS:
            self.result.status = self.__judge_result(official_out_path)
        with open(self.user_out_path) as f:
            self.result.output = f.read()
        self.result.time_used = round(time_used / count, 2)
        self.result.memory_used = round(memory_used / count, 2)
        return self.result

    def __judge_result(self, official_out_path):
        with open(official_out_path) as f:
            official_out_list = f.readlines()
        with open(self.user_out_path) as f:
            user_out_list = f.readlines()
        logger.debug('userfp:%s', self.user_out_path)
        logger.debug('user:%s, office:%s', user_out_list, official_out_list)
        if len(official_out_list) != len(user_out_list):
            return ResultStatus.WA
        if all([x.strip() == y.strip() for x, y in zip(official_out_list, user_out_list)]):
            return ResultStatus.AC
        else:
            return ResultStatus.WA

    def run(self, choice='many'):
        # can not compile them
        if self.problem['language'] not in ['JavaScript', 'Ruby', 'Python3'] and self.__compile() is False:
            with open(self.user_out_path) as f:
                self.result.output = f.read()
            self.result.status = ResultStatus.CE
            retval = self.result
        else:
            retval = self.__judge(choice)
        logger.debug('return:%s', retval.__dict__)
        return retval

    def __del__(self):  # clear user dir

        __import__("shutil").rmtree(self.user_dir)
        pass


def test():
    from os import chdir
    from pickle import load
    chdir('/root/source_code.d/software_design.d/CodeNut/CodeNutJudge')
    __import__("shutil").rmtree('../work_dir/1', ignore_errors=True)
    with open('/tmp/CodeNutJudge_problem.bug', 'rb') as f:
        problem = load(f)
    t = Program(problem).run()
    print(t.__dict__)


def updateData():
    if 1:
        from subprocess import run
        run(['python3', '/root/source_code.d/software_design.d/problem_solution.d/insert_code_sql.py'], check=True)
        run(['python3', 'download_answer.py'], check=True, shell=False,
            cwd='/root/source_code.d/software_design.d/CodeNut')


def configLogger():
    from pathlib import Path
    import logging
    from logging import Formatter
    from datetime import datetime

    class ColoredFormatter(Formatter):
        def __init__(self, use_color=True, **kwargs):
            self.use_color = use_color
            super().__init__(**kwargs)

        def format(self, record):
            if record.levelname in ['DEBUG']:
                record.name = '[*]'
            else:
                record.name = '[!]'
            if self.use_color:
                record.name = '\x1b[32m' + record.name + '\x1b[0m'
            return super().format(record)

    def saveCodeFile(content):
        with open('/tmp/program.code', 'w') as f:
            f.write(content)

    logfilepath = str(Path(__file__).parent / 'program.log')

    logger_name = __name__
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(logging.DEBUG)

    filename = logfilepath
    filehander = logging.FileHandler(filename, mode='w')
    filehander.setLevel(logging.DEBUG)

    # fmt ='%(asctime)s %(levelname)s: %(message)s'
    fmt = '%(name)s %(lineno)d-%(funcName)s-%(message)s'
    datefmt = '%H:%M:%S'
    formatter = ColoredFormatter(use_color=True, fmt=fmt, datefmt=datefmt)

    filehander.setFormatter(formatter)
    logger.addHandler(filehander)

    logger.saveCodeFile = saveCodeFile

    logger.debug('starting logger %s', datetime.now().strftime('%H:%M:%S'))

    return logger


logger = configLogger()
config = {
    'work_dir': '../work_dir',
    'answer_dir': '../answer_dir',
}

if __name__ == '__main__':
    # updateData()
    test()
