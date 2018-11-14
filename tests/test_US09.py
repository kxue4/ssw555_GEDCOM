#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:41
# @Author  : Zhe Jun
# @File    : test_US09.py
# @Software: PyCharm
import unittest
from  UserStories.US09 import birth_before_parents_death


class TestBirthBeforeParentsDeath(unittest.TestCase):

    def test_birth_before_deat(self):
        self.assertTrue(birth_before_parents_death(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1995-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(birth_before_parents_death(
            [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1991-07-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-06-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(birth_before_parents_death(
            [{'INDI': '@I1@', 'BIRT': '1992-06-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1992-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1991-06-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertTrue(birth_before_parents_death(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1998-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '2000-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(birth_before_parents_death(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '2001-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1936-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
