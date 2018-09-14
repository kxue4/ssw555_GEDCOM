#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/11/18 09:26
# @Author  : Kaiwen Xue
# @File    : project2-Kaiwen Xue.py
# @Software: PyCharm


sencond_place = {'NAME': '1', 'SEX': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1', 'FAMS': '1', 'MARR': '1', 'HUSB': '1',
                 'WIFE': '1', 'CHIL': '1', 'DIV': '1', 'DATE': '2', 'HEAD': '0', 'TRLR': '0', 'NOTE': '0'}
third_place = {'INDI': '0', 'FAM': '0'}
ged_file = open('my_test.ged')

for lines in ged_file:
    lines = lines.strip()
    line_list = lines.split(' ')
    line_len = len(line_list)

    if line_len == 2:

        if line_list[1] not in sencond_place.keys():
            line_list.insert(2, 'N')
        else:
            if sencond_place[line_list[1]] == line_list[0]:
                line_list.insert(2,'Y')
            else:
                line_list.insert(2,'N')

        new_line = '|'.join(line_list)

    elif line_len > 2:

        if line_list[1] not in sencond_place.keys() and line_list[2] not in third_place.keys():
            line_list.insert(2, 'N')

        elif line_list[1] in sencond_place.keys():

            if sencond_place[line_list[1]] == line_list[0]:
                line_list.insert(2, 'Y')
            else:
                line_list.insert(2, 'N')

        elif line_list[2] in third_place.keys():

            if third_place[line_list[2]] == line_list[0]:
                line_list[1],line_list[2] = line_list[2], line_list[1]
                line_list.insert(2, 'Y')
            else:
                line_list.insert(2, 'N')

        if line_len == 3:
            new_line = '|'.join(line_list)
        else:
            new_line = '|'.join(line_list[:3]) + '|' + ' '.join(line_list[3:])

    print('-->', lines)
    print('<--', new_line)
