#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22
# @Author  : Zhe Jun
# @File    : US03.py
# @Software: PyCharm
# @User story: Birth before death
from datetime import datetime


def birt_before_deat(indi_list):

    for people in indi_list:

        if people['DEAT'] != 'NONE':
            birt = datetime.strptime(people['BIRT'], '%Y-%m-%d')
            deat = datetime.strptime(people['DEAT'], '%Y-%m-%d')

            if birt > deat:
                raise Exception('Birth date must before death date!')