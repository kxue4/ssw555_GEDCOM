#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 21:04
# @Author  : Zhe Jun
# @File    : US12.py
# @Software: PyCharm
import re


def parents_not_too_old(indi_list, fam_list):

    for fam in fam_list:

        if fam['CHIL'] != 'NONE':
            find_husb_index = int(re.sub('\D', '', str(fam['HUSB']))) - 1
            find_wife_index = int(re.sub('\D', '', str(fam['WIFE']))) - 1

            for child in fam['CHIL']:
                find_child_index = int(re.sub('\D', '', child)) - 1
                age = indi_list[find_child_index]['AGE']

                if int(indi_list[find_wife_index]['AGE']) - int(age) > 60:
                    print("ERROR: INDIVIDUAL: US12: {}: {}: mother is too old {}".format( indi_list[find_child_index]['num']+4, indi_list[find_child_index]['INDI'], indi_list[find_wife_index]['AGE']))
                    return False

                if int(indi_list[find_husb_index]['AGE']) - int(age) > 80:
                    print("ERROR: INDIVIDUAL: US12: {}: {}: mother is too old {}".format(
                        indi_list[find_child_index]['num'] + 4, indi_list[find_child_index]['INDI'],
                        indi_list[find_husb_index]['AGE']))
                    return False

    return True
