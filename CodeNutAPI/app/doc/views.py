#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
from . import doc


@doc.route('/')
def index():
    return render_template('index.html')


@doc.route('/database/')
def database():
    return render_template('database/index.html')


@doc.route('/about/license/')
def license():
    return render_template('/about/license/index.html')


@doc.route('/about/release-notes/')
def release():
    return render_template('/about/release-notes/index.html')
