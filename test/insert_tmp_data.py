#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import create_app, db, models
import random
import string

app = create_app('development')
app_context = app.app_context()
app_context.push()


class User:
    @staticmethod
    def insert_UserRole():
        models.UserRole.insert_roles()

    @staticmethod
    def insert_User():
        who = ['user', 'administrator', 'sponsor', 'moderator']
        for i in who:
            user = models.User(username=i, email=i)
            user.password = i
            if i != 'user':
                role = models.UserRole.query.filter_by(name=i).first()
                user.role_id = role.id
            db.session.add(user)
        db.session.commit()

    @staticmethod
    def insert_UserInfo():
        users = models.User.query.all()
        for user in users:
            db.session.add(models.UserInfo(user_id=user.id, realname=user.username))
        db.session.commit()

    @staticmethod
    def insert_UserNote():
        role = models.UserRole.query.filter_by(name='user').first()
        for user in role.user:
            for i in range(1, 3):
                note = models.UserNote(user_id=user.id, problem_id=random.randint(1, 30), text=''.join(random.sample(string.ascii_letters + string.digits, 50)))
                db.session.add(note)
        db.session.commit()

    @staticmethod
    def insert_UserCollection():
        role = models.UserRole.query.filter_by(name='user').first()
        for user in role.user:
            for i in range(1, 3):
                collection = models.UserCollection(user_id=user.id, problem_id=random.randint(1, 30))
                db.session.add(collection)
        db.session.commit()

    @staticmethod
    def insert_UserLikeProblem():
        role = models.UserRole.query.filter_by(name='user').first()
        for user in role.user:
            for i in range(1, 3):
                like = models.UserLikeProblem(user_id=user.id, problem_id=random.randint(1, 30), is_like=True)
                db.session.add(like)
        db.session.commit()

    @staticmethod
    def insert_UserSubmitCode():
        role = models.UserRole.query.filter_by(name='user').first()
        for user in role.user:
            for i in range(1, 3):
                submit = models.UserSubmitCode(user_id=user.id, problem_id=random.randint(1, 30),
                        status='Accepted', language='Python3', time_used='1000', memory_used='45523',
                        code='print("hello")')
                db.session.add(submit)
        db.session.commit()

    @staticmethod
    def insert_UserJoinContest():
        role = models.UserRole.query.filter_by(name='user').first()
        for user in role.user:
            for i in range(1, 3):
                user_contest = models.UserJoinContest(user_id=user.id, contest_id=random.randint(1, 30))
                db.session.add(user_contest)
        db.session.commit()


class Problem:
    @staticmethod
    def insert_Problem():
        role = models.UserRole.query.filter_by(name='administrator').first()
        for user in role.user:
            for i in range(1, 31):
                problem = models.Problem(title=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                        level=random.randint(1, 3), tag=''.join(random.sample(string.ascii_letters, 4)),
                        description=''.join(random.sample(string.ascii_letters + string.digits, 50)),
                        code=''.join(random.sample(string.ascii_letters + string.digits, 20)),
                        solution=''.join(random.sample(string.ascii_letters + string.digits, 50)),
                        user_id=user.id)
                db.session.add(problem)
        db.session.commit()


class Contest:
    @staticmethod
    def insert_Contest():
        role = models.UserRole.query.filter_by(name='administrator').first()
        for sponsor in role.user:
            for i in range(1, 31):
                contest = models.Contest(user_id=sponsor.id,
                                        title=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                                        description=''.join(random.sample(string.ascii_letters + string.digits, 50)),
                                        start_time='2017-08-{} 06:02:18'.format(i),
                                        end_time='2017-09-{} 06:02:18'.format(i))
                db.session.add(contest)
        db.session.commit()


def run():
    db.session.remove()
    db.drop_all()
    print('drop all tables')
    db.create_all()
    print('create all tables')
    User.insert_UserRole()
    User.insert_User()
    User.insert_UserInfo()
    Problem.insert_Problem()
    User.insert_UserNote()
    User.insert_UserLikeProblem()
    User.insert_UserCollection()
    User.insert_UserSubmitCode()
    Contest.insert_Contest()
    User.insert_UserJoinContest()
    print('insert tmp data success')


if __name__ == '__main__':
    run()
