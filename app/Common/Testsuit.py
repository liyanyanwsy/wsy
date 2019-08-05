# -*- coding:utf-8 -*-

import unittest


def test_suit():
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover("D:\\Program Files\\Git\\11\\app" + "\\Cases", pattern='test*.py', top_level_dir=None)
    for suit in discover:
        for case in suit:
            test_unit.addTests(case)
    return test_unit
