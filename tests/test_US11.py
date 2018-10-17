#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/2
# @Author  : Jiaxin Wang
# @File    : test_US11.py
# @Software: PyCharm
import unittest
from UserStories.US11 import no_bigamy


class TestNoBigamy(unittest.TestCase):

    def test_no_bigamy(self):
        self.assertFalse( no_bigamy([{'SPOUSE': ['@F1@', '@F2@'],'num':14}],
                          [{'FAM':'@F1@','MARR': '1993-08-15','DIV':'1995-08-15','num':13},{'FAM':'@F2@','MARR': '1994-08-15','DIV':'1997-08-15','num':14}]))
        self.assertFalse(no_bigamy([{'SPOUSE': ['@F1@', '@F2@'],'num':14}],
                          [{'FAM':'@F1@','MARR': '1993-08-15','DIV':'1995-08-15','num':13},{'FAM':'@F2@','MARR': '1994-08-16','DIV':'1997-08-15','num':14}]))
        self.assertFalse(no_bigamy([{'SPOUSE': ['@F1@', '@F2@'],'num':14}],
                          [{'FAM':'@F1@','MARR': '1993-08-15','DIV':'1995-08-15','num':13},{'FAM':'@F2@','MARR': '1994-08-17','DIV':'1997-08-15','num':14}]))
        self.assertFalse(no_bigamy([{'SPOUSE': ['@F1@', '@F2@'],'num':14}], [{'FAM':'@F1@','MARR': '1993-08-15','DIV':'1995-08-15','num':14},{'FAM':'@F2@','MARR': '1996-08-16','DIV':'1997-08-15','num':14}]))
        self.assertFalse(no_bigamy([{'SPOUSE': ['@F1@', '@F2@'],'num':14}], [{'FAM':'@F1@','MARR': '1993-08-15','DIV':'1995-08-15','num':14},{'FAM':'@F2@','MARR': '1996-08-15','DIV':'1997-08-15','num':14}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)