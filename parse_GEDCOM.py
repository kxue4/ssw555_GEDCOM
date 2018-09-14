#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/14/18 14:44
# @Author  : Kaiwen Xue
# @File    : parse_GEDCOM.py
# @Software: PyCharm
from prettytable import PrettyTable
from datetime import datetime


def validate_gedcom(file_name):
    valid_dict = {'0': {'HEAD', 'TRLR', 'NOTE', 'INDI', 'FAM'},
                  '1': {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'},
                  '2': {'DATE'}}

    ged_file = open(file_name)
    ged = ged_file.readlines()
    ged_file.close()
    validated = []

    for lines in ged:
        lines = lines.strip()
        token = lines.split()
        token_lenth = len(token)

        if token[0] in valid_dict:

            if token_lenth == 2 and token[1] in valid_dict[token[0]]:
                level = token[0]
                tag = token[1]
                arg = ''
                validated.append((level, tag, arg))

            elif token_lenth >= 3 and token[1] in valid_dict[token[0]]:
                level = token[0]
                tag = token[1]
                arg = ' '.join(token[2:])
                validated.append((level, tag, arg))

            elif token_lenth >= 3 and token[2] in valid_dict[token[0]]:
                level = token[0]
                tag = token[2]
                arg = token[1]
                validated.append((level, tag, arg))

    return validated


def parse_gedcom(validated):
    indi_list = [] # ID, Name, Gender, Birthday, Age, Alive, Death, Child, Spouse
    indi_index = -1
    fam_list = []
    fam_index = -1
    type_of_date = 0

    for token in validated: # token = (level, tag, arg)
        level = token[0]
        tag = token[1]
        arg = token[2]

        if level == '0' and tag == 'INDI':
            indi_index += 1
            indi_list.append({})
            indi_list[indi_index][tag] = arg

        elif level == '1' and tag == 'NAME':
            indi_list[indi_index][tag] = arg

        elif level == '1' and tag == 'SEX':
            indi_list[indi_index][tag] = arg

        elif level == '1' and tag in ('BIRT', 'DEAT'):
            type_of_date = tag

        elif level == '2' and tag == 'DATE' and type_of_date != 0:
            indi_list[indi_index][type_of_date] = arg
            type_of_date = 0

    for people in indi_list:

        if 'DEAT' in people:
            people['Alive'] = 'False'
            people['Age'] = datetime.strptime(people['DEAT'], '%d %b %Y').year \
                            - datetime.strptime(people['BIRT'], '%d %b %Y').year
        else:
            people['DEAT'] = 'NA'
            people['Alive'] = 'True'
            people['Age'] = datetime.now().year - datetime.strptime(people['BIRT'], '%d %b %Y').year

    return indi_list


def pretty_table():
    pass


def main():
    a = parse_gedcom(validate_gedcom('my_test.ged'))
    print(a)

    # for i in a:
    #     if 'DEAT' in i:
    #         print(i)


if __name__ == '__main__':
    main()
