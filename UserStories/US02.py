#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 17:24
# @Author  : Kaiwen Xue
# @File    : US02.py
# @Software: PyCharm
# Birth before marriage
from datetime import datetime
import re


def birt_before_marr(indi_list, fam_list):

    for people in indi_list:

        if people['SPOUSE'] != 'NONE':
            birt = datetime.strptime(people['BIRT'], '%Y-%m-%d')

            for spouses in people['SPOUSE']:
                find_fam_index = int(re.sub('\D', '', spouses)) - 1
                marr = datetime.strptime(fam_list[find_fam_index]['MARR'], '%Y-%m-%d')

                if marr <= birt:
                    raise Exception('Birth date must before marriage date')
                else:
                    print(birt, marr)