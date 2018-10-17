#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US19.py
# @Author: Jiaxin Wang
# @Date  : 18-10-15
# @Software : PyCharm
# @Desc  : First cousins should not marry one another
# indilist = [{'INDI': '@I1@',  'SPOUSE': 'NONE',   'num': 3,   'CHIL': 'NONE'},
#             {'INDI': '@I2@',  'SPOUSE': ['@F1@'], 'num': 10,  'CHIL': ['@I1@']},
#             {'INDI': '@I1@',  'SPOUSE': ['@F1@'], 'num': 18,  'CHIL': ['@I1@']},
#             {'INDI': '@I3@',  'SPOUSE': ['@F2@'], 'num': 25,  'CHIL': ['@I2@', '@I6@']},
#             {'INDI': '@I5@',  'SPOUSE': ['@F2@'], 'num': 34,  'CHIL': ['@I2@', '@I6@']},
#             {'INDI': '@I6@',  'SPOUSE': ['@F3@', '@F4@'], 'num': 43, 'CHIL': ['@I9@']},
#             {'INDI': '@I7@',  'SPOUSE': ['@F4@'], 'num': 52,  'CHIL': ['@I9@']},
#             {'INDI': '@I8@',  'SPOUSE': ['@F3@'], 'num': 61,  'CHIL': ['@I10@']},
#             {'INDI': '@I9@',  'SPOUSE': 'NONE',   'num': 68,  'CHIL': 'NONE'},
#             {'INDI': '@I10@', 'SPOUSE': 'NONE',   'num': 75,  'CHIL': 'NONE'},
#             {'INDI': '@I11@', 'SPOUSE': 'NONE',   'num': 82,  'CHIL': 'NONE'},
#             {'INDI': '@I12@', 'SPOUSE': 'NONE',   'num': 89,  'CHIL': 'NONE'},
#             {'INDI': '@I13@', 'SPOUSE': 'NONE',   'num': 96,  'CHIL': 'NONE'},
#             {'INDI': '@I14@', 'SPOUSE': 'NONE',   'num': 103, 'CHIL': 'NONE'},
#             {'INDI': '@I14@', 'SPOUSE': 'NONE',   'num': 110, 'CHIL': 'NONE'},
#             {'INDI': '@I16@', 'SPOUSE': 'NONE',   'num': 117, 'CHIL': 'NONE'},
#             {'INDI': '@I17@', 'SPOUSE': 'NONE',   'num': 124, 'CHIL': 'NONE'},
#             {'INDI': '@I18@', 'SPOUSE': 'NONE',   'num': 131, 'CHIL': 'NONE'},
#             {'INDI': '@I19@', 'SPOUSE': 'NONE',   'num': 138, 'CHIL': 'NONE'},
#             {'INDI': '@I20@', 'SPOUSE': 'NONE',   'num': 145, 'CHIL': 'NONE'},
#             {'INDI': '@I21@', 'SPOUSE': 'NONE',   'num': 152, 'CHIL': 'NONE'},
#             {'INDI': '@I22@', 'SPOUSE': 'NONE',   'num': 159, 'CHIL': 'NONE'},
#             {'INDI': '@I23@', 'SPOUSE': 'NONE',   'num': 166, 'CHIL': 'NONE'},
#             {'INDI': '@I24@', 'SPOUSE': 'NONE',   'num': 173, 'CHIL': 'NONE'},
#             {'INDI': '@I25@', 'SPOUSE': 'NONE',   'num': 180, 'CHIL': 'NONE'},
#             {'INDI': '@I26@', 'SPOUSE': 'NONE',   'num': 187, 'CHIL': 'NONE'}]
#
# famlist = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'num': 194},
#            {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'num': 201},
#            {'FAM': '@F3@', 'HUSB': '@I1@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'num': 209},
#            {'FAM': '@F4@', 'HUSB': '@I2@', 'WIFE': '@I9@', 'CHIL': ['@I9@'], 'num': 216},
#            {'FAM': '@F5@', 'HUSB': '@I1@', 'WIFE': '@I9@', 'CHIL': ['@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@'], 'num': 225}]

cousin = []
wronglist = []


def first_cousin(indilist, famlist):
    tre = True
    #print(indilist)
    for fam in famlist:
        if len(fam['CHIL']) >= 2 and fam['CHIL'] != 'NONE':
            for chil in fam['CHIL']:
                find_people_index = int(chil[2])-1
                if indilist[find_people_index]['CHIL'] != 'NONE':
                    tem = indilist[find_people_index]['CHIL']
                    #print(indilist[find_people_index])
                    #print(tem)
                    tmp=tem[0]
                    #print(tmp)
                    cousin.append(tmp)
                    #print(cousin)


    for fam in famlist:
        #print(fam)
        for i in range(len(cousin)):
            #print('in')
            #print(i)
            for j in range(len(cousin)):
                #print('jn')
                #print(j)
                #print(fam['HUSB'])
                #print(len(cousin[i]))
                if fam['HUSB'] == cousin[i] and fam['WIFE'] == cousin[j]:
                    wronglist.append(fam)
                    #print("ERROR: FAMILY: US19: lines_num:{}: fam_id:{}: {}".format(fam['num'], fam['FAM'],'First cousins should not marry one another'))
    #print(wronglist)
    del_wronglist(wronglist)
    #print(len(wronglist))
    #print(wronglist)
    for q in range(len(wronglist)):
        print("ERROR: FAMILY: US19: lines_num:{}: fam_id:{}: {}".format(wronglist[q]['num'], wronglist[q]['FAM'],
                                                                    'First cousins should not marry one another'))
        tre = False
    return tre

def del_wronglist(wronglist):
    counter = 1
    while counter < len(wronglist):
        if wronglist[counter-1]['FAM'] == wronglist[counter]['FAM']:
            del wronglist[counter-1]
        else:
            counter = counter +1


# first_cousin(indilist,famlist)
#print(cousin)
