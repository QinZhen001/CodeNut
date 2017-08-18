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
import re
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


@app.errorhandler(405)
def error_method(error):
    # request not found, return 404
    return jsonify({'msg': 'no', 'error': 'request method error, please use correct method'}), 405


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
            return jsonify({'msg': 'no', 'error': 'json required'})
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
    template = db.Column(db.Text, nullable=True)
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


def verify_id(id):
    # verify id
    id = HashIDs().decrypt(id)
    if len(id) == 1:
        return id[0]
    else:
        return -1


def generate_id(id):
    # generate id
    return HashIDs().encrypt(id)


# for return and commit database
def json_format(iterator, pattern):
    if pattern == 'array':
        never = ['_sa_instance_state', 'description', 'solution', 'password', 'role']
        tmp = [{key: item.__dict__[key]
                if key != 'id' else generate_id(item.__dict__[key])
               for key in item.__dict__ if key not in never}
               for item in iterator]
        return jsonify({'result': tmp})
    elif pattern == 'object':
        never = ['_sa_instance_state', 'password', 'role']
        tmp = {key: iterator.__dict__[key]
                if key != 'id' else generate_id(iterator.__dict__[key])
                for key in iterator.__dict__ if key not in never}
        return jsonify(tmp)


def commit_delete(obj):
    try:
        db.session.delete(obj)
        db.session.commit()
        return jsonify({'msg': 'ok'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


def commit_update():
    try:
        db.session.commit()
        return jsonify({'msg': 'ok'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'no', 'error': str(e)})


# auth
def get_token():
    duration = 86400
    token = g.user.generate_auth_token(duration)
    return jsonify({'id': generate_id(g.user.id), 'token': token.decode('ascii'), 'duration': duration})


@app.route('/token', methods=['GET', 'POST'])
@auth.login_required
def get_auth_token():
    # usge: when receive {"error": "unauthorized"}, redirect to login view
    # if login successfully, get this token, and store it in client by localStorage
    return get_token()


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
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        if verify_password(username, password):
            return get_token()
    return unauthorized()


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
    return json_format(query, 'array')


# problems router
@app.route('/problems', methods=['GET'])
def get_all_problems():
    # GET to get all problems
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    paginate = Problem.query.order_by(Problem.id.desc()).paginate(page, per_page=per_page, error_out=False)
    # return all attribution and special one = 'None'
    return json_format(paginate.items, 'array')


@app.route('/problems/<id>', methods=['GET'])
def get_problem_detail(id):
    # GET to get a problem detail
    id = verify_id(id)
    problem = Problem.query.get(id)
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    return json_format(problem, 'object')


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


@app.route('/problems/<id>', methods=['PUT'])
@json_required
@auth.login_required
@manager_only
def update_problem(id):
    # PUT to update a problem
    id = verify_id(id)
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
    return commit_update()


@app.route('/problems/<id>', methods=['DELETE'])
@auth.login_required
@manager_only
def delete_problem(id):
    # DELETE to delete a problem
    id = verify_id(id)
    problem = Problem.query.get(id)
    if not problem:
        return jsonify({'msg': 'no', 'error': 'problem doesn\'t exist'})
    return commit_delete(problem)


# users router
@app.route('/users', methods=['GET'])
@auth.login_required
def get_all_users():
    # GET to get all users
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginate = User.query.order_by(User.id.desc()).paginate(page, per_page=per_page, error_out=False)
    # return all attribution and special one = 'None'
    return json_format(paginate.items, 'array')


@app.route('/users/<id>', methods=['GET'])
@auth.login_required
def get_user_detail(id):
    # GET to get a user detail
    id = verify_id(id)
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'no', 'error': 'user doesn\'t exist'})
    return json_format(user, 'object')


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


@app.route('/users/<id>', methods=['PUT'])
@json_required
@auth.login_required
def update_user(id):
    # PUT to update a user
    id = verify_id(id)
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
    return commit_update()


@app.route('/users/<id>', methods=['DELETE'])
@auth.login_required
@manager_only
def delete_users(id):
    id = verify_id(id)
    user = User.query.get(id)
    if not user:
        return jsonify({'msg': 'no', 'error': 'user doesn\'t exist'})
    return commit_delete(user)


