#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kombu import Queue

BROKER_URL = 'redis://localhost:6379'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TASK_RESULT_EXPIRES = 60 * 60

CELERY_TASK_SERIALIZER = 'msgpack'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_QUEUES = (
    Queue('judge', routing_key='judge.#'),
)

CELERY_ROUTES = ({
    'dispatcher.tasks.judge': {'queue': 'judge', 'routing_key': 'judge.add'},
},)

CELERY_IMPORTS = (
    'dispatcher.tasks'
)
