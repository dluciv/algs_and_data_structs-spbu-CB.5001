#!/usr/bin/env python3

import unittest
from fool import Fool

class FoolTest(unittest.TestCase):
    def setUp(self):
        self.f1 = Fool.TRUE
        self.f2 = Fool.UNLIKELY

    def tearDown(self):
        pass

    def test_constants(self):
        self.assertEqual(Fool.LIKELY, ~Fool.UNLIKELY)
        self.assertNotEqual(Fool.LIKELY, Fool.TRUE)
    
    def test_binops(self):
        v1_ = self.f1 & self.f2
        v2_ = self.f1 | self.f2
        self.assertTrue(v2_)
        self.assertEqual(v1_, Fool.UNLIKELY)
    
    def test_unops(self):
        self.assertFalse((~self.f1).bool)
        self.assertGreater(~self.f2, Fool.UNKNOWN)
        self.assertRaises(RuntimeError, lambda: self.f2.bool)

if __name__ == '__main__':
    unittest.main()
