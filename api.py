#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_cors import CORS
from functools import wraps
import json
from werkzeug.contrib.fixers import ProxyFix

# initialization
app = Flask(__name__)
# token secret key
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# set database url
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/codenut?charset=utf8'
# auto commit database modify when request teardown
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
CORS(app)


# custom json format error
@app.errorhandler(400)
def error_request(error):
    # error request, return 400
    return jsonify({'msg': 'no', 'error': 'error request'}), 400


@app.errorhandler(403)
def forbidden(error):
    # server forbid the request, return 403
    return jsonify({'msg': 'no', 'error': 'forbidden'}), 403


@app.errorhandler(404)
def not_found(error):
    # request not found, return 404
    return jsonify({'msg': 'no', 'error': 'not found'}), 404


@app.errorhandler(408)
def time_out(error):
    # request time out, return 408
    return jsonify({'msg': 'no', 'error': 'time out'}), 408


@app.errorhandler(500)
def internal_error(error):
    # server internal error, return 500
    return jsonify({'msg': 'no', 'error': 'server internal error'}), 500


@app.errorhandler(503)
def unavailable(error):
    # request not found, return 503
    return jsonify({'msg': 'no', 'error': 'service unavailable'}), 503


# wrapper
def manager_only(func):
    # wrapper: only manager role can delete or other thing.
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if g.user.role != 3:
            return jsonify({'msg': 'no', 'error': 'do not go beyond manager\'s commission'})
        return func(*args, **kwargs)

    return wrapped_func


def json_required(func):
    # wrapper: require json request
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if not request.json:
            return jsonify({'msg': 'no', 'error': 'require json request'})
        return func(*args, **kwargs)

    return wrapped_func


@app.route('/resource', methods=['GET', 'POST'])
@auth.login_required
@manager_only
def test_wrapper():
    return jsonify({'data': 'Hello, %s!' % g.user.username})


# Model
class Problem(db.Model):
    """Problem Model"""
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=False)
    accepted = db.Column(db.Integer, server_default='0')
    submitted = db.Column(db.Integer, server_default='0')
    solution = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Problem(title='%s')>" % self.title


