#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest


def pytest_configure(config):
    marker_list = ["add", "div"]
    for marker in marker_list:
        config.addinivalue_line("markers", marker)
