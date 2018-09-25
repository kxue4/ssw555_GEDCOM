#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/24/18
# @Author  : Zhiren Yang
# @File    : test_US23.py
# @Software: PyCharm

import unittest
from UserStories.US23 import unique_name_and_birth


class TestUniqueNameAndBirth(unittest.TestCase):

    def test_unique_ids(self):

        self.assertRaises(Exception, unique_name_and_birth, [{'NAME': 'Zhiren /Yang/', 'BIRT': '1993-12-26'},
                                                             {'NAME': 'Zhiren /Yang/', 'BIRT': '1993-12-26'}])

        self.assertEqual(unique_name_and_birth([{'NAME': 'Zhiren /Yang/', 'BIRT': '2014-06-21'},
                                                {'NAME': 'A /B/',         'BIRT': '1993-12-26'}]), None)
        self.assertEqual(unique_name_and_birth([{'NAME': 'Zhiren /Yang/', 'BIRT': '1993-12-26'},
                                                {'NAME': 'Zhiren /Yang/', 'BIRT': '2014-06-21'}]), None)
        self.assertEqual(unique_name_and_birth([{'NAME': 'A /B/',         'BIRT': '1993-12-26'},
                                                {'NAME': 'Zhiren /Yang/', 'BIRT': '1993-12-26'}]), None)
        self.assertEqual(unique_name_and_birth([{'NAME': 'Zhiren /Yang/', 'BIRT': '2014-06-21'}]), None)


if __name__ == '__main__':
    unittest.main()
