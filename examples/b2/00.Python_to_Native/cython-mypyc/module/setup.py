#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Fate1',
  ext_modules = cythonize("fate1.py")
)

setup(
  name = 'Fate2',
  ext_modules = cythonize("fate2.pyx")
)

