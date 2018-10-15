#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 13:18
# @Author  : Zhe Jun
# @File    : test_US08.py
# @Software: PyCharm
import unittest
from UserStories.US08 import birth_before_parents_marriage


class TestBirthBeforeParentsMarriage(unittest.TestCase):

    def test_div_before_deat(self):
        self.assertTrue(birth_before_parents_marriage([{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'MARR': '1968-12-15', 'CHIL': ['@I1@']}]))
        self.assertTrue(birth_before_parents_marriage([{'INDI': '@I1@', 'BIRT': '1993-08-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'MARR': 'NONE', 'CHIL': ['@I1@']}]))
        self.assertFalse(birth_before_parents_marriage([{'INDI': '@I1@', 'BIRT': '1991-01-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'MARR': '1999-12-15', 'CHIL': ['@I1@']}]))
        self.assertFalse(birth_before_parents_marriage([{'INDI': '@I1@', 'BIRT': '1990-09-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'MARR': '1998-1-15', 'CHIL': ['@I1@']}]))
        self.assertFalse(birth_before_parents_marriage([{'INDI': '@I1@', 'BIRT': '1992-04-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'MARR': '1997-2-22', 'CHIL': ['@I1@']}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
