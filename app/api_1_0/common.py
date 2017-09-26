#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, jsonify
from . import decorators
from ..models import db


@decorators.composed(decorators.route('/search', methods=['POST']), decorators.json_required)
def search():
    # target: Model, type: Model attribute, content: going to search
    target = request.json.get('target')
    type = request.json.get('type')
    content = request.json.get('content')
    cls = eval(target)
    attr = eval(target + '.' + type)
    query = db.session.query(cls).filter(attr.like('%{}%'.format(content))).all()
    pass
