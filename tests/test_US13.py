#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : test_US23.py
# @Software: PyCharm

import unittest
from UserStories.US13 import siblings_spacing


class TestSiblingsSpacing(unittest.TestCase):

    def test_siblings_spacing(self):
        # in 10 months(3 children)
        self.assertRaises(Exception, siblings_spacing,
                          [{'INDI': '@I2@', 'BIRT': '1965-11-03', 'CHIL': ['@I1@']},
                           {'INDI': '@I3@', 'BIRT': '1963-09-15', 'CHIL': ['@I6@']},
                           {'INDI': '@I5@', 'BIRT': '1963-09-12', 'CHIL': 'NONE'},
                           {'INDI': '@I4@', 'BIRT': '1934-04-12', 'CHIL': ['@I2@', '@I3@', '@I5@']}
                           ])
        # in 10 months
        self.assertRaises(Exception, siblings_spacing,
                          [{'INDI': '@I2@', 'BIRT': '1963-11-03', 'CHIL': ['@I1@']},
                           {'INDI': '@I3@', 'BIRT': '1963-09-15', 'CHIL': ['@I6@']},
                           {'INDI': '@I4@', 'BIRT': '1934-04-12', 'CHIL': ['@I2@', '@I3@']}
                           ])
        # bigger than 2 days
        self.assertRaises(Exception, siblings_spacing,
                          [{'INDI': '@I2@', 'BIRT': '1965-11-03', 'CHIL': ['@I1@']},
                           {'INDI': '@I3@', 'BIRT': '1965-11-06', 'CHIL': ['@I6@']},
                           {'INDI': '@I4@', 'BIRT': '1934-04-12', 'CHIL': ['@I2@', '@I3@']}
                           ])

        # true -> birth with in 1 day
        self.assertEqual(siblings_spacing(
                          [{'INDI': '@I2@', 'BIRT': '1965-11-03', 'CHIL': ['@I1@']},
                           {'INDI': '@I3@', 'BIRT': '1965-11-02', 'CHIL': ['@I6@']},
                           {'INDI': '@I4@', 'BIRT': '1934-04-12', 'CHIL': ['@I2@', '@I3@']}
                           ]), None)
        # true -> birth date bigger than 10 months
        self.assertEqual(siblings_spacing(
                            [{'INDI': '@I2@', 'BIRT': '1963-11-03', 'CHIL': ['@I1@']},
                             {'INDI': '@I3@', 'BIRT': '1965-11-02', 'CHIL': ['@I6@']},
                             {'INDI': '@I4@', 'BIRT': '1934-04-12', 'CHIL': ['@I2@', '@I3@']}
                             ]), None)


if __name__ == '__main__':
    unittest.main()
