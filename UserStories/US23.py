#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : US23.py
# @Software: PyCharm
# No more than one individual with the same name and birth date should appear in a GEDCOM file


def unique_name_and_birth(indi_list):
    tmp = []
    for i in indi_list:
        tmp.append(i['NAME'] + i['BIRT'])
    # print(tmp)
    if len(set(tmp)) != len(tmp):
        raise Exception('No more than one individual with the same name and birth date should appear in a GEDCOM file')
