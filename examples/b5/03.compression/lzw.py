#!/usr/bin/env python3

from __future__ import annotations
import itertools
from typing import Iterable

asciipuls = [bytes([i]) for i in range(256)] + [b'']
# 256th — вообще не нужно, из уважения к https://youtu.be/8uFqfZOiwMc

def lzw_compress(inp: bytes)-> Iterable[int]:
    d = asciipuls.copy()
    result = []

    while len(inp) > 0:
        maxmatched = b''
        maxmatchedidx = -1
        for idx, val in zip(itertools.count(), d):
            if inp.startswith(val) and len(val) > len(maxmatched):
                maxmatchedidx = idx
                maxmatched = val
        # Нашли самый длинный словарный префикс
        result.append(maxmatchedidx)  # и добавляем его индекс в вызодной поток

        if len(maxmatched) == len(inp):  # сопоставили до конца
            break
        else: # не до конца => достраиваем словарь
            newstring = inp[:len(maxmatched) + 1]
            d.append(newstring)

            # оставляем во входе новый байт, убираем только то, что нашлось!
            inp = inp[len(maxmatched):]

    print(d[256:])
    return result  
            
def lzw_decompress(inp: Iterable[int])-> bytes:
    result = b''
    d = asciipuls.copy()

    # https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Decoding
    # To rebuild the dictionary in the same way as it was built during encoding,
    # it also obtains the next value from the input and adds to the dictionary
    # 
    # the concatenation of the current string and the first character of the string
    # obtained by decoding the next input value,
    # or
    # the first character of the string just output if the next value can not be decoded

    # for i, ii in zip(inp, inp[1:] + [256]):
    for i, i_ in zip(inp, inp[1:] + [256]):
        s = d[i]
        result += s

        # Достроим словарь
        if i_ < len(d):
            s1_ = d[i_][:1]
        else:
            s1_ = s[:1]
        d.append(s + s1_)

        # print(result, d[256:])

    return result

b = "Однажны в студёную зимнюю пору сижу за решёткой в темнице сырой".encode('utf-8')
# b = b"ABABABABABAB"
e = lzw_compress(b)
print(e, len(b), len(e))

d = lzw_decompress(e)
print(d.decode('utf-8'))
