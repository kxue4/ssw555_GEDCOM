#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/18 15:30
# @Author  : Kaiwen Xue
# @File    : error_handler.py
# @Software: PyCharm
import re


def error_handler(id):
    file = open('my_test1.ged')
    line_num = 0
    id_dict = {}

    for lines in file:
        line_num += 1
        indi_id = re.findall('@(.+?)@ INDI', lines)
        fam_id = re.findall('@(.+?)@ FAM', lines)

        if len(indi_id) != 0:
            indi_id = '@' + str(indi_id[0]) + '@'
            try:
                id_dict[indi_id].append(line_num)
            except KeyError:
                id_dict[indi_id] = [line_num]

        if len(fam_id) != 0:
            fam_id = '@' + str(fam_id[0]) + '@'
            try:
                id_dict[fam_id].append(line_num)
            except KeyError:
                id_dict[fam_id] = [line_num]

    return re.sub('[][]', '', str(id_dict[id]))