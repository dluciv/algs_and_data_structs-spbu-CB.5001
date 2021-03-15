#!/usr/bin/env python3

from __future__ import annotations
from typing import Union
from typeguard import typechecked
import unittest

from numpy import uint8
from numbers import Integral

from backward_code import OneComp

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.v0 = OneComp(0)
        self.v1 = OneComp(10)
        self.v2 = OneComp(-12)
    
    def test_minus_z(self):
        self.assertNotEqual(self.v0, -self.v0)
        self.assertEquals(self.v0, -(-self.v0))

    def test_sum(self):
        self.assertEquals(self.v1 + self.v2, OneComp(-2))
        self.assertEquals(self.v1 + self.v2, OneComp(-2))
        self.assertEquals(self.v1 - self.v2, OneComp(22))
        self.assertEquals(self.v2 - self.v1, OneComp(-22))
    
    def test_fail(self):
        pass  # self.fail()

if __name__ == '__main__':
    unittest.main()
        