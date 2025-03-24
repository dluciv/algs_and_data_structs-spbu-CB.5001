#!/bin/bash

rm a.out 2>/dev/null
set -e

gcc -O3 ct.c

echo '=============== by row ==============='
time ./a.out r
echo '=============== by col ==============='
time ./a.out c
echo '========== valgrind by row ==========='
valgrind --tool=cachegrind --cache-sim=yes ./a.out r
echo '========== valgrind by col ==========='
valgrind --tool=cachegrind --cache-sim=yes ./a.out c

rm a.out