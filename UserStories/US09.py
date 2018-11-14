#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:18
# @Author  : Zhe Jun
# @File    : US09.py
# @Software: PyCharm
from datetime import datetime
import re


def birth_before_parents_death(indi_list, fam_list):

    for fam in fam_list:

        if fam['CHIL'] != 'NONE' and fam['MARR'] != 'NONE':
            find_husb_index = int(re.sub('\D', '', str(fam['HUSB']))) - 1
            find_wife_index = int(re.sub('\D', '', str(fam['WIFE']))) - 1

            for child in fam['CHIL']:
                find_child_index = int(re.sub('\D', '', child)) - 1
                birt = datetime.strptime(indi_list[find_child_index]['BIRT'], '%Y-%m-%d')

                if indi_list[find_wife_index]['DEAT'] != 'NA' and datetime.strptime(indi_list[find_wife_index]['DEAT'], '%Y-%m-%d') < birt:
                    print("ERROR: INDIVIDUAL: US09: {}: {}: Birth {} after mother death  {}".format( indi_list[find_child_index]['num']+4, indi_list[find_child_index]['INDI'], birt, datetime.strptime(indi_list[find_wife_index]['DEAT'], '%Y-%m-%d')))
                    return False

                if indi_list[find_husb_index]['DEAT'] != 'NA' and (birt - datetime.strptime(indi_list[find_husb_index]['DEAT'], '%Y-%m-%d')).days > 180:
                    print("ERROR: INDIVIDUAL: US09: {}: {}: Birth {} after father death  {}".format( indi_list[find_child_index]['num']+4, indi_list[find_child_index]['INDI'], birt, datetime.strptime(indi_list[find_husb_index]['DEAT'], '%Y-%m-%d')))
                    return False

    return True
