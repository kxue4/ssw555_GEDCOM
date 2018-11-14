#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_US30.py
# @Author: Zhiren Yang
# @Date  : 18-10-19
# @Software : PyCharm
# @Desc  : test--List all living married people in a GEDCOM file

import unittest
from UserStories.US30 import list_living_married


class TestListLivingMarried(unittest.TestCase):

    def test_list_living_married(self):

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

        self.assertIs(list_living_married(l1), None)
        self.assertIs(list_living_married(l1[:6]), None)
        self.assertIs(list_living_married(l1[4:7]), None)
        self.assertEqual(list_living_married(l1), None)
        self.assertIs(list_living_married(l1[3:]), None)


if __name__ == '__main__':
    unittest.main()