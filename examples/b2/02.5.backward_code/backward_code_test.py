#!/usr/bin/env python3

from __future__ import annotations
import unittest

from backward_code import OneComp

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.v0 = OneComp(0)
        self.v1 = OneComp(10)
        self.v2 = OneComp(-12)

    def test_minus_z(self):
        self.assertNotEqual(self.v0, -self.v0)
        self.assertEqual(self.v0, -(-self.v0))

    def test_sum(self):
        self.assertEqual(self.v1 + self.v2, OneComp(-2))
        self.assertEqual(self.v1 + self.v2, OneComp(-2))
        self.assertEqual(self.v1 - self.v2, OneComp(22))
        self.assertEqual(self.v2 - self.v1, OneComp(-22))

    def test_typing(self):
        self.assertRaises(TypeError, lambda: self.v1 + 3)

    def test_fail(self):
        pass  # self.fail()

if __name__ == '__main__':
    unittest.main()
