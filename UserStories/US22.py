#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : US22.py
# @Software: PyCharm
# All individual IDs and family IDs should be unique

bl = True


def unique_ids(indi_list, fam_list):
    global bl
    num = 0
    indi = []
    fam = []
    tmp_indi = []
    tmp_fam = []

    line_indi_num = []
    line_fam_num = []

    line_indi_id = []
    line_fam_id = []
    for i in indi_list:
        dul_index = [x for x in range(len(indi_list)) if indi_list[x]['INDI'] == i['INDI'] and x != num]
        num += 1
        for j in dul_index:
            tmp_indi.append(j)
        indi.append(i['INDI'])
    for i in tmp_indi:
        line_indi_num.append(indi_list[i]['num'])
        line_indi_id.append(indi_list[i]['INDI'])

    # fam list
    num = 0
    for f in fam_list:
        dul_index = [x for x in range(len(fam_list)) if fam_list[x]['FAM'] == f['FAM'] and x != num]
        num += 1
        for j in dul_index:
            tmp_fam.append(j)
        fam.append(f['FAM'])
    for i in tmp_fam:
        line_fam_num.append(fam_list[i]['num'])
        line_fam_id.append(fam_list[i]['FAM'])


    if len(set(indi)) != len(indi):
        print("ERROR: INDIVIDUAL: US22: lines_num:{}: indi_id:{}: {}".format(sorted(set(line_indi_num)),sorted(set(line_indi_id)),\
            "All individual IDs should be unique"))
        bl = False
    if len(set(fam)) != len(fam):
        print("ERROR: FAMILY: US22: lines_num:{}: fam_id:{}: {}".format(sorted(set(line_fam_num)),sorted(set(line_fam_id)),\
            "All family IDs should be unique"))
        bl = False
    return bl

