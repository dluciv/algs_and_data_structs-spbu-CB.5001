from __future__ import annotations
from typing import Union
from numbers import Real

class Fool:  # (bool)
    def __init__(self, val: Union[bool, Fool, Real]):
        if isinstance(val, bool):
            self._v: Real = 1.0 if val else -1.0
        elif isinstance(val, Real):
            self._v: Real = min(1.0, max(-1.0, val))  # saturate
        elif isinstance(val, Fool):
            self._v: Real = val._v
        else:
            raise ValueError(f"Expected {help(val)}, got {type(val)}")

    @property
    def bool(self):
        if self._v == -1.0:
            return False
        elif self._v == 1.0:
            return True
        else:
            raise RuntimeError(f"This {type(self)} is not a bool")

    def float(self):
        return self._v

    def __hash__(self):
        return hash(self._v)

    def __eq__(self, other: Union[bool, Fool]):
        return self._v == Fool(other)._v
    
    def __lt__(self, other: Union[bool, Fool]):
        return self._v < Fool(other)._v
    
    def __le__(self, other: Union[bool, Fool]):
        return self._v <= Fool(other)._v

    def __gt__(self, other: Union[bool, Fool]):
        return self._v > Fool(other)._v
    
    def __ge__(self, other: Union[bool, Fool]):
        return self._v >= Fool(other)._v

    def __invert__(self):
        return Fool(- self._v)
    
    def __or__(self, other: Union[bool, Fool]):
        return Fool(max(self._v, Fool(other)._v))

    def __and__(self, other: Union[bool, Fool]):
        return Fool(min(self._v, Fool(other)._v))
    
    def __repr__(self):
        return f"Fool({self._v})"
    
    def __str__(self):
        if abs(self._v) == 1.0:
            return str(bool(self))
        else:
            return repr(self)

# Not doing this in method to help typecheckers
Fool.TRUE:      Fool = Fool(True)
Fool.FALSE:     Fool = Fool(False)
Fool.UNKNOWN:   Fool = Fool(0.0)
Fool.LIKELY:    Fool = Fool(0.5)
Fool.UNLIKELY:  Fool = Fool(-0.5)

if __name__=='__main__':
    raise RuntimeError("This module is not supposed to be launched")
