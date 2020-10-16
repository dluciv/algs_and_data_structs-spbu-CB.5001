#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform#Sample_implementation

STX = "{"
ETX = "}"

def bwt(s: str) -> str:
    """Apply Burrows–Wheeler transform to input string."""
    assert STX not in s and ETX not in s, "Input string cannot contain STX and ETX characters"
    s = STX + s + ETX  # Add start and end of text marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string

def ibwt(r: str) -> str:
    """Apply inverse Burrows–Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith(ETX)][0]  # Find the correct row (ending in ETX)
    return s.rstrip(ETX).strip(STX)  # Get rid of start and end markers

s = input("> ")
b = bwt(s)
print("<" + b + ">")
i = ibwt(b)
print("<" + i + ">")
