#!/usr/bin/env python3

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
  ext_modules = cythonize("pure_cython.py")
)

setup(
  ext_modules = cythonize("pyx_cython.pyx")
)
