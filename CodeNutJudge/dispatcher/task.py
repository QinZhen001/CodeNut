#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ProblemTask:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_id = kwargs.get('user_id')
        self.language = kwargs.get('language')
        self.code = kwargs.get('code')
        self.custom_input = kwargs.get('custom_input')

    def __getitem__(self, key):
        return self.__dict__[key]

    def to_json(self):
        return self.__dict__


class ResultTask:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.output = kwargs.get('output', 'N/A')
        self.status = kwargs.get('status')
        self.time_used = kwargs.get('time_used', 'N/A')
        self.memory_used = kwargs.get('memory_used', 'N/A')

    def __getitem__(self, key):
        return self.__dict__[key]

    def to_json(self):
        return self.__dict__
