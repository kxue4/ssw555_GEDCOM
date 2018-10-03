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
        self.assertRaises(Exception, unique_ids, [{'INDI': '@I1@'}, {'INDI': '@I1@'}], [{'FAM':'@F1@'}, {'FAM': '@F2@'}])
        self.assertRaises(Exception, unique_ids, [{'INDI': '@I1@'}, {'INDI': '@I2@'}], [{'FAM':'@F1@'}, {'FAM': '@F1@'}])
        self.assertRaises(Exception, unique_ids, [{'INDI': '@I1@'}, {'FAM': '@I1@'}])
        self.assertRaises(Exception, unique_ids, [], [{'FAM':'@F1@'}, {'FAM':'@F1@'}])
        self.assertRaises(Exception, unique_ids, [{'INDI': '@I1@'}, {'INDI': '@I1@'}], [])
        self.assertEqual(unique_ids([{'INDI': '@I1@'}, {'INDI': '@I2@'}], [{'FAM':'@F1@'}, {'FAM': '@F2@'}]), None)


if __name__ == '__main__':
    unittest.main()
