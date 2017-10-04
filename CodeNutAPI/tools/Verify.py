#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def email(e):
    if re.match("[a-zA-Z0-9]+@+[a-zA-Z0-9]+\.+[a-zA-Z]", e) is not None:
        return True
    return False
