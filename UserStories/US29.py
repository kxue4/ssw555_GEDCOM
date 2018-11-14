#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/13/18 21:11
# @Author  : Kaiwen Xue
# @File    : US29.py
# @Software: PyCharm
# US29 List deceased


def list_deceased(indi_list):
    dead_list=[]

    for people in indi_list:

        if people['DEAT'] != 'NA':
            dead_list.append(people['INDI'])

    print('INFO: US29: All deceased people:', dead_list)