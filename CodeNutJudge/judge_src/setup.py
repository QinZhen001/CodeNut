#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import os

os.system("sudo apt-get install -y python3-dev")
os.system("sudo apt-get install -y libseccomp-dev")

setup (
	name='CodeNutJudge',
	version='1.0 beta',
	ext_modules=[Extension(name='CodeNutJudge', sources=['PythonAPI/PyAPI.c'], extra_compile_args=['-std=c99'], libraries=['seccomp'])])

