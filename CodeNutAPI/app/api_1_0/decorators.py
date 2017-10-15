#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps
from flask import request, jsonify, g
from ..models import db
from . import api


def route(rule, **options):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            rest = func(*args, **kwargs)
            try:
                db.session.commit()
                return rest
            except Exception as e:
                db.session.rollback()
                return jsonify({'msg': 'no', 'error': str(e)})
            finally:
                db.session.remove()

        endpoint = options.pop('endpoint', None)
        api.add_url_rule(rule, endpoint, decorated_function, **options)
        return decorated_function

    return decorator


def composed(*decorators):
    # compose 2 or more decorator
    def decorator(func):
        for dec in reversed(decorators):
            func = dec(func)
        return func

    return decorator


def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not g.current_user.operation(permission):
                return jsonify({'msg': 'no', 'error': 'insufficient permissions'})
            return func(*args, **kwargs)

        return decorated_function

    return decorator


def json_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not request.json:
            return jsonify({'msg': 'no', 'error': 'required json'})
        return func(*args, **kwargs)

    return decorated_function
