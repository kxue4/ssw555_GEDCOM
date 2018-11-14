#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US17.py
# @Author: Zhiren Yang
# @Date  : 18-10-30
# @Software : PyCharm
# @Desc  : Parents should not marry any of their descendants
# No marriages to descendants


def list_flatten(lst):
    child = []
    for i in lst:
        for j in range(len(i)):
            child.append(i[j])
    return child


def no_marriages_to_des(fam_list):

    rst = True
    for i in fam_list:
        # print(i['CHIL'])
        if i['HUSB'] in i['CHIL'] or i['WIFE'] in i['CHIL']:
            print("ERROR: FAMILY: US17: {}: {}: {}".format(i['num'], i['FAM'],
                    'Parents should not marry any of their descendants or parents'))
            rst = False

    return rst
