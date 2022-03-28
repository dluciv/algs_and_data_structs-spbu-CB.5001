from __future__ import annotations
from numbers import Real

def class_init(cls):
    """
    Class init decorator, inspired by  https://stackoverflow.com/a/60748729
    """
    if getattr(cls, "__class_init__", None):
        cls.__class_init__()
    return cls

@class_init
class Fool:  # (bool)

    @classmethod
    def __class_init__(cls):
        """
        Typecheckers will not likely find below values
        """
        cls.TRUE:     cls = cls(True)
        cls.FALSE:    cls = cls(False)
        cls.UNKNOWN:  cls = cls(0.0)
        cls.LIKELY:   cls = cls(0.5)
        cls.UNLIKELY: cls = cls(-0.5)

    def __init__(self, val: bool | Fool | Real):
        if isinstance(val, bool):
            self._v: Real = 1.0 if val else -1.0
        elif isinstance(val, Real):
            self._v: Real = min(1.0, max(-1.0, val))  # saturate
        elif isinstance(val, Fool):
            self._v: Real = val._v
        else:
            raise ValueError(f"Expected {help(val)}, got {type(val)}")

    def __bool__(self):
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

    def __eq__(self, other: bool | Fool):
        return self._v == Fool(other)._v
    
    def __lt__(self, other: bool | Fool):
        return self._v < Fool(other)._v
    
    def __le__(self, other: bool | Fool):
        return self._v <= Fool(other)._v

    def __gt__(self, other: bool | Fool):
        return self._v > Fool(other)._v
    
    def __ge__(self, other: bool | Fool):
        return self._v >= Fool(other)._v

    def __neg__(self):
        return Fool(- self._v)
    
    def __invert__(self):
        return Fool(- self._v)        
    
    def __or__(self, other: bool | Fool):
        return Fool(max(self._v, Fool(other)._v))

    def __and__(self, other: bool | Fool):
        return Fool(min(self._v, Fool(other)._v))
    
    def __repr__(self):
        return f"Fool({self._v})"
    
    def __str__(self):
        if abs(self._v) == 1.0:
            return str(bool(self))
        else:
            return repr(self)

if __name__=='__main__':
    raise RuntimeError("This module is not supposed to be launched")
