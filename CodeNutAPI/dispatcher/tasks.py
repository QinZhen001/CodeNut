#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dispatcher import app


@app.task
def judge(problem):
    return problem
