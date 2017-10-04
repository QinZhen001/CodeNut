#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, jsonify
from . import decorators
from ..models import *
from tools.HashIDs import generate_id


@decorators.composed(decorators.route('/search', methods=['POST']), decorators.json_required)
def search():
    # target: Model, type: Model attribute, content: going to search
    target = request.json.get('target')
    type = request.json.get('type')
    content = request.json.get('content')
    cls = eval(target)
    attr = eval(target + '.' + type)
    query = db.session.query(cls).filter(attr.like('%{}%'.format(content))).all()
    tmp_list = []
    for i in query:
        tmp_dict = {}
        if hasattr(i, 'to_json'):
            tmp_list.append(i.to_json())
            continue
        if hasattr(i, 'list_to_json'):
            tmp_list.append(i.list_to_json())
            continue
        for key in i.__dict__:
            if key == '_sa_instance_state' or key == 'password_hash' or key == 'role_id':
                continue
            if key == 'id' or key == 'contest_id' or key == 'user_id' \
                    or key == 'problem_id' or key == 'code_id':
                tmp_dict.update({key: generate_id(i.__dict__[key])})
                continue
            tmp_dict.update({key: i.__dict__[key]})
        tmp_list.append(tmp_dict)
    return jsonify({'msg': 'ok', 'result': tmp_list})
