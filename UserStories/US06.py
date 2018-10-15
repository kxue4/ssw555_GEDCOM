#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 11:37
# @Author  : Zhe Jun
# @File    : US06.py
# @Software: PyCharm
from datetime import datetime
import re


def div_before_deat(indi_list, fam_list):

    for people in indi_list:

        if people['SPOUSE'] != 'NONE' and people['DEAT'] != 'NA':
            deat = datetime.strptime(people['DEAT'], '%Y-%m-%d')

            for spouses in people['SPOUSE']:
                find_fam_index = int(re.sub('\D', '', spouses)) - 1

                if fam_list[find_fam_index]['DIV'] != 'NONE':
                    div = datetime.strptime(fam_list[find_fam_index]['DIV'], '%Y-%m-%d')

                    if div > deat:
                        print("ERROR: INDIVIDUAL: US06: {}: {}: Death {} before divorce {}".format(people['num']+6, people['INDI'], deat, div))
                        return False

    return True
