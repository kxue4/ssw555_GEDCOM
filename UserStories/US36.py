#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/13
# @Author  : Jiaxin Wang
# @File    : US36.py
# @Software: PyCharm
# recent death
from datetime import datetime

def recent_death (indilist):
    for indi in indilist:
        if indi['DEAT']!='NA':
            tem = (datetime.now() - datetime.strptime(indi['DEAT'], '%Y-%m-%d')).days
            if tem<=30:
                print("INFO : " + "people who were dead in last 30 days are: " + str(indi['INDI'])+' '+str(indi['NAME'])+' NUM: '+str(indi['num']))
