#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User, AnonymousUser
from tools.HashIDs import generate_id
from . import api

auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized(error='unauthorized'):
    # request need login, return 403
    # 401: unauthorized, but it will alert a login window, so 403 instead of 401
    return jsonify({'msg': 'no', 'error': error}), 403


@auth.verify_password
def verify_password(token_or_email_or_username, password):
    flag = True
    if not token_or_email_or_username:
        g.current_user = AnonymousUser()
        return flag
    # first try to authenticate by token
    user = User.verify_auth_token(token_or_email_or_username)
    if not user:
        # try to authenticate with email/password
        user = User.query.filter_by(email=token_or_email_or_username).first()
        if not user:
            # try to authenticate with username/password
            user = User.query.filter_by(username=token_or_email_or_username).first()
            if not user:
                return False
        flag = user.verify_password(password)
    g.current_user = user
    return flag


@api.before_request
@auth.login_required
def before_request():
    pass


def get_token(duration=18000):
    token = g.current_user.generate_auth_token(duration)
    return jsonify({'msg': 'ok', 'result': [{'id': generate_id(g.current_user.id), 'token': token.decode('ascii'), 'duration': duration}]})
