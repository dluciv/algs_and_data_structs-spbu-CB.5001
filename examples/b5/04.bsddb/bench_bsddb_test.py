#!/usr/bin/env python3

from bsddb3 import db
from timeit import timeit


hash_file_name = "num_hash.bsddb"
tree_file_name = "num_tree.bsddb"

test_start = 200000
test_size = 1000

hash_num_db = db.DB()
tree_num_db = db.DB()
hash_num_db.open(hash_file_name)
tree_num_db.open(tree_file_name)


rkeys = [n.to_bytes(4, byteorder='big') for n in range(test_start, test_start + test_size)]

def test_hash(do_print = False):
    n = 0
    for key in rkeys:
        value = hash_num_db.get(key)
        if do_print and n % 100 == 0:
            print(value.decode('UTF-8'))
        n += 1

def test_tree(do_print = False):
    cursor = tree_num_db.cursor()
    cursor.set(rkeys[0])  # ещё бывает set_range — можно отступить назад
    value = cursor.current()[1]
    for n in range(test_start, test_start + test_size):
        if do_print and n % 100 == 0:
            print(value.decode('UTF-8'))
        value = cursor.next()[1]

def test_tree_on_hash(do_print = False):
    n = 0
    for key in rkeys:
        value = tree_num_db.get(key)
        if do_print and n % 100 == 0:
            print(value.decode('UTF-8'))
        n += 1

test_hash(True)
test_tree(True)
test_tree_on_hash(True)

print("1.", timeit(test_hash, number=1000))
print("2.", timeit(test_tree, number=1000))
print("3.", timeit(test_tree_on_hash, number=1000))  # А на каком размере отстанет?

hash_num_db.close()
tree_num_db.close()
