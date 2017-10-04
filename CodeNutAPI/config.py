#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 'the quick brown fox jumps over the lazy dog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:root@127.0.0.1:3306/codenut?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'mysql+pymysql://root:root@127.0.0.1:3306/testcodenut?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:root@127.0.0.1:3306/codenut?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
