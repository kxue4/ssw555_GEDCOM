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
        self.assertRaises(Exception, birt_before_deat, [{'BIRT': '1990-09-12', 'DEAT': '1989-01-15'}])
        self.assertRaises(Exception, birt_before_deat, [{'BIRT': '1990-09-12', 'DEAT': '1989-01-15'}])
        self.assertRaises(Exception, birt_before_deat, [{'BIRT': '1990-09-12', 'DEAT': '1989-01-15'}])
        self.assertEqual(birt_before_deat([{'BIRT': '1990-09-12', 'DEAT': '1991-01-15'}]), None)
        self.assertEqual(birt_before_deat([{'BIRT': '1990-09-12', 'DEAT': '1991-01-15'}]), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
