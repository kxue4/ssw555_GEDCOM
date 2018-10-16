#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US15.py
# @Author: Zhiren Yang
# @Date  : 18-10-3
# @Software : PyCharm
# @Desc  : There should be fewer than 15 siblings in a family


def fewer_than_15_siblings(fam_list):
    tmp = []
    rst = True
    for i in fam_list:
        tmp.append(i['CHIL'] + [i['FAM']] + [i['num']])
    # print(tmp)
    for j in tmp:
        if len(j) > 15 + 2:
            print("ERROR: FAMILY: US15: lines_num:{}: fam_id:{}: {}".format(j[-1],j[-2],
                'There should be fewer than 15 siblings in a family'))
            rst = False
    return rst




# l = [{'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'BIRT': '1994-08-15', 'num': 3, 'DEAT': 'NA', 'ALIVE': 'True',
#       'AGE': 24, 'SPOUSE': 'NONE', 'CHIL': 'NONE'},
#      {'INDI': '@I2@', 'NAME': 'Mingxuan /Xue/', 'SEX': 'M', 'BIRT': '1958-09-03', 'SPOUSE': ['@F1@'], 'num': 10,
#       'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 60, 'CHIL': ['@I1@']},
#      ]
#
# f = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@',
#       'CHIL': ['@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', ],
#       'MARR': '1990-09-12', 'num': 82, 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE'},
#      {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I1@', '@I2@'], 'MARR': '1959-10-16', 'num': 89,
#       'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE'}]
# fewer_than_15_siblings(f)