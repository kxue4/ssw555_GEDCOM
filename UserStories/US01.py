#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/18 17:24
# @Author  : Kaiwen Xue
# @File    : US01.py
# @Software: PyCharm
# US01 Dates before current date
from datetime import datetime, timedelta
from error_handler import error_handler


def dates_before_current(indi_list, fam_list):
    line_num = []
    id_list = []
    current = datetime.now()

    for people in indi_list:
        birt = datetime.strptime(people['BIRT'], '%Y-%m-%d')

        try:
            deat = datetime.strptime(people['DEAT'], '%Y-%m-%d')
        except ValueError:
            deat = datetime.now() - timedelta(1)

        if birt >= current or deat >= current:
            line_num.append(error_handler(people['INDI']))
            id_list.append(people['INDI'])

    for families in fam_list:
        marr = datetime.strptime(families['MARR'], '%Y-%m-%d')

        try:
            div = datetime.strptime(families['DIV'], '%Y-%m-%d')
        except ValueError:
            div = datetime.now() - timedelta(1)

        if marr >= current or div >= current:
            line_num.append(error_handler(families['FAM']))
            id_list.append(families['FAM'])

    if line_num:
        print('ERROR: INDIVIDUAL: US01: lines_num:', sorted(set(line_num)), ': indi_id:', sorted(set(id_list)),
              ': Dates must before current date!')
