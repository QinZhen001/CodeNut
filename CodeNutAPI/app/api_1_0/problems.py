#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, jsonify, g
from tools.HashIDs import generate_id, verify_id
from . import decorators
from ..models import db, Problem, UserSubmitCode, UserCollection, UserAcceptCode, UserNote, UserLikeProblem, Permission
import time
from dispatcher import tasks
from dispatcher.task import ProblemTask
import msgpack
import random
import string


@decorators.composed(decorators.route('/problems/<id>/codes', methods=['PATCH']), decorators.json_required,
                     decorators.permission_required(Permission.PROGRAM))
def run_code(id):
    keyword = {'language', 'code', 'custom_input'}
    if not set(request.json.keys()).issubset(keyword):
        return jsonify({'msg': 'no', 'error': 'just require: {}'.format(keyword)})

    problem = ProblemTask(id=verify_id(id), user_id=str(g.current_user.id),
                          language=request.json.get('language'),
                          code=request.json.get('code'),
                          custom_input=request.json.get('custom_input'))
    r = tasks.judge.delay(msgpack.packb(problem.to_json()))
    while not r.ready():
        time.sleep(0.1)
    result = r.result

    return jsonify({'msg': 'ok', 'result': [{'output': result['output'], 'status': result['status'],
                                             'time_used': result['time_used'], 'memory_used': result['memory_used']}]})


@decorators.composed(decorators.route('/problems/<id>/codes', methods=['POST']), decorators.json_required,
                     decorators.permission_required(Permission.PROGRAM))
def submit_code(id):
    keyword = {'language', 'code', 'custom_input'}
    if not set(request.json.keys()).issubset(keyword):
        return jsonify({'msg': 'no', 'error': 'just require: {}'.format(keyword)})

    """
    problem = ProblemTask(id=verify_id(id), user_id=str(g.current_user.id),
                        language=request.json.get('language'),
                        code=request.json.get('code'),
                        custom_input=request.json.get('custom_input'))
    r = tasks.judge.delay(msgpack.packb(problem.to_json()))
    while not r.ready():
        time.sleep(0.1)
    result = r.result

    # if accepted already, update code
    accept = UserAcceptCode.query.filter_by(user_id=problem.user_id, problem_id=problem.id).first()
    if accept:
        accept.submit_code.update_time = time.strftime('%Y-%m-%d %H:%M:%S')
        accept.code = request.json.get('code')
    else:
        submit = UserSubmitCode(user_id=problem.user_id, problem_id=problem.id, code=request.json.get('code'), status=result['status'],
                                language=problem.language, time_used=result['time_used'], memory_used=result['memory_used'])
        db.session.add(submit)
    """

    # for test
    result = {'output': ''.join(random.sample(string.ascii_lowercase + string.digits, 20)),
              'status': random.choice(['System Error',
                                       'Accepted',
                                       'Wrong Answer',
                                       'Dangerous System Call',
                                       'Runtime Error',
                                       'Compile Error',
                                       'Time Limit Exceed',
                                       'Memory Limit Exceed',
                                       'Output Limit Exceed',
                                       'Run Successfully']), 'time_used': random.uniform(0, 1),
              'memory_used': random.uniform(1, 6000)}

    return jsonify({'msg': 'ok', 'result': [{'output': result['output'], 'status': result['status'],
                                             'time_used': result['time_used'], 'memory_used': result['memory_used']}]})


@decorators.route('/problems', methods=['GET'])
def get_all_problems():
    contest_id = request.args.get('contest_id', None)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    paginate = Problem.query.filter_by(contest_id=contest_id).order_by(Problem.id.desc()).paginate(page,
                                                                                                   per_page=per_page, error_out=False)
    return jsonify({'msg': 'ok', 'result': [item.list_to_json() for item in paginate.items]})


@decorators.route('/problems/<id>', methods=['GET'])
def get_problem_info(id):
    problem = Problem.query.get(verify_id(id))
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    return jsonify({'msg': 'ok', 'result': [problem.info_to_json()]})


@decorators.composed(decorators.route('/problems', methods=['POST']), decorators.json_required,
                     decorators.permission_required(Permission.SPONSOR))
def create_problem():
    keyword = {'title', 'description', 'level',
               'tag', 'code', 'input', 'output', 'program'}
    if not set(request.json.keys()) == keyword:
        return jsonify({'msg': 'no', 'error': 'just require: {}'.format(keyword)})
    if Problem.query.filter_by(title=request.json.get('title')).first():
        return jsonify({'msg': 'no', 'error': 'title: {} is already existed'.format(request.json.get('title'))})

    problem = Problem(user_id=g.current_user.id)
    for key in request.json:
        setattr(problem, key, request.json.get(key))
    db.session.add(problem)
    db.session.flush()
    return jsonify({'msg': 'ok', 'result': [{'title': problem.title, 'id': generate_id(problem.id)}]})


