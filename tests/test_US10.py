#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 17:10
# @Author  : Zhe Jun
# @File    : test_US10.py
# @Software: PyCharm
import unittest
from US10 import marriage_after_14


class TestMarriageAfter14(unittest.TestCase):

    def test_marriage_after_14(self):
        self.assertTrue(marriage_after_14(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'BIRT': '1982-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'BIRT': '1981-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1998-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(marriage_after_14(
            [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'BIRT': '1991-07-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'BIRT': '1996-06-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1998-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(marriage_after_14(
            [{'INDI': '@I1@', 'BIRT': '1992-06-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'BIRT': '1981-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'BIRT': '1991-06-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1998-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertTrue(marriage_after_14(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'BIRT': '1980-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'BIRT': '1971-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1998-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(marriage_after_14(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'BIRT': '1997-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'BIRT': '1936-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1998-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)