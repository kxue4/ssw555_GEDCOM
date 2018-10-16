#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : US14.py
# @Author: Zhiren Yang
# @Date  : 18-10-3
# @Software : PyCharm
# @Desc  : No more than five siblings should be born at the same time


from datetime import datetime

# use to get all sublists and make a comparation
def subsets(lst):
    """
    :param lst: a list
    :return: sub-list
    e.g. [1,2,3]       ->  [[], [1], [2], [3], [1,2], [1,3],[2,3], [1,2,3]]
    """
    output = [[]]
    for i in range(len(lst)):
        for j in range(len(output)):
            output.append(output[j] + [lst[i]])
    return output


def id_to_birth(indi_list, ids_list):
    """
    :param init_list:  init_list
    :param ids_list: ids_list =  ['@I2@', '@I6@', '@I3@', '@I5@']
    :return: birth_list =  ['1958-09-03', '1964-09-15', '1938-09-17', '1958-02-09']
    e.g.
           ids_list = ['@I2@', '@I6@', '@I3@', '@I5@']
        -> ['1958-09-03', '1964-09-15', '1938-09-17', '1958-02-09']
    """

    birth_list = []
    for i in indi_list:
        # birth_list.append([i['BIRT'] for j in ids_list if i['INDI'] == j])
        if i['INDI'] in ids_list:
            birth_list.append(i['BIRT'])
    return birth_list


# use to get the days between two BIRTH data.
def days(lst):
    """
    :param lst: list of birthdays, only two elements
                ['1958-09-03', '1964-09-15',
    :return: days between two dates     ->     2204 days

    """

    time = (datetime.strptime(lst[0], '%Y-%m-%d') - datetime.strptime(lst[1], '%Y-%m-%d')).days
    return abs(time)


def multiple_births_less_5(indi_list, fam_list):
    rst = True
    for f in fam_list:
        birth_days = []

        if len(f['CHIL']) > 5:
            birth_list = id_to_birth(indi_list, f['CHIL'])
            sub_birth = subsets(birth_list)
            for i in sub_birth:
                if len(i) == 2:
                    birth_days.append(days(i))
            # whether all the children are born in a same day
            assert birth_days != []
            if max(birth_days) <= 2:
                print("ERROR: FAMILY: US14: lines_num:{}: fam_id:{}: {}".format(f['num'], f['FAM'],
                      'No more than FIVE siblings should be born at the SMAE time'))
                rst = False
    return rst

