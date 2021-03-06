#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/14/18 14:44
# @Author  : Kaiwen Xue
# @File    : parse_GEDCOM.py
# @Software: PyCharm

from prettytable import PrettyTable
from datetime import datetime
import re
from UserStories import *

indi_lines = []
fam_lines = []

def validate_gedcom(file_name):
    """
    Validate the levels and tags from original GEDCOM file.
    :param validated: file_name
    :return: a validated list.  e.g.[('1', 'NAME', 'Kaiwen Xue'), ('1', 'SEX', 'M')]
    """
    valid_dict = {'0': {'HEAD', 'TRLR', 'NOTE', 'INDI', 'FAM'},
                  '1': {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'},
                  '2': {'DATE'}}

    ged_file = open(file_name)

    #
    all_lines = []
    global indi_lines
    global fam_lines
    ged = []
    for (num, value) in enumerate(ged_file):
        if 'INDI' in value:
            indi_lines.append(num+1)
        if 'FAM' in value and 'FAMC' not in value and 'FAMS' not in value:
            fam_lines.append(num+1)
        all_lines.append(num+1)
        ged.append(value)
    dic = dict(zip(all_lines, ged))
    #
    ged_file.close()

    # print(dic)
    # print(indi_lines)
    # print(fam_lines)
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
    """
    Parse validated list and return indi_list and fam_list
    :param validated: the result of validate_gedcom()
    :return: indi_list, fam_list
            e.g. indi_list = [{'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'BIRT': '15 AUG 1994', 'DEAT': 'NA',
            'ALIVE': 'True', 'AGE': 24, 'SPOUSE': 'NONE', 'CHIL': 'NONE'}, {'INDI': '@I2@', 'NAME': 'Mingxuan /Xue/',
            'SEX': 'M', 'BIRT': '3 NOV 1963', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 55, 'CHIL': ['@I1@']}]
            fam_list = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '12 SEP 1990',
            'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE'}, {'FAM': '@F2@', 'HUSB': '@I4@',
            'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '16 OCT 1959', 'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME':
            'Xiuzhen /Mei/', 'DIV': 'NONE'}]
    """
    indi_list = []
    indi_index = -1
    fam_list = []
    fam_index = -1
    indi_date_type = 'NONE'
    fam_date_type = 'NONE'
    index_indi = 0
    index_fam = 0


    for token in validated: # token = (level, tag, arg)
        level = token[0]
        tag = token[1]
        arg = token[2]

        if level == '0' and tag == 'INDI':
            indi_index += 1
            indi_list.append({})
            indi_list[indi_index][tag] = arg

        elif level == '0' and tag == 'FAM':
            fam_index += 1
            fam_list.append({})
            fam_list[fam_index][tag] = arg

        elif level == '1' and tag == 'NAME':
            indi_list[indi_index][tag] = arg

        elif level == '1' and tag == 'SEX':
            indi_list[indi_index][tag] = arg

        elif level == '1' and tag in ('BIRT', 'DEAT'):
            indi_date_type = tag

        elif level == '2' and tag == 'DATE' and indi_date_type != 'NONE':
            indi_list[indi_index][indi_date_type] = datetime.strptime(arg, '%d %b %Y').strftime('%Y-%m-%d')
            indi_date_type = 'NONE'

        elif level == '1' and tag == 'FAMS':
            indi_list[indi_index].setdefault('SPOUSE', []).append(arg)

        elif level == '1' and tag == 'HUSB':
            fam_list[fam_index][tag] = arg

        elif level == '1' and tag == 'WIFE':
            fam_list[fam_index][tag] = arg

        elif level == '1' and tag == 'CHIL':
            fam_list[fam_index].setdefault('CHIL', []).append(arg)

        elif level == '1' and tag in ('MARR', 'DIV'):
            fam_date_type = tag

        elif level == '2' and tag == 'DATE' and fam_date_type != 'NONE':
            fam_list[fam_index][fam_date_type] = datetime.strptime(arg, '%d %b %Y').strftime('%Y-%m-%d')
            fam_date_type = 'NONE'

    for people in indi_list:

        people['num'] = indi_lines[index_indi]
        index_indi +=1
        if 'DEAT' in people:
            people['ALIVE'] = 'False'
            people['AGE'] = datetime.strptime(people['DEAT'], '%Y-%m-%d').year \
                            - datetime.strptime(people['BIRT'], '%Y-%m-%d').year

        if 'DEAT' not in people:
            people['DEAT'] = 'NA'
            people['ALIVE'] = 'True'
            people['AGE'] = datetime.now().year - datetime.strptime(people['BIRT'], '%Y-%m-%d').year

        if 'SPOUSE' in people:

            for spouses in people['SPOUSE']:
                find_fam_index = int(re.sub('\D', '', spouses)) - 1
                people['CHIL'] = fam_list[find_fam_index]['CHIL']

        if 'SPOUSE' not in people:
            people['SPOUSE'] = 'NONE'
            people['CHIL'] = 'NONE'

    for families in fam_list:
        families['num'] = fam_lines[index_fam]
        index_fam += 1
        find_husb_index = int(re.sub('\D', '', families['HUSB'])) - 1
        find_wife_index = int(re.sub('\D', '', families['WIFE'])) - 1
        families['HUSB_NAME'] = indi_list[find_husb_index]['NAME']
        families['WIFE_NAME'] = indi_list[find_wife_index]['NAME']

        if 'DIV' not in families:
            families['DIV'] = 'NONE'

    return indi_list, fam_list


def pretty_table(a, b):
    indi_table = PrettyTable(field_names=["ID", "Name", "Gender", "Birthday", "Age", "Alive","Death", "Child","Spouse", "num"])
    fam_table = PrettyTable(field_names=["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID",
                                         "Wife Name", "Children", "num"])
    fam_table.align["name"] = "1"
    fam_table.padding_width = 1
    indi_table.align["name"] = "l"
    indi_table.padding_width = 1
    i = 0
    j = 0

    while i < len(a):
        each_indi = [a[i]['INDI'], a[i]['NAME'], a[i]['SEX'], a[i]['BIRT'], a[i]['AGE'], a[i]['ALIVE'], a[i]['DEAT'],
                     a[i]['CHIL'], a[i]['SPOUSE'], a[i]['num']]
        indi_table.add_row(each_indi)  # x.add_row(a[1])
        i += 1  # x.add_row(a[2])

    while j < len(b):
        each_fam = [b[j]['FAM'], b[j]['MARR'], b[j]['DIV'], b[j]['HUSB'], b[j]['HUSB_NAME'], b[j]['WIFE'],
                    b[j]['WIFE_NAME'], b[j]['CHIL'], b[j]['num']]
        fam_table.add_row(each_fam)  # x.add_row(a[1])
        j += 1  # x.add_row(a[2])

    print("Individuals")
    print(indi_table)
    print("Families")
    print(fam_table)


def main():
    result = parse_gedcom(validate_gedcom('my_test1.ged'))  # parse GEDCOM file
    pretty_table(result[0], result[1])

    # User stories part
    dates_before_current(result[0], result[1])  # US01
    birt_before_marr(result[0], result[1])  # US02
    birt_before_deat(result[0])  # US03
    marr_before_div(result[1])  # US04
    marr_before_deat(result[0], result[1])  # US05
    div_before_deat(result[0], result[1])  # US06
    less_than_150(result[0])  # US07
    birth_before_parents_marriage(result[0], result[1])  # US08
    birth_before_parents_death(result[0], result[1])  # US09
    marriage_after_14(result[0], result[1])  # US10
    no_bigamy(result[0],result[1])  # US11
    parents_not_too_old(result[0], result[1])   # US 12
    siblings_spacing(result[0])  # US13
    multiple_births_less_5(result[0], result[1])  # US14
    fewer_than_15_siblings(result[1])   # US15
    male_last_names(result[0], result[1])   # US 16
    no_marriages_to_des(result[1])  # US 17
    sibs_should_not_marry(result[1])  # US 18
    first_cousin(result[0], result[1])  # US19
    aunt_uncle(result[0],result[1])  # US20
    correct_gender_role(result[0], result[1])  # US21
    unique_ids(result[0], result[1])  # US22
    unique_name_and_birth(result[0])  # US23
    Unique_fam(result[1])  # US24
    #unique_first_name(result[0], result[1])  # US25
    Corresponding_entires(result[0], result[1])  # US26
    list_deceased(result[0])  # US29
    list_living_married(result[0])  # US 30
    list_living_single(result[0])  # US 31
    recent_birth(result[0])  # US35
    recent_death(result[0])  # US36


if __name__ == '__main__':
    main()
