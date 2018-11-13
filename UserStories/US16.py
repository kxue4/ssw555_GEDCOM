#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 21:05
# @Author  : Zhe Jun
# @File    : US16.py
# @Software: PyCharm
import re


def male_last_names(indi_list, fam_list):

    for fam in fam_list:

        if fam['CHIL'] != 'NONE':
            find_husb_index = int(re.sub('\D', '', str(fam['HUSB']))) - 1
            father_last_name = indi_list[find_husb_index]['NAME'].split( )[1]

            for child in fam['CHIL']:
                find_child_index = int(re.sub('\D', '', child)) - 1
                child_last_name = indi_list[find_child_index]['NAME'].split( )[1]

                if indi_list[find_child_index]['SEX'] == 'M' and father_last_name != child_last_name:
                    print("ERROR: INDIVIDUAL: US16: {}: {}: {}: and {}: male last names are not same".format( indi_list[find_child_index]['num']+2, indi_list[find_child_index]['INDI'], father_last_name, child_last_name))
                    return False

    return True