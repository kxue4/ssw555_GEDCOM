#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 23:50
# @Author  : Zhe Jun
# @File    : test_US12.py
# @Software: PyCharm
import unittest
from UserStories.US12 import parents_not_too_old


class TestParentsNotTooOld(unittest.TestCase):

    def test_parents_not_too_old(self):
        self.assertTrue(parents_not_too_old(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1995-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-08-15', 'AGE': '40', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(parents_not_too_old(
            [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1991-07-15', 'AGE': '1000', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-06-15', 'AGE': '60', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(parents_not_too_old(
            [{'INDI': '@I1@', 'BIRT': '1992-06-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1992-08-15', 'AGE': '30', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1991-06-15', 'AGE': '200', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertTrue(parents_not_too_old(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1998-08-15', 'AGE': '50','SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '2000-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(parents_not_too_old(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '2001-08-15', 'AGE': '209', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1936-08-15', 'AGE': '30','SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