@decorators.composed(decorators.route('/problems/<id>', methods=['PUT']), decorators.json_required,
                     decorators.permission_required(Permission.SPONSOR))
def update_problem_info(id):
    problem = Problem.query.get(verify_id(id))
    if problem.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not modify other sponsor\'s problem'})
    keyword = {'title', 'level', 'tag', 'description',
               'code', 'input', 'output', 'program'}
    if not set(request.json.keys()).issubset(keyword):
        return jsonify({'msg': 'no', 'error': 'update error'})
    for key in request.json:
        if key == 'title' and Problem.query.filter_by(title=request.json.get('title')).first():
            return jsonify({'msg': 'no', 'error': 'title: {} is already existed'.format(request.json.get(key))})
        setattr(problem, key, request.json.get(key))
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/problems/<id>', methods=['DELETE']),
                     decorators.permission_required(Permission.SPONSOR))
def delete_problem(id):
    problem = Problem.query.get(verify_id(id))
    if problem.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not delete other sponsor\'s problem'})
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    db.session.delete(problem)
    return jsonify({'msg': 'ok'})


@decorators.route('/problems/<id>/codes', methods=['GET'])
def get_problem_code(id):
    code = None
    if g.current_user.id:
        code = UserAcceptCode.query.filter_by(
            user_id=g.current_user.id, problem_id=verify_id(id)).first()
    if not code:
        code = Problem.query.get(verify_id(id))  # waite for web front
    return jsonify({'msg': 'ok', 'result': [{'code': code.code}]})


@decorators.route('/problems/<id>/solutions', methods=['GET'])
def get_problem_solution(id):
    problem = Problem.query.get(verify_id(id))
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    return jsonify({'msg': 'ok', 'result': [problem.solution_to_json()]})


@decorators.composed(decorators.route('/problems/<id>/solutions', methods=['PUT']), decorators.json_required,
                     decorators.permission_required(Permission.SPONSOR))
def update_problem_solution(id):
    problem = Problem.query.get(verify_id(id))
    if problem.user_id != g.current_user.id:
        return jsonify({'msg': 'no', 'error': 'do not modify other sponsor\'s solution'})
    problem.solution = request.json.get('solution')
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/problems/<id>/notes', methods=['GET']),
                     decorators.permission_required(Permission.PROGRAM))
def get_user_notes(id):
    note = UserNote.query.filter_by(
        user_id=g.current_user.id, problem_id=verify_id(id)).first()
    if not note:
        return jsonify({'msg': 'no', 'error': 'note doesn\'t exist'})
    return jsonify({'msg': 'ok', 'result': [{'text': note.text}]})


@decorators.composed(decorators.route('/problems/<id>/notes', methods=['PUT']), decorators.json_required,
                     decorators.permission_required(Permission.PROGRAM))
def update_user_notes(id):
    note = UserNote.query.filter_by(
        user_id=g.current_user.id, problem_id=verify_id(id)).first()
    text = request.json.get('text')
    if not note:
        note = UserNote(user_id=g.current_user.id,
                        problem_id=verify_id(id), text=text)
        db.session.add(note)
    else:
        note.text = text
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/problems/<id>/collections', methods=['POST']),
                     decorators.permission_required(Permission.PROGRAM))
def add_collection(id):
    collection = UserCollection(
        user_id=g.current_user.id, problem_id=verify_id(id))
    db.session.add(collection)
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/problems/<id>/collections', methods=['DELETE']),
                     decorators.permission_required(Permission.PROGRAM))
def delete_collection(id):
    collection = UserCollection.query.filter_by(
        user_id=g.current_user.id, problem_id=verify_id(id)).first()
    db.session.delete(collection)
    return jsonify({'msg': 'ok'})


@decorators.composed(decorators.route('/problems/<id>/likes', methods=['PUT']),
                     decorators.permission_required(Permission.PROGRAM))
def like_problem(id):  # true: like, false: hate, none: no feel
    true_or_false_or_none = request.args.get('true_or_false_or_none', None)
    like = UserLikeProblem.query.filter_by(
        user_id=g.current_user.id, problem_id=verify_id(id)).first()
    if not like:
        like = UserLikeProblem(user_id=g.current_user.id, problem_id=verify_id(
            id), is_like=true_or_false_or_none)
        db.session.add(like)
    else:
        like.is_like = true_or_false_or_none
    return jsonify({'msg': 'ok'})
