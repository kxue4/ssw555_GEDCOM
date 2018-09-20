#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 15:04
# @Author  : Kaiwen Xue
# @File    : US04.py
# @Software: PyCharm
# US01 Marriage before divorce
from datetime import datetime


def marr_before_div(fam_list):

    for families in fam_list:

        if families['DIV'] != 'NONE':
            marr = datetime.strptime(families['MARR'], '%Y-%m-%d')
            div = datetime.strptime(families['DIV'], '%Y-%m-%d')

            if marr >= div:
                raise Exception('Marriage date must before divorce date!')
