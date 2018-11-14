#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US18.py
# @Author: Zhiren Yang
# @Date  : 18-10-30
# @Software : PyCharm
# @Desc  : Siblings should not marry one another
# Siblings should not marry


def list_flatten(lst):
    child = []
    for i in lst:
        for j in range(len(i)):
            child.append(i[j])
    return child


def sibs_should_not_marry(fam_list):
    rst = True
    child_list = []
    for i in fam_list:
        child_list.append(i['CHIL'])
        # child_list = [y for x in child_list for y in x]
    child_list = list_flatten(child_list)

    for j in fam_list:
        # print(j['HUSB'], j['WIFE'])
        if j['HUSB'] in child_list and j['WIFE'] in child_list:
            print("ERROR: FAMILY: US18: {}: {}: {}".format(j['num'], j['FAM'],
                'Siblings should not marry one another'))
            rst = False

    return rst
