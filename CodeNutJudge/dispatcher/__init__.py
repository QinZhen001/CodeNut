#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('judge')
app.config_from_object('dispatcher.celery_conf')
