#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dispatcher import app
import msgpack
from program import Program


def byte_dict_2_string_dict(byte_dict):
    tmp = {}
    for key, value in byte_dict.items():
        if not isinstance(value, int) and value:
            value = value.decode()
        tmp.update({key.decode(): value})
    return tmp


@app.task
def judge(problem):
    a = msgpack.unpackb(problem)
    a = byte_dict_2_string_dict(a)
    rest = Program(a).run()
    return rest.to_json()
