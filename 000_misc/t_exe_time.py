#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
wrapper for print program execute time.
"""

def exec_time(func):
    import time
    def new_func(*args, **kwargs):
        begin = time.time()
        back = func(*args, **kwargs)
        print "%.3fs taken for [%s]" % (time.time() - begin, func.__name__)
        return back
    return new_func

