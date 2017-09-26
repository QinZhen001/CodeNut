#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
from . import doc


@doc.app_errorhandler(400)
def error_request(error):
    return render_template('error.html', error='error request', status=400)


@doc.app_errorhandler(403)
def forbidden(error):
    return render_template('error.html', error='forbidden', status=403)


@doc.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error='not found', status=404)


@doc.app_errorhandler(405)
def error_method(error):
    return render_template('error.html', error='request method error', status=405)


@doc.app_errorhandler(408)
def time_out(error):
    return render_template('error.html', error='time out', status=408)


@doc.app_errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='server internal error', status=500)


@doc.app_errorhandler(503)
def unavailable(error):
    return render_template('error.html', error='service unavailable', status=503)
