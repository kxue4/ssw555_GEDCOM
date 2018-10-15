#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 17:24
# @Author  : Kaiwen Xue
# @File    : US02.py
# @Software: PyCharm
# Birth before marriage
from datetime import datetime
from error_handler import error_handler
import re


def birt_before_marr(indi_list, fam_list):
    indi_id = []
    line_num = []

    for people in indi_list:

        if people['SPOUSE'] != 'NONE':
            birt = datetime.strptime(people['BIRT'], '%Y-%m-%d')

            for spouses in people['SPOUSE']:
                find_fam_index = int(re.sub('\D', '', spouses)) - 1
                marr = datetime.strptime(fam_list[find_fam_index]['MARR'], '%Y-%m-%d')

                if marr <= birt:
                    line_num.append(error_handler(people['INDI']))
                    indi_id.append(people['INDI'])

    if line_num:
        print('ERROR: INDIVIDUAL: US02: lines_num:', sorted(set(line_num)), ': indi_id:', sorted(set(indi_id)),
              ': Birth date must before marriage date')
        return 'BUG'
