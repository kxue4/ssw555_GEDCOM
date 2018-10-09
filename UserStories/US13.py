#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : US23.py
# @Software: PyCharm
# Birth dates of siblings should be more than 8 months apart or less than 2 days apart

from datetime import datetime


# use to get all sublists and make a comparation
def subsets(lst):
    output = [[]]
    for i in range(len(lst)):
        for j in range(len(output)):
            output.append(output[j] + [lst[i]])
    return output


def siblings_spacing(indi_list):
    rst = True
    all_children = []
    two_child_fams = []
    error_birth = []
    line_indi_num = []
    line_indi_id = []
    for i in indi_list:
        all_children.append(i['CHIL'])

    for i in all_children:
        if len(i) > 1 and i != 'NONE':
            two_child_fams.append(i)
    # print("two_child_fams:",two_child_fams)
    for k in indi_list:
        for i in two_child_fams:
            for j in range(len(i)):
                if k['INDI'] == i[j]:
                    i[j] = k['BIRT']

    err_num = 0
    for i in range(len(two_child_fams)):
        # print("birthday", two_child_fams[i])
        sublist = subsets(two_child_fams[i])
        # print("sublist ", sublist)
        for j in sublist:
            # print("j =",j)
            if len(j) == 2:
                birth_days = (datetime.strptime(j[0], '%Y-%m-%d') - datetime.strptime(j[1], '%Y-%m-%d')).days
                birth_days = abs(birth_days)
                if 2 <= birth_days <= 305:
                    err_num += 1
                    error_birth.append(j[0])
                    error_birth.append(j[1])
    error_birth = (list(set(error_birth)))
    # print(error_birth)
    for i in indi_list:
        for j in error_birth:
            if j == i['BIRT']:
                line_indi_id.append(i['INDI'])
                line_indi_num.append(i['num'])
    # print("line_indi_id=",line_indi_id, "\nline_indi_num=",line_indi_num)
    if err_num != 0:
        print("ERROR: INDIVIDUAL: US13: lines_num:{}: indi_id:{}: {}".format(line_indi_num,line_indi_id,\
            'Birth dates of siblings should be more than 8 months apart or less than 2 days apart'))
