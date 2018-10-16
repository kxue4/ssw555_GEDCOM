#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 15:04
# @Author  : Kaiwen Xue
# @File    : US04.py
# @Software: PyCharm
# US04 Marriage before divorce
from datetime import datetime
from error_handler import error_handler


def marr_before_div(fam_list):
    line_num = []
    fam_id = []

    for families in fam_list:

        if families['DIV'] != 'NONE':
            marr = datetime.strptime(families['MARR'], '%Y-%m-%d')
            div = datetime.strptime(families['DIV'], '%Y-%m-%d')

            if marr >= div:
                line_num.append(error_handler(families['FAM']))
                fam_id.append(families['FAM'])

    if line_num:
        print('ERROR: FAMILY: US04: lines_num:', sorted(set(line_num)), ': fam_id:', sorted(set(fam_id)),
              ': Marriage date must before divorce date!')
