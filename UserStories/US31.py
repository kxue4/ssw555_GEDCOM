#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US31.py
# @Author: Zhiren Yang
# @Date  : 18-10-17
# @Software : PyCharm
# @Desc  : List all living people over 30 who have never been married in a GEDCOM file


def list_living_single(indi_list):
    ls = []
    for i in indi_list:
        if i['AGE'] > 30 and i['SPOUSE'] == 'NONE':
            ls.append(i['INDI'] + '_lineNum:' + str(i['num']))
    print("INFO: " + "US31: All living people over 30 who have never been married are: " + str(ls))
