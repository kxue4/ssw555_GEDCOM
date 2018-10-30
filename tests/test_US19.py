#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 6:25
# @Author  : Jiaxin Wang
# @File    : test_US19.py
# @Software: PyCharm
import unittest
from UserStories.US19 import first_cousin

indilist = [{'INDI': '@I1@',  'SPOUSE': 'NONE',   'num': 3,   'CHIL': 'NONE'},
            {'INDI': '@I2@',  'SPOUSE': ['@F1@'], 'num': 10,  'CHIL': ['@I1@']},
            {'INDI': '@I1@',  'SPOUSE': ['@F1@'], 'num': 18,  'CHIL': ['@I1@']},
            {'INDI': '@I3@',  'SPOUSE': ['@F2@'], 'num': 25,  'CHIL': ['@I2@', '@I6@']},
            {'INDI': '@I5@',  'SPOUSE': ['@F2@'], 'num': 34,  'CHIL': ['@I2@', '@I6@']},
            {'INDI': '@I6@',  'SPOUSE': ['@F3@', '@F4@'], 'num': 43, 'CHIL': ['@I9@']},
            {'INDI': '@I7@',  'SPOUSE': ['@F4@'], 'num': 52,  'CHIL': ['@I9@']},
            {'INDI': '@I8@',  'SPOUSE': ['@F3@'], 'num': 61,  'CHIL': ['@I10@']},
            {'INDI': '@I9@',  'SPOUSE': 'NONE',   'num': 68,  'CHIL': 'NONE'},
            {'INDI': '@I10@', 'SPOUSE': 'NONE',   'num': 75,  'CHIL': 'NONE'},
            {'INDI': '@I11@', 'SPOUSE': 'NONE',   'num': 82,  'CHIL': 'NONE'},
            {'INDI': '@I12@', 'SPOUSE': 'NONE',   'num': 89,  'CHIL': 'NONE'},
            {'INDI': '@I13@', 'SPOUSE': 'NONE',   'num': 96,  'CHIL': 'NONE'},
            {'INDI': '@I14@', 'SPOUSE': 'NONE',   'num': 103, 'CHIL': 'NONE'},
            {'INDI': '@I14@', 'SPOUSE': 'NONE',   'num': 110, 'CHIL': 'NONE'},
            {'INDI': '@I16@', 'SPOUSE': 'NONE',   'num': 117, 'CHIL': 'NONE'},
            {'INDI': '@I17@', 'SPOUSE': 'NONE',   'num': 124, 'CHIL': 'NONE'},
            {'INDI': '@I18@', 'SPOUSE': 'NONE',   'num': 131, 'CHIL': 'NONE'},
            {'INDI': '@I19@', 'SPOUSE': 'NONE',   'num': 138, 'CHIL': 'NONE'},
            {'INDI': '@I20@', 'SPOUSE': 'NONE',   'num': 145, 'CHIL': 'NONE'},
            {'INDI': '@I21@', 'SPOUSE': 'NONE',   'num': 152, 'CHIL': 'NONE'},
            {'INDI': '@I22@', 'SPOUSE': 'NONE',   'num': 159, 'CHIL': 'NONE'},
            {'INDI': '@I23@', 'SPOUSE': 'NONE',   'num': 166, 'CHIL': 'NONE'},
            {'INDI': '@I24@', 'SPOUSE': 'NONE',   'num': 173, 'CHIL': 'NONE'},
            {'INDI': '@I25@', 'SPOUSE': 'NONE',   'num': 180, 'CHIL': 'NONE'},
            {'INDI': '@I26@', 'SPOUSE': 'NONE',   'num': 187, 'CHIL': 'NONE'}]

famlist_correct = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'num': 194},
           {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'num': 201},
           {'FAM': '@F3@', 'HUSB': '@I1@', 'WIFE': '@I7@', 'CHIL': ['@I10@'], 'num': 209},
           {'FAM': '@F4@', 'HUSB': '@I2@', 'WIFE': '@I7@', 'CHIL': ['@I9@'], 'num': 216},
           {'FAM': '@F5@', 'HUSB': '@I7@', 'WIFE': '@I10@', 'CHIL': ['@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@'], 'num': 225}]

famlist_fault = [{'FAM': '@F1@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@'], 'num': 194},
           {'FAM': '@F2@', 'HUSB': '@I4@', 'WIFE': '@I5@', 'CHIL': ['@I2@', '@I6@'], 'num': 201},
           {'FAM': '@F3@', 'HUSB': '@I1@', 'WIFE': '@I6@', 'CHIL': ['@I10@'], 'num': 209},
           {'FAM': '@F4@', 'HUSB': '@I2@', 'WIFE': '@I9@', 'CHIL': ['@I9@'], 'num': 216},
           {'FAM': '@F5@', 'HUSB': '@I1@', 'WIFE': '@I9@', 'CHIL': ['@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@'], 'num': 225}]

class Testfirst_cousin(unittest.TestCase):

    def test_aunt_uncle(self):
        self.assertTrue(first_cousin(indilist, famlist_correct))
        self.assertTrue(first_cousin(indilist, famlist_correct))
        self.assertFalse(first_cousin(indilist, famlist_fault))
        self.assertFalse(first_cousin(indilist, famlist_fault))
        self.assertFalse(first_cousin(indilist, famlist_fault))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
