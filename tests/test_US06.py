#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 11:46
# @Author  : Zhe Jun
# @File    : test_US06.py.py
# @Software: PyCharm
import unittest
from US06 import div_before_deat


class TestDivBeforeDeat(unittest.TestCase):

    def test_div_before_deat(self):
        self.assertTrue(div_before_deat([{'INDI': '@I1@', 'DEAT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1968-12-15'}]))
        self.assertTrue(div_before_deat([{'INDI': '@I1@', 'DEAT': '1993-08-15', 'SPOUSE': 'NONE', 'num': 5}], [{'DIV': 'NONE'}]))
        self.assertFalse(div_before_deat([{'INDI': '@I1@', 'DEAT': '1991-01-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1999-12-15'}]))
        self.assertFalse(div_before_deat([{'INDI': '@I1@', 'DEAT': '1990-09-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1998-1-15'}]))
        self.assertFalse(div_before_deat([{'INDI': '@I1@', 'DEAT': '1992-04-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1997-2-22'}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)