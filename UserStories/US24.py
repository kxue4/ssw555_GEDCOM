#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30
# @Author  : Jiaxin Wang
# @File    : US24.py
# @Software: PyCharm
# Unique Families
from datetime import datetime
# famlist=[{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '1990-09-12', 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE', 'num': 1},
#          {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE', 'num': 2},
#          {'FAM': '@F3@', 'HUSB': '@I8@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'MARR': '1986-09-10', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'DIV': 'NONE', 'num': 3},
#          {'FAM': '@F4@', 'HUSB': '@I7@', 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'MARR': '1986-09-10', 'DIV': '1985-11-12', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'num': 4}]

def Unique_fam (famlist):
    marrList = []
    nameList = []
    tre =True
    for people in famlist:
        time = datetime.strptime(people['MARR'], '%Y-%m-%d')
        name = people['HUSB_NAME']
        marrList.append(time)
        nameList.append(name)
        #print(marrList)
        #print(nameList)
    # if (marr[0] > div[1]) or (marr[1] > div[0] and marr[1] < marr[0]):
    # # if (marr[0]>div[1] and marr[0]<marr[1]) or (marr[1]>div[0] and marr[1]<marr[0]):
    #     #raise Exception('biomarry')
    #     print("ERROR: FAMILY: US11: lines_num:{}: fam_id:{}: {}".format(wrongfam[0]['num'], wrongfam[0]['FAM'], \
    #                                                                          'Marriage should not occur during marriage to another spouse'))
    #     tre =False
    for i in range(len(famlist)):
        for j in range(i, len(famlist)):
            #print(i, j)
            if i != j and marrList[i] == marrList[j] and nameList[i] == nameList[j]:
                print("ERROR: FAMILY: US24: lines_num:{}: fam_id:{}: {}".format(famlist[i]['num'], famlist[i]['FAM'], \
                                                                              'No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file'))
                tre = False
    return tre

#Unique_fam (famlist)