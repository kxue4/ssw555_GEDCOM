#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/19/18 15:37
# @Author  : Kaiwen Xue
# @File    : test_parse_GEDCOM.py
# @Software: PyCharm
import unittest
from parse_GEDCOM import validate_gedcom, parse_gedcom


class TestParseGedcom(unittest.TestCase):

    def test_validate_gedcom(self):
        self.assertEqual(validate_gedcom('test_parse_GEDCOM.ged'),
                         [('0', 'NOTE', 'Github repository name: ssw555_GEDCOM'), ('0', 'NOTE', 'define Kaiwen Xue'),
                          ('0', 'INDI', '@I1@'), ('1', 'NAME', 'Kaiwen /Xue/'), ('1', 'SEX', 'M'), ('1', 'BIRT', ''),
                          ('2', 'DATE', '15 AUG 1994')])

    def test_parse_gedcom(self):
        self.assertEqual(parse_gedcom([('0', 'NOTE', 'Github repository name: ssw555_GEDCOM'),
                                                                    ('0', 'NOTE', 'define Kaiwen Xue'),
                                                                    ('0', 'INDI', '@I1@'),
                                                                    ('1', 'NAME', 'Kaiwen /Xue/'),
                                                                    ('1', 'SEX', 'M'),
                                                                    ('1', 'BIRT', ''),
                                                                    ('2', 'DATE', '15 AUG 1994')]),
                                      ([{'AGE': 24, 'ALIVE': 'True', 'BIRT': '1994-08-15', 'CHIL': 'NONE', 'DEAT': 'NA',
                                         'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'SPOUSE': 'NONE'}], []))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)