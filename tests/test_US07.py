#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/18 17:50
# @Author  : Kaiwen Xue
# @File    : test_US07.py
# @Software: PyCharm
import unittest
from UserStories.US07 import less_than_150


class TestLessThan150(unittest.TestCase):

    def test_less_than_150(self):
        self.assertRaises(Exception, less_than_150, [{'INDI': '@I1@', 'AGE': 200}])
        self.assertRaises(Exception, less_than_150, [{'INDI': '@I1@', 'AGE': 150}])
        self.assertRaises(Exception, less_than_150, [{'INDI': '@I1@', 'AGE': 151}])
        self.assertEqual(less_than_150([{'INDI': '@I1@', 'AGE': 149}]), None)
        self.assertEqual(less_than_150([{'INDI': '@I1@', 'AGE': 23}]), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)