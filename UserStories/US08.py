#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 12:34
# @Author  : Zhe Jun
# @File    : US08.py
# @Software: PyCharm
from datetime import datetime
import re


def birth_before_parents_marriage(indi_list, fam_list):

    for fam in fam_list:

        if fam['CHIL'] != 'NONE' and fam['MARR'] != 'NONE':
            marr = datetime.strptime(fam['MARR'], '%Y-%m-%d')

            for child in fam['CHIL']:
                find_child_index = int(re.sub('\D', '', child)) - 1
                birt = datetime.strptime(indi_list[find_child_index]['BIRT'], '%Y-%m-%d')

                if marr > birt:
                    print("ERROR: INDIVIDUAL: US08: {}: {}: Birth {} before parents marriage {}".format( indi_list[find_child_index]['num']+4, indi_list[find_child_index]['INDI'], birt, marr))
                    return False

    return True