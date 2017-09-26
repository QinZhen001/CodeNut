#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint

doc = Blueprint('doc', __name__)

from . import views, errors
