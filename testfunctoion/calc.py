#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Calc:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except "ZeroDivisionError" or "TypeError":
            return "error"

