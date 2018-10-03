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
        self.assertRaises(Exception, marr_before_deat, [{'DEAT': '1992-08-15', 'SPOUSE': ['@F1@']}],
                          [{'MARR': '1999-06-15'}])
        self.assertRaises(Exception, marr_before_deat, [{'DEAT': '1999-08-1', 'SPOUSE': ['@F1@']}],
                          [{'MARR': '2003-08-20'}])
        self.assertRaises(Exception, marr_before_deat, [{'DEAT': '2010-08-25', 'SPOUSE': ['@F1@', '@F2@']}],
                          [{'MARR': '2012-08-15'}, {'MARR': '2018-08-17'}])
        self.assertEqual(marr_before_deat([{'DEAT': '1994-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1968-12-15'}]), None)
        self.assertEqual(marr_before_deat([{'DEAT': '1994-08-15', 'SPOUSE': 'NONE'}], [{'MARR': 'NONE'}]), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
