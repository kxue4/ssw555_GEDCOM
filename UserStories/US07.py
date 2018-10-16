#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/18 17:24
# @Author  : Kaiwen Xue
# @File    : US07.py
# @Software: PyCharm
# US07 Less than 150 years old
from error_handler import error_handler


def less_than_150(indi_list):
    indi_id = []
    line_num = []

    for people in indi_list:

        if people['AGE'] >= 150:
            line_num.append(error_handler(people['INDI']))
            indi_id.append(people['INDI'])

    if line_num:
        print('ERROR: INDIVIDUAL: US07: lines_num:', sorted(set(line_num)), ': indi_id:', sorted(set(indi_id)),
              ': Age must less than 150 years old')
        return 'BUG'