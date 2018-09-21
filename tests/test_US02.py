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
        self.assertRaises(Exception, birt_before_marr, [{'BIRT': '1994-08-15', 'SPOUSE': '@F1@'}], [{'MARR': '1998-07-16'}])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)