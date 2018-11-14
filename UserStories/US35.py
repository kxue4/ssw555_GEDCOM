#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/13
# @Author  : Jiaxin Wang
# @File    : US35.py
# @Software: PyCharm
# recent birth
from datetime import datetime


def recent_birth (indilist):
    for indi in indilist:
        tem = (datetime.now() - datetime.strptime(indi['BIRT'], '%Y-%m-%d')).days
        if tem<=30:
            print("INFO: US35: " + "people who were born in last 30 days are: " + str(indi['INDI'])+' '+str(indi['NAME'])+' NUM: '+str(indi['num']))
