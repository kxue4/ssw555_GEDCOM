#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : US22.py
# @Software: PyCharm
# All individual IDs and family IDs should be unique


def unique_ids(indi_list, fam_list):
    tmp = []
    for i in indi_list:
        tmp.append(i['INDI'])
    for f in fam_list:
        tmp.append(f['FAM'])

    # print(tmp)
    if len(set(tmp)) != len(tmp):
        raise Exception('All individual IDs should be unique and all family IDs should be unique')

