#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30
# @Author  : Jiaxin Wang
# @File    : test_US24.py
# @Software: PyCharm
import unittest
from UserStories.US24 import Unique_fam
famlist=[{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '1990-09-12', 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE', 'num': 1},
         {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE', 'num': 2},
         {'FAM': '@F3@', 'HUSB': '@I8@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'MARR': '1986-09-10', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'DIV': 'NONE', 'num': 3},
         {'FAM': '@F4@', 'HUSB': '@I7@', 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'MARR': '1986-09-10', 'DIV': '1985-11-12', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'num': 4}]
class TestUnique_fam(unittest.TestCase):

    def test_Unique_fam(self):
        self.assertFalse(Unique_fam(famlist))
        self.assertFalse(Unique_fam(famlist))
        self.assertFalse(Unique_fam(famlist))
        self.assertFalse(Unique_fam(famlist))
        self.assertFalse(Unique_fam(famlist))

if __name__ == '__main__':

    unittest.main(exit=False, verbosity=5)

