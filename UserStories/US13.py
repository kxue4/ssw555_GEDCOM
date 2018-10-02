#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : US23.py
# @Software: PyCharm
# No more than one individual with the same name and birth date should appear in a GEDCOM file

from datetime import datetime


def subsets(lst):
    output = [[]]
    for i in range(len(lst)):
        for j in range(len(output)):
            output.append(output[j] + [lst[i]])
    return output


def siblings_spacing(indi_list):
    tmp1 = []
    tmp2 = []

    for i in indi_list:
        tmp1.append(i['CHIL'])
    for i in tmp1:
        if (len(i) > 1 and i != 'NONE'):
            tmp2.append(i)
    for k in indi_list:
        for i in tmp2:
            for j in range(len(i)):
                if k['INDI'] == i[j]:
                    i[j] = k['BIRT']
    n = 0
    for i in range(len(tmp2)):
        a = subsets(tmp2[i])
        for j in a:
            if len(j) == 2:
                s = (datetime.strptime(j[0], '%Y-%m-%d') - datetime.strptime(j[1], '%Y-%m-%d')).days
                s = abs(s)
                # print(s)
                if s <= 305 and s >= 2:
                    n += 1
    if n != 0:
        raise Exception('No more than one individual with the same name and birth date should appear in a GEDCOM file')




# tmp1 = []
# tmp2 = []
# l = [{'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'BIRT': '1994-08-15', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 24, 'SPOUSE': 'NONE', 'CHIL': 'NONE'}, {'INDI': '@I2@', 'NAME': 'Mingxuan /Xue/', 'SEX': 'M', 'BIRT': '1963-11-03', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 55, 'CHIL': ['@I1@']}, {'INDI': '@I3@', 'NAME': 'Huifang /Li/', 'SEX': 'F', 'BIRT': '1964-09-15', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 54, 'CHIL': ['@I1@']}, {'INDI': '@I4@', 'NAME': 'Zhishan /Xue/', 'SEX': 'M', 'BIRT': '1934-04-12', 'DEAT': '1984-08-23', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 50, 'CHIL': ['@I2@', '@I6@']}, {'INDI': '@I5@', 'NAME': 'Xiuzhen /Mei/', 'SEX': 'F', 'BIRT': '1938-09-17', 'DEAT': '1984-08-06', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 46, 'CHIL': ['@I2@', '@I6@']}, {'INDI': '@I6@', 'NAME': 'Xiumei /Xue/', 'SEX': 'F', 'BIRT': '1958-02-09', 'SPOUSE': ['@F3@', '@F4@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 60, 'CHIL': ['@I9@']}, {'INDI': '@I7@', 'NAME': 'Zhenli /Zhang/', 'SEX': 'M', 'BIRT': '1957-10-07', 'DEAT': '1985-11-12', 'SPOUSE': ['@F4@'], 'ALIVE': 'False', 'AGE': 28, 'CHIL': ['@I9@']}, {'INDI': '@I8@', 'NAME': 'Jianjun /Dang/', 'SEX': 'M', 'BIRT': '1952-08-08', 'SPOUSE': ['@F3@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 66, 'CHIL': ['@I10@']}, {'INDI': '@I9@', 'NAME': 'Jianguo /Zhang/', 'SEX': 'M', 'BIRT': '1984-10-11', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 34, 'SPOUSE': 'NONE', 'CHIL': 'NONE'}, {'INDI': '@I10@', 'NAME': 'Weimin /Dang/', 'SEX': 'M', 'BIRT': '1989-04-14', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 29, 'SPOUSE': 'NONE', 'CHIL': 'NONE'}]
#
# for i in l:
#     tmp1.append(i['CHIL'])
# for i in tmp1:
#     if(len(i)>1 and i!='NONE'):
#         tmp2.append(i)
# print("tmp2 = ", tmp2)
# for k in l:
#     for i in tmp2:
#         for j in range(len(i)):
#             if k['INDI'] == i[j]:
#                 i[j] = k['BIRT']
#
#
# tmp2_now = [['1958-08-03', '1958-02-09', '1958-02-06'], ['1963-11-03', '1963-05-09']]
# n = 0
# for i in range(len(tmp2_now)):
#     a = subsets(tmp2_now[i])
#     for j in a:
#         if len(j) == 2:
#             s = (datetime.strptime(j[0], '%Y-%m-%d') - datetime.strptime(j[1], '%Y-%m-%d')).days
#             print("s = ", s)
#             if s <= 305 and s >= 2:
#                 n+=1
# print(n)