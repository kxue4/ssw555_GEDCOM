#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : jiaxin wang
# @File    : US23.py
# @Software: PyCharm
# No more than one individual with the same name and birth date should appear in a GEDCOM file


def unique_name_and_birth(indi_list):
    tre= True
    tmp = []
    for i in indi_list:
        tmp.append(i['NAME'] + i['BIRT'])
    # print(tmp)
    if len(set(tmp)) != len(tmp):
        print("ERROR: INDIVIDUAL: US23: lines_num:{}: indi_id:{}: {}".format(i['num'], i['INDI'], \
                                                                             'No more than one individual with the same name and birth date should appear in a GEDCOM file'))
        tre = False
    return tre
