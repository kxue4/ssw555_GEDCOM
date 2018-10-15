#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 17:42
# @Author  : Kaiwen Xue
# @File    : test_US02.py
# @Software: PyCharm
import unittest
from UserStories.US02 import birt_before_marr


class TestBirtBeforeMarr(unittest.TestCase):

    def test_birt_before_marr(self):
        self.assertRaises(FileNotFoundError, birt_before_marr, [{'INDI':'@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@']}],
                          [{'MARR': '1993-08-15'}])
        self.assertRaises(FileNotFoundError, birt_before_marr, [{'INDI':'@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@']}],
                          [{'MARR': '1994-08-15'}])
        self.assertRaises(FileNotFoundError, birt_before_marr, [{'INDI':'@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@', '@F2@']}],
                          [{'MARR': '2014-08-15'}, {'MARR': '1993-09-17'}])
        self.assertEqual(birt_before_marr([{'INDI':'@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@']}],
                          [{'MARR': '2014-08-15'}]), None)
        self.assertEqual(birt_before_marr([{'INDI':'@I1@', 'BIRT': '1994-08-15', 'SPOUSE': 'NONE'}],
                          [{'MARR': '2014-08-15'}]), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)