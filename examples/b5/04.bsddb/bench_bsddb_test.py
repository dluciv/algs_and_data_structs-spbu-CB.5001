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


def test_hash(print_every = 1000000):
    for n in range(test_start, test_start + test_size):
        key = n.to_bytes(4, byteorder='big')
        value = hash_num_db.get(key)
        if n % print_every == 0:
            print(value.decode('UTF-8'))


def test_tree(print_every = 1000000):
    start_key = test_start.to_bytes(4, byteorder='big')
    cursor = tree_num_db.cursor()

    cursor.set(start_key)  # ещё бывает set_range — можно отступить назад
    value = cursor.current()[1]
    for n in range(test_start, test_start + test_size):
        if n % print_every == 0:
            print(value.decode('UTF-8'))
        value = cursor.next()[1]

test_hash(print_every = 100)
test_tree(print_every = 100)

print(timeit(test_hash, number=1000))
print(timeit(test_tree, number=1000))

hash_num_db.close()
tree_num_db.close()