# hashids Python port
# Written by Eric Martel - www.ericmartel.com
# Licensed under MIT - see LICENSE
class HashIDs:
    version = '0.0.1'
    __alphabet = 'xcS4F6h89aUbideAI7tkynuopqrXCgTE5GBKHLMjfRsz'
    __primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    __minHashLength = 0

    def __init__(self, salt='the quick brown fox jumps over the lazy dog', minHashLength=0, alphabet=None):
        if not isinstance(salt, str):
            raise ValueError('Salt should be a string')

        self.__salt = salt

        if minHashLength is not None and isinstance(minHashLength, int) and minHashLength > 0:
            self.__minHashLength = minHashLength

        if alphabet is not None and isinstance(alphabet, str) and len(alphabet) > 0:
            if len(alphabet) < 4:
                raise ValueError('The alphabet should contain at least 4 unique symbols')

            # Make sure the user created alphabet only contains unique values
            self.__alphabet = ''.join(set(alphabet))

        self.__guards = []
        self.__seps = []

        for prime in self.__primes:
            if prime - 1 > len(self.__alphabet):
                break

            character = self.__alphabet[prime - 1]
            self.__seps.append(character)
            self.__alphabet = self.__alphabet.replace(character, ' ')

        for index in [0, 4, 8, 12]:
            if index > len(self.__seps):
                break

            sep = self.__seps[index]
            self.__guards.append(sep)
            self.__seps.remove(sep)

        self.__alphabet = self.__alphabet.replace(' ', '')
        self.__alphabet = self.__shuffle(self.__alphabet, self.__salt)

    def encrypt(self, *values):
        ret = ''

        if len(values) == 0:
            return ret

        for number in values:
            if not isinstance(number, int) or number < 0:
                return ret

        return self.__encode(values, self.__alphabet, self.__salt, self.__minHashLength)

    def decrypt(self, hash):
        if not hash or not isinstance(hash, str):
            raise ValueError('Hash should be a string')
        return self.__decode(hash)

    def __encode(self, values, alphabet, salt, minHashLength):
        ret = ''

        seps = list(self.__shuffle(self.__seps, values))

        for idx, val in enumerate(values):
            if not idx:
                lotterySalt = '-'.join('%d' % value for value in values)
                for subNumber in values:
                    lotterySalt += '-' + str((subNumber + 1) * 2)

                lottery = self.__shuffle(alphabet, lotterySalt)
                lotteryChar = lottery[0]
                ret += lotteryChar

                alphabet = lotteryChar + alphabet.replace(lotteryChar, '')

            alphabet = self.__shuffle(alphabet, str((ord(lotteryChar) & 12345)) + salt)
            ret += self.__hash(val, alphabet)

            if idx + 1 < len(values):
                sepsIndex = (val + idx) % len(seps)
                ret += seps[sepsIndex]

        if len(ret) < minHashLength:
            firstIndex = 0
            for idx, val in enumerate(values):
                firstIndex += (idx + 1) * val

            guardIndex = firstIndex % len(self.__guards)
            guard = self.__guards[guardIndex]

            ret = guard + ret
            if len(ret) < minHashLength:
                guardIndex = (guardIndex + len(ret)) % len(self.__guards)
                guard = self.__guards[guardIndex]

                ret += guard

        while len(ret) < minHashLength:
            padList = [str(ord(alphabet[1])), str(ord(alphabet[0]))]

            padLeft = self.__encode(padList, alphabet, salt, minHashLength)
            padRight = self.__encode(padList, alphabet, ''.join(padList), minHashLength)

            ret = padLeft + ret + padRight
            excess = len(ret) - minHashLength

            if excess > 0:
                trim = excess / 2
                ret = ret[trim:minHashLength + trim]

            alphabet = self.__shuffle(alphabet, salt + ret)

        return ret

    def __decode(self, hash):
        ret = []

        if len(hash):
            originalHash = hash

            hash = re.sub('[%s]' % ''.join(self.__guards), '', hash)
            hashExplode = hash.split(' ')

            i = 0
            if len(hashExplode) == 3 or len(hashExplode) == 2:
                i = 1

            hash = hashExplode[i]

            hash = re.sub('[%s]' % ''.join(self.__seps), ' ', hash)
            hashArray = hash.split(' ')

            alphabet = ""
            lotteryChar = ''

            for idx, subHash in enumerate(hashArray):
                if len(subHash):
                    if not idx:
                        lotteryChar = hash[0]
                        subHash = subHash[1:]
                        alphabet = lotteryChar + self.__alphabet.replace(lotteryChar, '')

                    alphabet = self.__shuffle(alphabet, str(ord(lotteryChar) & 12345) + self.__salt)
                    number = self.__dehash(subHash, alphabet)
                    ret.append(number)

            encryptResult = self.encrypt(*ret)
            if encryptResult != originalHash:
                ret = []
        return ret

    @staticmethod
    def __shuffle(alphabet, salt):
        if isinstance(alphabet, list):
            alphabet = ''.join(alphabet)

        if isinstance(salt, list):
            salt = ''.join(salt)

        if isinstance(salt, tuple):
            salt = ''.join('%d' % num for num in salt)

        if alphabet:
            alphabetList = list(alphabet)

            sortingList = [ord(character) for character in salt]

            for i in range(len(sortingList)):
                add = True
                for k in range(i, len(sortingList) + i - 1):
                    nextIndex = (k + 1) % len(sortingList)
                    if add:
                        sortingList[i] += sortingList[nextIndex] + (k * i)
                    else:
                        sortingList[i] -= sortingList[nextIndex]
                    add = not add
                sortingList[i] = abs(sortingList[i])

            i = 0
            ret = ''
            sortingArraySize = len(sortingList)
            while len(alphabetList) > 0:
                size = len(alphabetList)
                pos = sortingList[i]

                if pos >= size:
                    pos = pos % size

                ret += alphabetList.pop(pos)

                i = (i + 1) % sortingArraySize
            return ret
        return None

    @staticmethod
    def __hash(input, alphabet):
        hash = ''
        alphabetLength = len(alphabet)

        while True:
            index = (input % alphabetLength)

            hash = alphabet[index] + hash
            input = int(input / alphabetLength)

            if not input:
                break
        return hash

    @staticmethod
    def __dehash(input, alphabet):
        number = 0

        if len(input) and alphabet:
            alphabetLength = len(alphabet)
            inputChars = input[::1]

            for idx, character in enumerate(inputChars):
                pos = alphabet.find(character)
                number += pos * pow(alphabetLength, (len(input) - idx - 1))

        return number

if __name__ == '__main__':
    # """
    app.run(debug=True)
    """
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0', port=5000, debug=False)
    #"""
