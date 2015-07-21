#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Usage: ./t_euler_problem.py [problem_id*]
"""
import sys
import re                       # regex
import importlib
from os import listdir
from os.path import isdir, join

target_dir = "./"


def find_and_figure_out_problem():
    for argv_index in range(1, len(sys.argv)):
        # print sys.argv[argv_index]
        problem_str = sys.argv[argv_index]
        problem_id = abs(int(problem_str))
        find_str   = problem_str
        if problem_id < 100:
            find_str = "0" + problem_str
        dir_list = [f for f in listdir(target_dir) if isdir(join(target_dir, f))]
        for dir_name in dir_list:
            pattern = re.compile(r'^' + find_str)
            match = pattern.match(dir_name)
            if match:
                print find_str
                print dir_name
                mo = importlib.import_module(dir_name + '.' + dir_name)
                # from dir_name.dir_name import exec_euler
                mo.exec_main()
        print dir_list

find_and_figure_out_problem()
