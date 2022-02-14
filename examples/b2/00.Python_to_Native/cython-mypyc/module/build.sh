#!/bin/bash

./setup.py build_ext --inplace
mypyc fate3.py
mv *.so ..
