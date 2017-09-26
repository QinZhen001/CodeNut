#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import current_app
from app import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import time
from tools.HashIDs import generate_id


class Problem(db.Model):
    __tablename__ = 'codenut_problems'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=False, unique=True, index=True)
    level = db.Column(db.SmallInteger, nullable=False)
    tag = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=False)
    accepted = db.Column(db.Integer, default='0')
    submitted = db.Column(db.Integer, default='0')
    description = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text)
    contest_id = db.Column(db.Integer, db.ForeignKey('codenut_contests.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))  # who create

    user = db.relationship('User', backref='Problem', uselist=False, lazy='select')
    user_accept_code = db.relationship('UserAcceptCode', backref='Problem', uselist=False)

    def list_to_json(self):
        like_nums = len(UserLikeProblem.query.filter_by(problem_id=self.id, is_like=True).all())
        hate_nums = len(UserLikeProblem.query.filter_by(problem_id=self.id, is_like=False).all())
        json = {
            'id': generate_id(self.id),
            'title': self.title,
            'level': self.level,
            'tag': self.tag,
            'accepted': self.accepted,
            'submitted': self.submitted,
            'like_nums': like_nums,
            'hate_nums': hate_nums
        }
        return json

    def info_to_json(self):
        json = self.list_to_json()
        json.update({'description': self.description})
        return json

    def solution_to_json(self):
        solution = self.solution if self.solution is not None else 'null'
        json = {'solution': solution}
        return json

    def __repr__(self):
        return '<Problem(title={})>'.format(self.title)


class Contest(db.Model):
    __tablename__ = 'codenut_contests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    title = db.Column(db.Unicode(128, collation='utf8_bin'), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    auto_approve = db.Column(db.Boolean, default=True)  # auto approve user join
    password = db.Column(db.Unicode(32, collation='utf8_bin'))  # for user who know contest password

    user = db.relationship('User', backref='Contest', uselist=False, lazy='select')
    problem = db.relationship('Problem', backref='Contest', lazy='dynamic', cascade='all, delete-orphan')

    def to_json(self):
        user_nums = len(UserJoinContest.query.filter_by(contest_id=self.id, is_join=True).all())
        json = {
            'id': generate_id(self.id),
            'sponsor': self.user.username,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'user_nums': user_nums,
            'auto_approve': self.auto_approve
        }
        return json

    def __repr__(self):
        return '<Contest(title={})>'.format(self.title)


class UserLikeProblem(db.Model):
    __tablename__ = 'codenut_user_like_problems'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('codenut_problems.id'))
    is_like = db.Column(db.Boolean)

    user = db.relationship('User', backref='UserLikeProblem', uselist=False, lazy='select')
    problem = db.relationship('Problem', backref='UserLikeProblem', uselist=False, lazy='select')

    def __repr__(self):
        return '<UserLikeProblem(user_id={}, problem_id={}, islike={})>'.format(self.user_id, self.problem_id, self.islike)


class UserSubmitCode(db.Model):
    __tablename__ = 'codenut_user_submit_codes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('codenut_problems.id'))
    code_id = db.Column(db.Integer, db.ForeignKey('codenut_user_accept_codes.id'))
    status = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=False)
    language = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=False)
    time_used = db.Column(db.Float, nullable=False)
    memory_used = db.Column(db.Float, nullable=False)
    create_time = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
    update_time = db.Column(db.DateTime)

    user = db.relationship('User', backref='UserSubmitCode', uselist=False, lazy='select')
    problem = db.relationship('Problem', backref='UserSubmitProblem', uselist=False, lazy='select')

    def to_json(self):
        json = {
            'user_id': generate_id(self.user_id),
            'problem_id': generate_id(self.problem_id),
            'code_id': generate_id(self.code_id),
            'status': self.status,
            'language': self.language,
            'time_used': self.time_used,
            'memory_used': self.memory_used,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
        return json

    def __init__(self, **kwargs):
        # attr code not belong this class
        code = kwargs.pop('code')
        super().__init__(**kwargs)
        # store user code
        # only when result status is 'Accepted'
        if self.status == 'Accepted' and self.update_time is None:
            user_code = UserAcceptCode(user_id=self.user_id, problem_id=self.problem_id, code=code)
            self.code_id = user_code.id
            db.session.add(user_code)
            db.session.commit()

    def __repr__(self):
        return '<UserProblem(user_id={})>'.format(self.user_id)


class UserAcceptCode(db.Model):
    __tablename__ = 'codenut_user_accept_codes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('codenut_problems.id'))
    code = db.Column(db.Text)

    submit_code = db.relationship('UserSubmitCode', backref='UserAcceptCode', uselist=False)
    problem = db.relationship('Problem', backref='UserAcceptCode', uselist=False, lazy='select')

    def __repr__(self):
        return '<UserAcceptCode(problem_id={})>'.format(self.problem_id)


class UserJoinContest(db.Model):
    __tablename__ = 'codenut_user_join_contests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    contest_id = db.Column(db.Integer, db.ForeignKey('codenut_contests.id'))
    # sponsor have to approve by hand if contest is not auto approve
    is_join = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref='UserJoinContest', uselist=False, lazy='select')
    contest = db.relationship('Contest', backref='UserJoinContest', uselist=False, lazy='select')

    def __repr__(self):
        return '<UserJoinContest(user_id={})>'.format(self.user_id)


