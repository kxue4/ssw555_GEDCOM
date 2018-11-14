#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:56
# @Author  : Zhe Jun
# @File    : US10.py
# @Software: PyCharm
from datetime import datetime
import re


def marriage_after_14(indi_list, fam_list):

    for fam in fam_list:

        if fam['MARR'] != 'NONE':
            marr = datetime.strptime(fam['MARR'], '%Y-%m-%d')
            find_husb_index = int(re.sub('\D', '', str(fam['HUSB']))) - 1
            find_wife_index = int(re.sub('\D', '', str(fam['WIFE']))) - 1
            birt_husb = datetime.strptime(indi_list[find_husb_index]['BIRT'], '%Y-%m-%d')
            birt_wife = datetime.strptime(indi_list[find_wife_index]['BIRT'], '%Y-%m-%d')

            if (marr.year - birt_wife.year) < 15:
                print("ERROR: INDIVIDUAL: US10: {}: {}: marriage {} before 14 years old".format( indi_list[find_wife_index]['num']+4, indi_list[find_wife_index]['INDI'], marr))
                return False

            if (marr.year - birt_husb.year) < 15:
                print("ERROR: INDIVIDUAL: US10: {}: {}: marriage {} before 14 years old".format( indi_list[find_wife_index]['num']+4, indi_list[find_wife_index]['INDI'], marr))
                return False

    return True
