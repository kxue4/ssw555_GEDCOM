#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US30.py
# @Author: Zhiren Yang
# @Date  : 18-10-17
# @Software : PyCharm
# @Desc  : List all living married people in a GEDCOM file


def list_living_married(init_list):
    lm = []
    for i in init_list:
        if i['ALIVE'] == 'True' and i['SPOUSE'] != 'NONE':
            lm.append(i['INDI'] + '_lineNum:'+ str(i['num']))
    print("INFO : " + "All living married people in a GEDCOM file are: " + str(lm))