class UserCollection(db.Model):
    __tablename__ = 'codenut_user_collections'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('codenut_problems.id'))

    user = db.relationship('User', backref='UserCollection', uselist=False, lazy='select')
    problem = db.relationship('Problem', backref='UserCollection', uselist=False, lazy='select')

    def to_json(self):
        json = {
            'user_id': generate_id(self.user_id),
            'problem_id': generate_id(self.problem_id),
            'username': self.user.username,
            'problem': self.problem.title
        }
        return json

    def __repr__(self):
        return '<UserCollection(user_id={}, problem_id={})>'.format(self.user_id, self.problem_id)


class UserNote(db.Model):
    __tablename__ = 'codenut_user_notes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('codenut_problems.id'))
    text = db.Column(db.Text)

    user = db.relationship('User', backref='UserNote', uselist=False, lazy='select')
    problem = db.relationship('Problem', backref='UserNote', uselist=False, lazy='select')

    def __repr__(self):
        return '<UserNote(problem_id={})>'.format(self.problem_id)


class UserInfo(db.Model):
    __tablename__ = 'codenut_user_infos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('codenut_users.id'), index=True)
    realname = db.Column(db.Unicode(32, collation='utf8_bin'))
    profile = db.Column(db.Text)
    school = db.Column(db.Unicode(64, collation='utf8_bin'))
    about_me = db.Column(db.Unicode(512, collation='utf8_bin'))
    tag = db.Column(db.Unicode(128, collation='utf8_bin'))
    create_time = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
    login_time = db.Column(db.DateTime)

    user = db.relationship('User', backref='UserInfo', uselist=False, lazy='select')

    def to_json(self):
        submit_nums = len(UserSubmitCode.query.filter_by(user_id=self.user_id).all())
        accept_nums = len(UserAcceptCode.query.filter_by(user_id=self.user_id).all())
        json = {
            'user_id': generate_id(self.user_id),
            'username': self.user.username,
            'realname': self.realname,
            'profile': self.profile,
            'school': self.school,
            'about_me': self.about_me,
            'tag': self.tag,
            'submit_nums': submit_nums,
            'accept_nums': accept_nums,
            'create_time': self.create_time,
            'login_time': self.login_time
        }
        return json

    def __repr__(self):
        return '<UserInfo(user_id={})>'.format(self.user_id)


class User(db.Model):
    __tablename__ = 'codenut_users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(64, collation='utf8_bin'), nullable=False, unique=True, index=True)
    username = db.Column(db.Unicode(32, collation='utf8_bin'), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.Unicode(256, collation='utf8_bin'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('codenut_user_roles.id'))

    role = db.relationship('UserRole', backref='User', uselist=False, lazy='select')
    info = db.relationship('UserInfo', backref='User', uselist=False, lazy='select', cascade='all, delete-orphan')
    contests_joined = db.relationship('UserJoinContest', backref='User', lazy='dynamic', cascade='all, delete-orphan')
    contests_sponsor = db.relationship('Contest', backref='User', lazy='dynamic', cascade='all, delete-orphan')
    codes_submitted = db.relationship('UserSubmitCode', backref='User', lazy='dynamic', cascade='all, delete-orphan')
    problems_liked = db.relationship('UserLikeProblem', backref='User', lazy='dynamic', cascade='all, delete-orphan')
    notes = db.relationship('UserNote', backref='User', lazy='dynamic', cascade='all, delete-orphan')
    collections = db.relationship('UserCollection', backref='User', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return '<User(username={})>'.format(self.username)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role_id is None:
            if self.username == 'administrator':
                role = UserRole.query.filter_by(permissions=0xff).first()
            else:
                role = UserRole.query.filter_by(default=True).first()
            self.role_id = role.id

    def operation(self, permissions):
        return self.role_id is not None and (self.role.permissions & permissions) == permissions

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


class AnonymousUser(User):
    def operation(self, permissions):
        return False


class Permission:
    PROGRAM = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    SPONSOR = 0x10
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class UserRole(db.Model):
    __tablename__ = 'codenut_user_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    user = db.relationship('User', backref='UserRole', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def insert_roles():
        roles = {
            'user': (Permission.PROGRAM |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'moderator': (Permission.PROGRAM |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'sponsor': (Permission.PROGRAM |
                        Permission.COMMENT |
                        Permission.WRITE_ARTICLES |
                        Permission.SPONSOR, False),
            'administrator': (0xff, False)
        }
        for r in roles:
            role = UserRole.query.filter_by(name=r).first()
            if role is None:
                role = UserRole(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<UserRole(nanme={}, permissions={})>'.format(self.name, self.permissions)