class User(db.Model):
    """User Model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=False, unique=True)
    password = db.Column(db.Unicode(256, collation='utf8_bin'), nullable=False)
    username = db.Column(db.Unicode(32, collation='utf8_bin'), nullable=False, unique=True, index=True)
    realname = db.Column(db.Unicode(32, collation='utf8_bin'), nullable=True)
    profile = db.Column(db.Unicode(256, collation='utf8_bin'), nullable=True)
    occupation = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=True)
    school = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=True)
    company = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=True)
    about_me = db.Column(db.Text, nullable=True)
    blog = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=True)
    role = db.Column(db.Integer, server_default='0')

    def __repr__(self):
        return "<User(name='%s')>" % self.username

    def hash_password(self, password):
        self.password = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


# auth
@app.route('/token', methods=['GET', 'POST'])
@auth.login_required
def get_auth_token():
    # usge: when receive {"error": "unauthorized"}, redirect to login view
    # if login successfully, get this token, and store it in client by localStorage
    token = g.user.generate_auth_token(86400)
    return jsonify({'token': token.decode('ascii'), 'duration': 86400})


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth.error_handler
def unauthorized():
    # request need login, return 403
    # (401: unauthorized, but it will alert a login window, so 403 instead of 401)
    return jsonify({'msg': 'no', 'error': 'unauthorized'}), 403


# router
@app.route('/search', methods=['POST'])
@json_required
def search():
    # target: Model, type: Model attribute, content: going to search
    target = request.json.get('target')
    type = request.json.get('type')
    content = request.json.get('content')
    cls = eval(target)
    attr = eval(target + '.' + type)
    query = db.session.query(cls).filter(attr.like('%{}%'.format(content))).all()
    return json.dumps([{key: i.__dict__[key]
                        if key != '_sa_instance_state' and key != 'description' and key != 'solution'
                        and key != 'password' and key != 'role'
                        else None for key in i.__dict__} for i in query])


# problems router
@app.route('/problems', methods=['GET'])
def get_all_problems():
    # GET to get all problems
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    paginate = Problem.query.order_by(Problem.id.desc()).paginate(page, per_page=per_page, error_out=False)
    # return all attribution and special one = 'None'
    return json.dumps([{key: problem.__dict__[key]
                        if key != '_sa_instance_state' and key != 'description' and key != 'solution'
                        else None for key in problem.__dict__} for problem in paginate.items])


@app.route('/problems/<int:id>', methods=['GET'])
def get_problem_detail(id):
    # GET to get a problem detail
    problem = Problem.query.get(id)
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    return jsonify({key: problem.__dict__[key]
                    if key != '_sa_instance_state'
                    else None for key in problem.__dict__})


@app.route('/problems', methods=['POST'])
@json_required
@auth.login_required
@manager_only
def create_problem():
    # POST to create a problem
    # require: title, description, level, tag
    keyword = ['title', 'description', 'level', 'tag']
    for key in keyword:
        if key not in request.json:
            return jsonify({'msg': 'no', 'error': 'missing arguments, require: title, description, level, tag'})
    # title is already existed
    if Problem.query.filter_by(title=request.json.get('title')).first() is not None:
        return jsonify({'msg': 'no', 'error': '{} is already existed'.format(request.json.get('title'))})

    problem = Problem()
    for key in request.json:
        setattr(problem, key, request.json.get(key))
    try:
        db.session.add(problem)
        db.session.commit()
        return (jsonify({'msg': 'ok', 'title': problem.title}), 201,
                {'Location': url_for('get_problem_detail', id=problem.id, _external=True)})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


@app.route('/problems/<int:id>', methods=['PUT'])
@json_required
@auth.login_required
@manager_only
def update_problem(id):
    # PUT to update a problem
    old = Problem.query.get(id)
    for key in request.json:
        # if key is wrong
        if key not in old.__dict__:
            return jsonify({'msg': 'no', 'error': 'Problem has no attribute {}'.format(key)})
        # do not modify these attribution
        if key == 'id':
            return jsonify({'msg': 'no', 'error': 'can not modify {}'.format(key)})
        # set old user's attribution as json value
        setattr(old, key, request.json.get(key))
    try:
        db.session.commit()
        return jsonify({'msg': 'yes'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


@app.route('/problems/<int:id>', methods=['DELETE'])
@auth.login_required
@manager_only
def delete_problem(id):
    # DELETE to delete a problem
    problem = Problem.query.get(id)
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    try:
        db.session.delete(problem)
        db.session.commit()
        return jsonify({'msg': 'yes'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


# users router
@app.route('/users', methods=['GET'])
@auth.login_required
def get_all_users():
    # GET to get all users
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginate = User.query.order_by(User.id.desc()).paginate(page, per_page=per_page, error_out=False)
    # return all attribution and special one = 'None'
    return json.dumps([{key: user.__dict__[key]
                        if key != '_sa_instance_state' and key != 'password' and key != 'role'
                        else None for key in user.__dict__} for user in paginate.items])


@app.route('/users/<int:id>', methods=['GET'])
@auth.login_required
def get_user_detail(id):
    # GET to get a user detail
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'no', 'error': 'user doesn\'t exist'})
    return jsonify({key: user.__dict__[key]
                    if key != '_sa_instance_state' and key != 'password'
                    else None for key in user.__dict__})


@app.route('/users', methods=['POST'])
@json_required
def create_user():
    # POST to create a user
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    # require these value
    if username is None or password is None or email is None:
        return jsonify({'msg': 'no', 'error': 'missing arguments, require: email, username, password'})
    # user or email is already existed
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'msg': 'no', 'error': 'username: {} is already existed'.format(username)})
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'msg': 'no', 'error': 'email: {} is already existed'.format(email)})
    user = User(email=email, username=username)
    user.hash_password(password)
    try:
        db.session.add(user)
        db.session.commit()
        return (jsonify({'msg': 'ok', 'email': user.email, 'username': user.username}), 201,
                {'Location': url_for('get_user_detail', id=user.id, _external=True)})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


@app.route('/users/<int:id>', methods=['PUT'])
@json_required
@auth.login_required
def update_user(id):
    # PUT to update a user
    old = User.query.get(id)
    for key in request.json:
        # if key is wrong
        if key not in old.__dict__ and key != 'oldpassword':
            return jsonify({'msg': 'no', 'error': 'User has no attribute {}'.format(key)})
        # do not modify these attribution
        if key == 'id' or key == 'username' or key == 'role':
            return jsonify({'msg': 'no', 'error': 'can not modify {}'.format(key)})
        # if new password not None
        if key == 'oldpassword' or key == 'password':
            # check old password that is correct or not
            # after modify, must logout!
            if not verify_password(old.username, request.json.get('oldpassword')):
                return jsonify({'msg': 'no', 'error': 'old password not correct'})
            old.hash_password(request.json.get('password'))
        else:
            # set old user's attribution as json value
            setattr(old, key, request.json.get(key))
    try:
        db.session.commit()
        return jsonify({'msg': 'yes'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


@app.route('/users/<int:id>', methods=['DELETE'])
@auth.login_required
@manager_only
def delete_users(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'no', 'error': 'user doesn\'t exist'})
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'msg': 'yes'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})

if __name__ == '__main__':
    #"""
    # db.drop_all()
    db.create_all()
    app.run(debug=True)
    #"""
    """
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0', port=5000, debug=False)
    """
