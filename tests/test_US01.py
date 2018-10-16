#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/18 17:50
# @Author  : Kaiwen Xue
# @File    : test_US01.py
# @Software: PyCharm
import unittest
from UserStories.US01 import dates_before_current


class TestDatesBeforeCurrent(unittest.TestCase):

    def test_dates_before_current(self):
        self.assertRaises(Exception, dates_before_current, [{'INDI': '@I1@', 'BIRT': '2099-10-11'}], [])
        self.assertRaises(Exception, dates_before_current, [{'INDI': '@I1@', 'DEAT': '2099-10-11'}], [])
        self.assertRaises(Exception, dates_before_current, [], [{'FAM': '@I1@', 'DIV': '2099-1-1'}])
        self.assertRaises(Exception, dates_before_current, [], [{'FAM': '@I1@', 'MARR': '2099-1-1'}])
        self.assertEqual(dates_before_current([{'INDI': '@I1@', 'BIRT': '1999-10-11', 'DEAT': 'NA'}],
                                              [{'FAM': '@F1@', 'MARR': '2015-1-1', 'DIV': 'NA'}]), None)


if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)