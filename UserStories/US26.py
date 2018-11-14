#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30
# @Author  : Jiaxin Wang
# @File    : US26.py
# @Software: PyCharm
# Corresponding entries
indilist = [{'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'BIRT': '1994-08-15', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 24, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '1'},
            {'INDI': '@I2@', 'NAME': 'Mingxuan /Xue/', 'SEX': 'M', 'BIRT': '1963-11-03', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 55, 'CHIL': ['@I1@'], 'num': '2'},
            {'INDI': '@I3@', 'NAME': 'Huifang /Li/', 'SEX': 'F', 'BIRT': '1964-09-15', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 54, 'CHIL': ['@I1@'], 'num': '3'},
            {'INDI': '@I4@', 'NAME': 'Zhishan /Xue/', 'SEX': 'M', 'BIRT': '1934-04-12', 'DEAT': '1984-08-23', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 50, 'CHIL': ['@I2@', '@I6@'], 'num': '4'},
            {'INDI': '@I5@', 'NAME': 'Xiuzhen /Mei/', 'SEX': 'F', 'BIRT': '1938-09-17', 'DEAT': '1984-08-06', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 46, 'CHIL': ['@I2@', '@I6@'], 'num': '5'},
            {'INDI': '@I6@', 'NAME': 'Xiumei /Xue/', 'SEX': 'F', 'BIRT': '1958-02-09', 'SPOUSE': ['@F3@', '@F4@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 60, 'CHIL': ['@I9@'], 'num': '6'},
            {'INDI': '@I7@', 'NAME': 'Zhenli /Zhang/', 'SEX': 'M', 'BIRT': '1957-10-07', 'DEAT': '1985-11-12', 'SPOUSE': ['@F4@'], 'ALIVE': 'False', 'AGE': 28, 'CHIL': ['@I9@'], 'num': '7'},
            {'INDI': '@I8@', 'NAME': 'Jianjun /Dang/', 'SEX': 'M', 'BIRT': '1952-08-08', 'SPOUSE': ['@F3@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 66, 'CHIL': ['@I10@'], 'num': '8'},
            {'INDI': '@I9@', 'NAME': 'Jianguo /Zhang/', 'SEX': 'M', 'BIRT': '1984-10-11', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 34, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '9'},
            {'INDI': '@I18@', 'NAME': 'Weimin /Dang/', 'SEX': 'M', 'BIRT': '1989-04-14', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 29, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '10'}]
famlist = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '1990-09-12', 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE', 'num': '1'},
           {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE', 'num': '2'},
           {'FAM': '@F3@', 'HUSB': '@I8@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'MARR': '1986-09-10', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'DIV': 'NONE', 'num': '3'},
           {'FAM': '@F4@', 'HUSB': '@I7@', 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'MARR': '1971-08-11', 'DIV': '1985-11-12', 'HUSB_NAME': 'Zhenli /Zhang/', 'WIFE_NAME': 'Xiumei /Xue/', 'num': '4'}]

def Corresponding_entires (indilist, famlist):
    i = 0
    tre =True
    famL = []
    indiL = []
    for fam in famlist:
        famL.append(fam['HUSB'])
        famL.append(fam['WIFE'])
        for chil in fam['CHIL']:
            famL.append(chil)
    for indi in indilist:
        if indi['INDI'] in famL:
            i+=1
        else:
            print("ERROR: INDIVIDUAL: US26: lines_num:{}: indi_id:{}: {}".format(indi['num'], indi['INDI'], \
             'All individual roles (spouse, child) specified in family records should have corresponding entries in the corresponding  individuals records'))
            #print(famL)

    for indi in indilist:
        indiL.append(indi['INDI'])
    #print(indiL)

    for fam in famlist:
        if fam['HUSB'] in indiL or fam['WIFE'] in indiL:
            for chil in fam['CHIL']:
                if chil in indiL:
                    i += 1
                else:
                    tre = False
                    print("ERROR: FAMILY: US26: lines_num:{}: fam_id:{}: {}".format(fam['num'], fam['FAM'], \
                    'All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family records.'))
        else:
            for chil in fam['CHIL']:
                if chil in indiL:
                    i += 1
                else:
                    tre = False
                    print("ERROR: FAMILY: US26: lines_num:{}: fam_id:{}: {}".format(fam['num'], fam['FAM'], \
                    'All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family records.'))
   
    return tre

Corresponding_entires(indilist,famlist)