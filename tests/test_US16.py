#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 1:43
# @Author  : Zhe Jun
# @File    : test_US16.py
# @Software: PyCharm
import unittest
from UserStories.US16 import male_last_names


class TestMaleLastNAme(unittest.TestCase):

    def test_Male_Last_Name(self):
        self.assertTrue(male_last_names(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SEX': 'M', 'NAME': 'Xin Yang', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1995-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-08-15', 'SEX': 'M', 'NAME': 'Shi Yang', 'AGE': '40', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(male_last_names(
            [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'SEX': 'M', 'NAME': 'Xin Yang','AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1991-07-15', 'AGE': '1000', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-06-15', 'SEX': 'M', 'NAME': 'Xin Sang','AGE': '60', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(male_last_names(
            [{'INDI': '@I1@', 'BIRT': '1992-06-15', 'SEX': 'M', 'NAME': 'Xin Yang','AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1992-08-15', 'AGE': '30', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1991-06-15', 'SEX': 'M', 'NAME': 'Xin Shu','AGE': '200', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertTrue(male_last_names(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SEX': 'M', 'NAME': 'Xin Yang', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1998-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '2000-08-15', 'AGE': '50', 'SEX': 'M', 'NAME': 'Luo Yang', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(male_last_names(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SEX': 'M', 'NAME': 'Xin Yang','SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '2001-08-15', 'AGE': '209', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1936-08-15', 'AGE': '30', 'SEX': 'M', 'NAME': 'Xin Ing','SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
