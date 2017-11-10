#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FFDebug_FALG = 1

import requests
import json
try:
    FFDebug_FALG
except NameError: 
    from insert_tmp_data import run as insert_run
import time


class Test:
    url = 'http://0.0.0.0:5000'
    headers = {'Content-Type': 'application/json'}
    token = tuple()

    def tokens(self):
        resource = '/tokens'
        # login
        try:
            FFDebug_FALG
        except NameError: 
            data = {'username': 'administrator', 'password': 'administrator'}    
        else:
            data = {'username': 'admin', 'password': 'admin'}
        response = requests.post(
            self.url + resource, json=data, headers=self.headers)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'
        self.token = (jdict['result'][0]['token'], '')
        # logout
        response = requests.delete(self.url + resource, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'
        # error login
        data = {'username': 'xx', 'password': 'xx'}
        response = requests.post(
            self.url + resource, json=data, headers=self.headers)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'no'

    def users(self):
        resource = '/users'
        self.tokens()
        # get_all_users
        response = requests.get(self.url + resource, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_user_info
        for i in jdict['result']:
            response = requests.get(
                self.url + resource + '/' + i['user_id'], auth=self.token)
            jdict = json.loads(json.dumps(response.json()))
            assert jdict['msg'] == 'ok'

            # get_user_contests_joined
            response = requests.get(
                self.url + resource + '/' + i['user_id'] + '/contests_joined', auth=self.token)
            jdict = json.loads(json.dumps(response.json()))
            assert jdict['msg'] == 'ok'

            # get_user_contests_sponsor
            response = requests.get(
                self.url + resource + '/' + i['user_id'] + '/contests_sponsor', auth=self.token)
            jdict = json.loads(json.dumps(response.json()))
            assert jdict['msg'] == 'ok'

            # get_user_codes_submitted
            response = requests.get(
                self.url + resource + '/' + i['user_id'] + '/codes_submitted', auth=self.token)
            jdict = json.loads(json.dumps(response.json()))
            assert jdict['msg'] == 'ok'

            # get_user_collections
            response = requests.get(
                self.url + resource + '/' + i['user_id'] + '/collections', auth=self.token)
            jdict = json.loads(json.dumps(response.json()))
            assert jdict['msg'] == 'ok'

        # create_user
        data = {'email': 'test@text.com',
                'username': 'test', 'password': 'test'}
        response = requests.post(
            self.url + resource, json=data, headers=self.headers)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_user_info
        data = {'realname': 'testadmin', 'profile': 'testadmin'}
        response = requests.put(
            self.url + resource + '/info', json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_user_password
        data = {'oldpassword': 'administrator', 'newpassword': 'testadmin'}
        requests.put(self.url + resource + '/password', json=data,
                     headers=self.headers, auth=self.token)
        data = {'username': 'administrator', 'password': 'testadmin'}
        response = requests.post(self.url + '/tokens',
                                 json=data, headers=self.headers)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_user_role
        data = {'role': 'sponsor'}  # user id: o6
        response = requests.put(self.url + resource + '/o6/role',
                                json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # delete_users  # sponsor id: dx
        response = requests.delete(
            self.url + resource + '/dx', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

    def problems(self):
        resource = '/problems'
        self.tokens()
        # get_all_problems
        response = requests.get(self.url + resource)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_problem_info
        response = requests.get(self.url + resource + '/Meq')
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_problem_solution
        response = requests.get(self.url + resource + '/Meq/solutions')
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # create_problem
        data = {'title': 'test', 'description': 'test',
                'level': '1', 'tag': 'test', 'code': 'test'}
        response = requests.post(
            self.url + resource, json=data, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_problem_solution # 31
        data = {'solution': 'testsolution'}
        response = requests.put(self.url + resource +
                                '/zaa/solutions', json=data, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_problem_info  # 30
        data = {'title': 'testupdate'}
        response = requests.put(self.url + resource +
                                '/Meq', json=data, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # delete_problem  # 29
        response = requests.delete(
            self.url + resource + '/K4', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_problem_code
        response = requests.get(self.url + resource + '/Meq/codes')
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # add_collection
        response = requests.post(
            self.url + resource + '/Meq/collections', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # delete_collection
        response = requests.delete(
            self.url + resource + '/Meq/collections', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # like_problem  # 30
        response = requests.put(self.url + resource +
                                '/Meq/likes/True', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'
        # hate  # 30
        response = requests.put(self.url + resource +
                                '/Meq/likes/False', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'
        # no feel  # 30
        response = requests.put(self.url + resource +
                                '/Meq/likes/None', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_user_notes
        data = {'text': 'testnote'}
        response = requests.put(self.url + resource + '/Meq/notes',
                                json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'
        data = {'text': 'xxxxx'}
        response = requests.put(self.url + resource + '/Meq/notes',
                                json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # run_code
        data = {'language': 'xxxxx', 'code': 'xx', 'custom_input': 'xx'}
        response = requests.patch(
            self.url + resource + '/Meq/codes', json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # submit_code
        data = {'language': 'xxxxx', 'code': 'xx', 'custom_input': 'xx'}
        response = requests.post(
            self.url + resource + '/Meq/codes', json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

    def contests(self):
        resource = '/contests'
        self.tokens()

        # create_contest
        data = {'title': 'test', 'description': 'test', 'start_time': time.strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': time.strftime('%Y-11-%d %H:%M:%S'), 'auto_approve': True, 'password': 'test'}
        response = requests.post(
            self.url + resource, json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # update_contest_info
        data = {'title': 'testupdate',
                'auto_approve': False, 'password': 'testupdate'}
        response = requests.put(
            self.url + resource + '/dx', json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # delete_contest
        response = requests.delete(
            self.url + resource + '/dx', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_contest_info
        response = requests.get(self.url + resource + '/o6', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_all_contests
        response = requests.get(self.url + resource)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # join_contest
        data = {'password': None}
        response = requests.post(
            self.url + resource + '/o6/users', json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # get_contest_user
        response = requests.get(self.url + resource + '/o6/users')
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # out_contest
        response = requests.delete(
            self.url + resource + '/o6/users', auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'ok'

        # allow_join_or_out
        data = {'user_id': 'GG'}
        response = requests.put(self.url + resource + '/o6/users',
                                json=data, headers=self.headers, auth=self.token)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'no'

    def search(self):
        resource = '/search'
        self.tokens()

        data = {'target': 'Problem', 'type': 'id', 'content': '12'}
        response = requests.post(
            self.url + resource, json=data, headers=self.headers)
        jdict = json.loads(json.dumps(response.json()))
        assert jdict['msg'] == 'no'

    def run_code(self):
        from time import sleep
        from subprocess import run, PIPE
        from sys import path
        path.append('/root/source_code.d/software_design.d/CodeNut/CodeNutAPI/tools')
        from HashIDs import generate_id
        print('begin test')
        run('supervisorctl -c ../../supervisord.conf restart all', shell = True, check= True, stdout = PIPE)
        
        resource = '/problems'
        self.tokens()
        
        for pid, lan, text, fpath in getRequestData():
            hasd_pid = generate_id(pid)            
            data = {'language': lan,'code': text}
            URL = self.url + resource + '/%s/codes' % hasd_pid
            response = requests.patch(URL, json=data, headers=self.headers, auth=self.token)
            
            print(fpath)            
            if 'Accepted' not in response.text:
                save_bug_info(pid, lan, text)
                raise ValueError(fpath)
            #sleep(3)
        print('test done')
def save_bug_info(pid, language, codetext):
    from pickle import dump
    problem = {
        'id': pid,
        'user_id': '1',
        'language': language,
        'custom_input': None,
        'code': codetext
    }
    with open('/tmp/CodeNutJudge_problem.bug', 'wb') as f:    
        dump(problem, f)

def getRequestData():
    from pathlib import Path
    language_type = {
        'C': 'Solution.c',
        'C++': 'Solution.cpp',
        'C#': 'Solution.cs',
        'Go': 'Solution.go',
        'Java': 'Solution.java',
        'Python3': 'Solution.py',
        'Ruby': 'Solution.rb',
        'JavaScript': 'Solution.js',
    }        
    
    root = Path('/root/source_code.d/software_design.d/problem_solution.d')
    for pdir in root.glob('*d'):
        pid = int(list(pdir.glob('?'))[0].name)
        for fpath in pdir.glob('Solu*'):
            language = [key for key,item in language_type.items() if item== fpath.name][0]                
            with fpath.open() as f:
                content = f.read()
            code_text = getUserCode(content, language)
            yield pid, language, code_text, str(fpath)
                
def getUserCode(content, language):
    from re import findall, MULTILINE, DOTALL
    text = findall(r'ssstart\n(.+)\n[ ]*[/#]{1,2} eeend',content,MULTILINE|DOTALL)[0]
    if language == 'Java':
        text = text + '}'
    return text
            
if __name__ == '__main__':
    try:
        FFDebug_FALG
    except NameError: 
        insert_run()
    Test().run_code()
