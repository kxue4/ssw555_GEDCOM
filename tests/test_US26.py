#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30
# @Author  : Jiaxin Wang
# @File    : test_US24.py
# @Software: PyCharm
import unittest
from UserStories.US26 import Corresponding_entires
indilist = [{'INDI': '@I1@', 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'BIRT': '1994-08-15', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 24, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '1'},
            {'INDI': '@I2@', 'NAME': 'Mingxuan /Xue/', 'SEX': 'M', 'BIRT': '1963-11-03', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 55, 'CHIL': ['@I1@'], 'num': '2'},
            {'INDI': '@I3@', 'NAME': 'Huifang /Li/', 'SEX': 'F', 'BIRT': '1964-09-15', 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 54, 'CHIL': ['@I1@'], 'num': '3'},
            {'INDI': '@I4@', 'NAME': 'Zhishan /Xue/', 'SEX': 'M', 'BIRT': '1934-04-12', 'DEAT': '1984-08-23', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 50, 'CHIL': ['@I2@', '@I6@'], 'num': '4'},
            {'INDI': '@I5@', 'NAME': 'Xiuzhen /Mei/', 'SEX': 'F', 'BIRT': '1938-09-17', 'DEAT': '1984-08-06', 'SPOUSE': ['@F2@'], 'ALIVE': 'False', 'AGE': 46, 'CHIL': ['@I2@', '@I6@'], 'num': '5'},
            {'INDI': '@I6@', 'NAME': 'Xiumei /Xue/', 'SEX': 'F', 'BIRT': '1958-02-09', 'SPOUSE': ['@F3@', '@F4@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 60, 'CHIL': ['@I9@'], 'num': '6'},
            {'INDI': '@I7@', 'NAME': 'Zhenli /Zhang/', 'SEX': 'M', 'BIRT': '1957-10-07', 'DEAT': '1985-11-12', 'SPOUSE': ['@F4@'], 'ALIVE': 'False', 'AGE': 28, 'CHIL': ['@I9@'], 'num': '7'},
            {'INDI': '@I8@', 'NAME': 'Jianjun /Dang/', 'SEX': 'M', 'BIRT': '1952-08-08', 'SPOUSE': ['@F3@'], 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 66, 'CHIL': ['@I10@'], 'num': '8'},
            {'INDI': '@I9@', 'NAME': 'Jianguo /Zhang/', 'SEX': 'M', 'BIRT': '1984-10-11', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 34, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '9'},
            {'INDI': '@I18@', 'NAME': 'Weimin /Dang/', 'SEX': 'M', 'BIRT': '1989-04-14', 'DEAT': 'NA', 'ALIVE': 'True', 'AGE': 29, 'SPOUSE': 'NONE', 'CHIL': 'NONE', 'num': '10'}]
famlist = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'MARR': '1990-09-12', 'HUSB_NAME': 'Mingxuan /Xue/', 'WIFE_NAME': 'Huifang /Li/', 'DIV': 'NONE', 'num': '1'},
           {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE', 'num': '2'},
           {'FAM': '@F3@', 'HUSB': '@I8@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'MARR': '1986-09-10', 'HUSB_NAME': 'Jianjun /Dang/', 'WIFE_NAME': 'Xiumei /Xue/', 'DIV': 'NONE', 'num': '3'},
           {'FAM': '@F4@', 'HUSB': '@I7@', 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'MARR': '1971-08-11', 'DIV': '1985-11-12', 'HUSB_NAME': 'Zhenli /Zhang/', 'WIFE_NAME': 'Xiumei /Xue/', 'num': '4'}]

class TestCorresponding_entires(unittest.TestCase):

    def test_Corresponding_entires(self):
        self.assertFalse(Corresponding_entires (indilist, famlist))
        self.assertFalse(Corresponding_entires (indilist, famlist))
        self.assertFalse(Corresponding_entires (indilist, famlist))
        self.assertFalse(Corresponding_entires (indilist, famlist))
        self.assertFalse(Corresponding_entires (indilist, famlist))

if __name__ == '__main__':

    unittest.main(exit=False, verbosity=5)

