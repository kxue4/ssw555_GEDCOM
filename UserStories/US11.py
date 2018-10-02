#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/2
# @Author  : Jiaxin Wang
# @File    : US11.py
# @Software: PyCharm
# No Bigamy
from datetime import datetime

def no_bigamy (indilist,famlist):
    marr = []
    div = []
    for people in indilist:
        print(people)
        if len(people['SPOUSE'])>=2 and people['SPOUSE']!='NONE':
            for spouse in people['SPOUSE']:
                print(spouse)
                find_fam_index = int(spouse[2])-1
                print(find_fam_index)
                if famlist[find_fam_index]['DIV'] == 'NONE':
                    tem = int((datetime.now() - datetime.strptime(famlist[find_fam_index]['MARR'], '%Y-%m-%d')).days)
                    marr.append(tem)
                    div.append(1000000)
                else :
                    tem = int((datetime.now() - datetime.strptime(famlist[find_fam_index]['MARR'], '%Y-%m-%d')).days)
                    tem2 = int((datetime.now() - datetime.strptime(famlist[find_fam_index]['DIV'],'%Y-%m-%d')).days)
                    #print(tem)
                    marr.append( tem)
                    #print(marr)
                    div.append( tem2)
                    #print(div)

    if marr[0]>div[1] or marr[1]>div[0]:
        raise Exception('biomarry')

#no_bigamy(indilist,famlist)