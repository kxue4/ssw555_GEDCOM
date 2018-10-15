#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22
# @Author  : Zhe Jun
# @File    : US03.py
# @Software: PyCharm
import unittest
from UserStories.US03 import birt_before_deat


class TestBirtBeforeDeat(unittest.TestCase):

    def test_birt_before_deat(self):
        self.assertTrue(birt_before_deat([{'INDI': '@I1@', 'num': 5, 'BIRT': '1990-09-12', 'DEAT': '1991-01-15'}]))
        self.assertTrue(birt_before_deat([{'INDI': '@I1@', 'num': 5, 'BIRT': '1990-06-12', 'DEAT': '1991-02-15'}]))
        self.assertFalse(birt_before_deat([{'INDI': '@I1@', 'num': 5, 'BIRT': '1998-07-12', 'DEAT': '1992-01-15'}]))
        self.assertFalse(birt_before_deat([{'INDI': '@I1@', 'num': 5, 'BIRT': '1999-02-12', 'DEAT': '1992-01-15'}]))
        self.assertFalse(birt_before_deat([{'INDI': '@I1@', 'num': 5, 'BIRT': '1994-08-12', 'DEAT': '1992-01-15'}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
