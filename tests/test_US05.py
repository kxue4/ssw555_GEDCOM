#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23
# @Author  : Zhe Jun
# @File    : test_US05.py
# @Software: PyCharm
import unittest
from UserStories.US05 import marr_before_deat


class TestMarrBeforeDeat(unittest.TestCase):

    def test_marr_before_deat(self):

        self.assertTrue(marr_before_deat([{'INDI': '@I1@', 'num': 5, 'DEAT': '1994-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1968-12-15'}]))
        self.assertTrue(marr_before_deat([{'INDI': '@I1@', 'num': 5, 'DEAT': '1994-08-15', 'SPOUSE': 'NONE'}], [{'MARR': 'NONE'}]))
        self.assertFalse(marr_before_deat([{'INDI': '@I1@', 'num': 5, 'DEAT': '1993-08-15', 'SPOUSE': ['@F1@', '@F2@']}],[{'MARR': '1999-12-15'}, {'MARR': '2000-12-15'}]))
        self.assertFalse(marr_before_deat([{'INDI': '@I1@', 'num': 5, 'DEAT': '1992-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1996-11-15'}]))
        self.assertFalse(marr_before_deat([{'INDI': '@I1@', 'num': 5, 'DEAT': '1991-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1999-1-15'}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
