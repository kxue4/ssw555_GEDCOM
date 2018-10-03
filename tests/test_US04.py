#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/20/18 15:18
# @Author  : Kaiwen Xue
# @File    : test_US04.py
# @Software: PyCharm
import unittest
from UserStories.US04 import marr_before_div


class TestMarrBeforeDiv(unittest.TestCase):

    def test_marr_before_div(self):
        self.assertRaises(Exception, marr_before_div, [{'MARR': '1990-09-12', 'DIV': '1989-01-15'}])
        self.assertRaises(Exception, marr_before_div, [{'MARR': '1990-09-12', 'DIV': '1990-09-12'}])
        self.assertRaises(ValueError, marr_before_div, [{'MARR': '1990-09-12', 'DIV': '1991-JAN-15'}])
        self.assertEqual(marr_before_div([{'MARR': '1990-09-12', 'DIV': '1991-01-15'}]), None)
        self.assertEqual(marr_before_div([{'MARR': '1990-09-12', 'DIV': 'NONE'}]), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
