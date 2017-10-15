#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from insert_tmp_data import run as insert_run
import time


class Test:
    url = 'http://0.0.0.0:5000'
    headers = {'Content-Type': 'application/json'}
    token = tuple()

    def tokens(self):
        resource = '/tokens'
        # login
        data = {'username': 'administrator', 'password': 'administrator'}
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
        resource = '/problems'
        self.tokens()

        data = {'language': 'C++',
                'code': """
                #include <cstdio>\n
                #include <iostream>\n

                int main(int argc, char* argv[]) {\n
                char* a = argv[1];\n
                printf("hello %s", a);\n
                return 0;\n
            }"""}
        for i in range(5):
            response = requests.patch(
                self.url + resource + '/2/codes', json=data, headers=self.headers, auth=self.token)
            print(response.text)


if __name__ == '__main__':
    insert_run()
    Test().run_code()
