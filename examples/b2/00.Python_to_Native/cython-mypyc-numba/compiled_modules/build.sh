#!/bin/bash

./setup.py build_ext --inplace
mypyc mypy_python.py
mv *.so ..
