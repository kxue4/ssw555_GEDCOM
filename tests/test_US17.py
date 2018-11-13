#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_US17.py
# @Author: Zhiren Yang
# @Date  : 18-10-31
# @Software : PyCharm
# @Desc  :


import unittest
from UserStories.US17 import no_marriages_to_des


class TestNoMarriagesToDes(unittest.TestCase):

    def test_no_marriages_to_des(self):

        f = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '1990-09-12', 'num': 194,
              'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE'},
             {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '2018-10-16', 'num': 201,
              'HUSB_NAME': 'Kaiwen /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE'},
             {'FAM': '@F3@', 'HUSB': '@I8@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'MARR': '1984-09-10', 'num': 209,
              'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'DIV': 'NONE'},
             {'FAM': '@F4@', 'HUSB': '@I7@', 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'MARR': '1997-08-11',
              'DIV': '1988-11-12', 'num': 216, 'HUSB_NAME': 'Zhenli /Zhang/', 'WIFE_NAME': 'Xiumei /Xue/'},
             {'FAM': '@F5@', 'HUSB': '@I7@', 'WIFE': '@I10@',
              'CHIL': ['@I2@', '@I3@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I4@',
                       '@I5@', '@I7@', '@I24@', '@I25@', '@I26@'], 'MARR': '1997-08-11', 'DIV': '1988-11-12',
              'num': 225, 'HUSB_NAME': 'Zhenli /Zhang/', 'WIFE_NAME': 'Weimin /Dang/'}]


        self.assertEqual(no_marriages_to_des(f[0:]), False)
        self.assertEqual(no_marriages_to_des(f[1:]), False)
        self.assertEqual(no_marriages_to_des(f[2:]), False)
        self.assertEqual(no_marriages_to_des(f[3:]), False)
        self.assertEqual(no_marriages_to_des(f), False)


