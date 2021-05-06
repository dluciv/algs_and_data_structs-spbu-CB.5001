#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Fate',
  ext_modules = cythonize("fate.py")
)

setup(
  name = 'FFate',
  ext_modules = cythonize("ffate.pyx")
)

# ./setup.py build_ext --inplace
