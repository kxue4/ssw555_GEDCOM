#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_US15.py
# @Author: Zhiren Yang
# @Date  : 18-10-3
# @Software : PyCharm
# @Desc  :

import unittest
from UserStories.US15 import fewer_than_15_siblings


class TestFewerThan15Siblings(unittest.TestCase):

    def test_fewer_than_15_siblings(self):

        # wrong list
        f1 = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@',
              'CHIL': ['@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@', '@I1@',
                       '@I1@', '@I1@', '@I1@', '@I1@', ],
              'MARR': '1990-09-12', 'num': 82, 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/',
              'DIV': 'NONE'}]

        # correct list
        f2 = [{'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I1@', '@I2@'], 'MARR': '1959-10-16', 'num': 89,
              'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE'}]

        # 2 families, 1st has 16 children, second has 2 children
        self.assertEqual(fewer_than_15_siblings(f1), False)
        self.assertIs(fewer_than_15_siblings(f1),False)
        self.assertIs(fewer_than_15_siblings(f2),True)
        self.assertEqual(fewer_than_15_siblings(f1), False)
        self.assertTrue(fewer_than_15_siblings(f2), True)




