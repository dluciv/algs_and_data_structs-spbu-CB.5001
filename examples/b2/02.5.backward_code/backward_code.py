#!/usr/bin/env python3

from __future__ import annotations
from typeguard import typechecked
from numbers import Integral, Number

from numpy import uint8

@typechecked
class OneComp(Number): # (Integral): # Tooo many to implement

    def __init__(self, i: Integral|OneComp):
        if isinstance(i, OneComp):
            self.v: uint8 = i.v
        else:
            if i >= 0:
                self.v: uint8 = uint8(i)
            else:
                self.v: uint8 = (-i) ^ 0b11111111

    def __eq__(self, o: OneComp) -> bool:
        return bool(self.v == o.v)

    def __ne__(self, o: OneComp) -> bool:
        return bool(self.v != o.v)

    def __neg__(self) -> OneComp:
        return OneComp(self.v ^ 0b11111111)

    def __add__(self, other: OneComp) -> OneComp:
        return OneComp(self.v + other.v)

    def __sub__(self, other: OneComp) -> OneComp:
        return OneComp(self.v + (-other.v))  # Number theory here?.. =)

    def __str__(self) -> str:
        if self.v & 0b10000000 == 0:
            return str(self.v)
        else:
            return '-' + str(-self)
    
    def __repr__(self) -> str:
        return bin(self.v) + ' (=' + str(self) + ')'
