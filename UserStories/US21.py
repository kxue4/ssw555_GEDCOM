#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30/18 20:49
# @Author  : Kaiwen Xue
# @File    : US21.py
# @Software: PyCharm
import re
from error_handler import error_handler


def correct_gender_role(indi_list, fam_list):
    line_num = []
    id_list = []

    for families in fam_list:
        husb_id = families['HUSB']
        wife_id = families['WIFE']

        for people in indi_list:

            if people['INDI'] == husb_id and people['SEX'] != 'M':
                line_num.append(error_handler(families['HUSB']))
                id_list.append(husb_id)

            if people['INDI'] == wife_id and people['SEX'] != 'F':
                line_num.append(error_handler(families['WIFE']))
                id_list.append(wife_id)

    if line_num:
        print('ERROR: INDIVIDUAL: US21: lines_num:', sorted(set(line_num)), ': indi_id:', sorted(set(id_list)),
              ': Gender and role are not correct!')