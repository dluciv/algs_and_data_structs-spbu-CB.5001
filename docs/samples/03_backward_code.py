#!/usr/bin/env python3

from __future__ import annotations
from numpy import uint8
from numbers import Integral

class OneComp: # (Integral):
    def __init__(self, v: Integral):
        raise NotImplementedError("Реализуй меня!")
    
    def __neg__(self) -> OneComp:
        raise NotImplementedError("Реализуй меня!")
    
    def __add__(self, other: OneComp) -> OneComp:
        raise NotImplementedError("Реализуй меня!")
    
    def __sub__(self, other: OneComp) -> OneComp:
        raise NotImplementedError("Реализуй меня!")
    
    def __str__(self) -> str:
        raise NotImplementedError("Реализуй меня!")


if __name__ == '__main__':
    v1 = OneComp(10)
    v2 = OneComp(-12)
    v3 = v1 + v2
    v4 = v1 - v2
    print(v1, v2, v3, v4)
