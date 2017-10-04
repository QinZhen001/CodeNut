#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify
from . import doc


@doc.app_errorhandler(400)
def error_request(error):
    return jsonify({'msg': 'no', 'error': 'error request'}), 400


@doc.app_errorhandler(403)
def forbidden(error):
    return jsonify({'msg': 'no', 'error': 'forbidden'}), 403


@doc.app_errorhandler(404)
def not_found(error):
    return jsonify({'msg': 'no', 'error': 'not found'}), 404


@doc.app_errorhandler(405)
def error_method(error):
    return jsonify({'msg': 'no', 'error': 'request method error'}), 405


@doc.app_errorhandler(408)
def time_out(error):
    return jsonify({'msg': 'no', 'error': 'time out'}), 408


@doc.app_errorhandler(500)
def internal_error(error):
    return jsonify({'msg': 'no', 'error': 'server internal error'}), 500


@doc.app_errorhandler(503)
def unavailable(error):
    return jsonify({'msg': 'no', 'error': 'service unavailable'}), 503
