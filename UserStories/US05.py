#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23
# @Author  : Zhe Jun
# @File    : US05.py
# @Software: PyCharm
# @User story: Marriage before death
from datetime import datetime
import re


def marr_before_deat(indi_list, fam_list):

    for people in indi_list:

        if people['SPOUSE'] != 'NONE' and people['DEAT'] != 'NONE':
            deat = datetime.strptime(people['DEAT'], '%Y-%m-%d')

            for spouses in people['SPOUSE']:
                find_fam_index = int(re.sub('\D', '', spouses)) - 1
                marr = datetime.strptime(fam_list[find_fam_index]['MARR'], '%Y-%m-%d')

                if marr > deat:
                    raise Exception(' Marriage date must before death date')