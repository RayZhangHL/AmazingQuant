# -*- coding: utf-8 -*-

# ------------------------------
# @Time    : 2019/11/14
# @Author  : gao
# @File    : performance_test.py.py
# @Project : AmazingQuant

__author__ = "gao"

from time import *


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.secs = self.end - self.start
        self.millisecond = self.secs * 1000  # millisecond
        if self.verbose:
            print('elapsed time: %f ms' % self.millisecond)
