#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_US14.py
# @Author: Zhiren Yang
# @Date  : 18-10-13
# @Software : PyCharm
# @Desc  : test -- No more than five siblings should be born at the same time


import unittest
from UserStories.US14 import multiple_births_less_5


class TestMultipleBirthsLess5(unittest.TestCase):

    def test_multiple_births_less_5(self):

        """
        l1 is the individual list
        f1 is the family list which can raise the Exception(return False)
        f1[3:] is a part of list f1 which can not raise the Exception(return True)
        """

        l1 = [{'num': 3, 'CHIL': 'NONE', 'AGE': 24, 'NAME': 'Kaiwen /Xue/', 'SEX': 'M', 'ALIVE': 'True', 'DEAT': 'NA',
              'INDI': '@I1@', 'SPOUSE': 'NONE', 'BIRT': '1994-08-15'},
             {'num': 10, 'CHIL': ['@I1@'], 'DEAT': 'NA', 'AGE': 60, 'NAME': 'Mingxuan /Xue/', 'SEX': 'M', 'ALIVE': 'True',
              'SPOUSE': ['@F1@'], 'INDI': '@I2@', 'BIRT': '1994-08-15'},
             {'num': 18, 'CHIL': ['@I1@'], 'DEAT': 'NA', 'AGE': 54, 'NAME': 'Huifang /Li/', 'SEX': 'F', 'ALIVE': 'True',
              'SPOUSE': ['@F1@'], 'INDI': '@I3@', 'BIRT': '1964-09-15'},
             {'num': 25, 'CHIL': ['@I2@', '@I6@'], 'AGE': 50, 'DEAT': '1984-08-23', 'SEX': 'M', 'ALIVE': 'False',
              'SPOUSE': ['@F2@'], 'BIRT': '1934-04-12', 'INDI': '@I4@', 'NAME': 'Zhishan /Xue/'},
             {'num': 34, 'CHIL': ['@I2@', '@I6@'], 'AGE': 46, 'DEAT': '1984-08-06', 'SEX': 'F', 'ALIVE': 'False',
              'SPOUSE': ['@F2@'], 'BIRT': '1938-09-17', 'INDI': '@I5@', 'NAME': 'Xiuzhen /Mei/'},
             {'num': 43, 'CHIL': ['@I9@'], 'DEAT': 'NA', 'AGE': 60, 'NAME': 'Xiumei /Xue/', 'SEX': 'F', 'ALIVE': 'True',
              'SPOUSE': ['@F3@', '@F4@'], 'INDI': '@I6@', 'BIRT': '1994-08-15'},
             {'num': 52, 'CHIL': ['@I9@'], 'AGE': 28, 'DEAT': '1985-11-12', 'SEX': 'M', 'ALIVE': 'False', 'SPOUSE': ['@F4@'],
              'BIRT': '1957-10-07', 'INDI': '@I7@', 'NAME': 'Zhenli /Zhang/'},
             {'num': 61, 'CHIL': ['@I10@'], 'DEAT': 'NA', 'AGE': 66, 'NAME': 'Jianjun /Dang/', 'SEX': 'M', 'ALIVE': 'True',
              'SPOUSE': ['@F3@'], 'INDI': '@I8@', 'BIRT': '1994-08-15'},
             {'num': 68, 'CHIL': 'NONE', 'AGE': 34, 'NAME': 'Jianguo /Zhang/', 'SEX': 'M', 'ALIVE': 'True', 'DEAT': 'NA',
              'INDI': '@I9@', 'SPOUSE': 'NONE', 'BIRT': '1994-08-15'},
             {'num': 75, 'CHIL': 'NONE', 'AGE': 29, 'NAME': 'Weimin /Dang/', 'SEX': 'M', 'ALIVE': 'True', 'DEAT': 'NA',
              'INDI': '@I10@', 'SPOUSE': 'NONE', 'BIRT': '1994-08-15'}]

        f1 = [{'num': 82, 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'HUSB': '@I2@', 'FAM': '@F1@', 'WIFE_NAME': 'Huifang /Li/',
              'DIV': 'NONE', 'MARR': '1990-09-12', 'HUSB_NAME': 'Mingxuan /Xue/'},
             {'num': 89, 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@', '@I9@','@I8@','@I10@', '@I1@'], 'HUSB': '@I4@', 'FAM': '@F2@', 'WIFE_NAME': 'Xiuzhen /Mei/',
              'DIV': 'NONE', 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/'},
             {'num': 97, 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'HUSB': '@I8@', 'FAM': '@F1@', 'WIFE_NAME': 'Xiumei /Xue/',
              'DIV': 'NONE', 'MARR': '1986-09-10', 'HUSB_NAME': 'Jianjun /Dang/'},
             {'num': 104, 'WIFE': '@I6@', 'CHIL': ['@I9@'], 'HUSB': '@I7@', 'FAM': '@F4@', 'WIFE_NAME': 'Xiumei /Xue/',
              'DIV': '1985-11-12', 'MARR': '1971-08-11', 'HUSB_NAME': 'Zhenli /Zhang/'},
              {'num': 66, 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I5@', '@I9@', '@I8@', '@I10@', '@I1@'], 'HUSB': '@I4@',
               'FAM': '@F6@', 'WIFE_NAME': 'Xiuzhen /Mei/', 'DIV': 'NONE', 'MARR': '1959-10-16', 'HUSB_NAME': 'Zhishan /Xue/'}
              ]

        self.assertIs(multiple_births_less_5(l1,f1[3:]),True)
        self.assertIs(multiple_births_less_5(l1,f1),False)
        self.assertIs(multiple_births_less_5(l1, f1), False)
        self.assertEqual(multiple_births_less_5(l1,f1), False)
        self.assertTrue(multiple_births_less_5(l1,f1[3:]), True)


if __name__ == '__main__':
    unittest.main()
