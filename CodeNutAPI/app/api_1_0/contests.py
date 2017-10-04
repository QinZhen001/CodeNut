#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, jsonify, g
from tools.HashIDs import generate_id, verify_id
from . import decorators
from ..models import db, Contest, UserJoinContest, Permission


@decorators.composed(decorators.route('/contests/<id>/users', methods=['POST']), decorators.json_required, decorators.permission_required(Permission.PROGRAM))
def join_contest(id):
    contest = Contest.query.get(verify_id(id))
    password = request.json.get('password')
    if contest.password != password:
        return jsonify({'msg': 'no', 'error': 'password wrong'})
    user_contest = UserJoinContest(user_id=g.current_user.id, contest_id=verify_id(id))
    if contest.auto_approve:
        user_contest.is_join = True
    db.session.add(user_contest)
    return jsonify({'msg': 'ok', 'result': [{'is_join': user_contest.is_join}]})


@decorators.composed(decorators.route('/contests/<id>/users', methods=['DELETE']), decorators.permission_required(Permission.PROGRAM))
def out_contest(id):
    user_contest = UserJoinContest.query.filter_by(user_id=g.current_user.id, contest_id=verify_id(id), is_join=True).first()
    if not user_contest:
        return jsonify({'msg': 'no', 'error': 'out contest wrong'})
    db.session.delete(user_contest)
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/contests/<id>/users', methods=['PUT']), decorators.json_required, decorators.permission_required(Permission.SPONSOR))
def allow_join_or_out(id):
    contest = Contest.query.get(verify_id(id))
    if contest.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not modify other sponsor\'s contest'})
    user_id = request.json.get('user_id')
    user_contest = UserJoinContest.query.filter_by(user_id=verify_id(user_id), contest_id=verify_id(id)).first()
    if not user_contest:
        return jsonify({'msg': 'no', 'error': 'user or contest doesn\'t exist'})
    user_contest.is_join = False if user_contest.is_join else True
    return jsonify({'msg': 'ok', 'result': [{'is_join': user_contest.is_join}]})


@decorators.route('/contests', methods=['GET'])
def get_all_contests():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    paginate = Contest.query.order_by(Contest.id.desc()).paginate(page, per_page=per_page, error_out=False)
    return jsonify({'msg': 'ok', 'result': [item.to_json() for item in paginate.items]})


@decorators.route('/contests/<id>', methods=['GET'])
def get_contest_info(id):
    contest = Contest.query.get(verify_id(id))
    if not contest:
        return jsonify({'msg': 'no', 'error': 'contest doesn\'t exist'})
    json = contest.to_json()
    is_join = None
    if g.current_user.id:
        user_contest = UserJoinContest.query.filter_by(user_id=g.current_user.id, contest_id=verify_id(id)).first()
        if user_contest:
            is_join = user_contest.is_join
    json.update({'is_join': is_join})
    return jsonify({'msg': 'ok', 'result': [json]})


@decorators.route('/contests/<id>/users', methods=['GET'])
def get_contest_user(id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    is_join = request.args.get('is_join', True)
    paginate = UserJoinContest.query.filter_by(contest_id=verify_id(id), is_join=is_join).paginate(page, per_page=per_page, error_out=False)
    return jsonify({'msg': 'ok', 'result': [{'user_id': generate_id(item.user_id), 'user': item.user.username, 'is_join': item.is_join} for item in paginate.items]})


@decorators.composed(decorators.route('/contests', methods=['POST']), decorators.json_required, decorators.permission_required(Permission.SPONSOR))
def create_contest():
    keyword = {'title', 'description', 'start_time', 'end_time', 'auto_approve', 'password'}
    if not set(request.json.keys()).issubset(keyword):
        return jsonify({'msg': 'no', 'error': 'just require: {}'.format(keyword)})
    contest = Contest(user_id=g.current_user.id)
    for key in request.json:
        setattr(contest, key, request.json.get(key))
    db.session.add(contest)
    return jsonify({'msg': 'ok', 'result': [contest.to_json()]})


@decorators.composed(decorators.route('/contests/<id>', methods=['PUT']), decorators.json_required, decorators.permission_required(Permission.SPONSOR))
def update_contest_info(id):
    contest = Contest.query.get(verify_id(id))
    if contest.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not modify other sponsor\'s contest'})
    keyword = {'title', 'description', 'start_time', 'end_time', 'auto_approve', 'password'}
    if not set(request.json.keys()).issubset(keyword):
        return jsonify({'msg': 'no', 'error': 'update error'})
    for key in request.json:
        setattr(contest, key, request.json.get(key))
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/contests/<id>', methods=['DELETE']), decorators.permission_required(Permission.SPONSOR))
def delete_contest(id):
    contest = Contest.query.get(verify_id(id))
    if contest.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not delete other sponsor\'s contest'})
    if not contest:
        return jsonify({'msg': 'no', 'error': 'contests doesn\'t exist'})
    db.session.delete(contest)
    return jsonify({'msg': 'ok'})
