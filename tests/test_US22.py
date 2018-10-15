#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : test_US22.py
# @Software: PyCharm

import unittest
from UserStories.US22 import unique_ids


class TestUniqueIds(unittest.TestCase):

    def test_unique_ids(self):

        self.assertEqual(unique_ids([{'INDI': '@I1@', 'num': 3}, {'INDI': '@I2@', 'num':5}],
                                    [{'FAM':'@F1@', 'num': 3}, {'FAM': '@F2@', 'num': 32}]), True)
        self.assertEqual(unique_ids([{'INDI': '@I2@', 'num': 3}, {'INDI': '@I2@', 'num': 5}],
                                    [{'FAM': '@F1@', 'num': 3}, {'FAM': '@F2@', 'num': 32}]), False)
        self.assertEqual(unique_ids([{'INDI': '@I1@', 'num': 3}, {'INDI': '@I2@', 'num': 5}],
                                    [{'FAM': '@F1@', 'num': 3}, {'FAM': '@F1@', 'num': 32}]), False)
        self.assertEqual(unique_ids([{'INDI': '@I2@', 'num': 3}, {'INDI': '@I2@', 'num': 5}],
                                    [{'FAM': '@F2@', 'num': 3}, {'FAM': '@F2@', 'num': 32}]), False)
        self.assertEqual(unique_ids([{'INDI': '@I1@', 'num': 3}, {'INDI': '@I2@', 'num': 5}],
                                    [{'FAM': '@F2@', 'num': 3}, {'FAM': '@F2@', 'num': 32}]), False)

#

if __name__ == '__main__':
    unittest.main()
