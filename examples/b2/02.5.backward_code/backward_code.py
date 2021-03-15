#!/usr/bin/env python3

from __future__ import annotations
from typing import Union
from typeguard import typechecked

from numpy import uint8
from numbers import Integral

@typechecked
class OneComp: # (Integral): # Tooo many to implement

    def __init__(self, i: Union[Integral, OneComp]):
        if isinstance(i, OneComp):
            self.v: uint8 = i.v
        else:
            if i >= 0:
                self.v: uint8 = uint8(i)
            else:
                self.v: uint8 = (-i) ^ 0b11111111

    def __eq__(self, o):
        return self.v == o.v

    def __neg__(self) -> OneComp:
        return OneComp(self.v ^ 0b11111111)

    def __add__(self, other: OneComp) -> OneComp:
        return OneComp(self.v + other.v)

    def __sub__(self, other: OneComp) -> OneComp:
        return OneComp(self.v + (-other.v))

    def __str__(self) -> str:
        if self.v & 0b10000000 == 0:
            return str(self.v)
        else:
            return '-' + str(-self)
    
    def __repr__(self) -> str:
        return bin(self.v)
