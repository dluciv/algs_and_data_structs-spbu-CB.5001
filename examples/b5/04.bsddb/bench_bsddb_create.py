#!/usr/bin/env python3

from bsddb3 import db
import num2words.lang_RU as lr
from tqdm import tqdm
nw = lr.Num2Word_RU()


hash_file_name = "num_hash.bsddb"
tree_file_name = "num_tree.bsddb"
rec_num = 1_000_000

hash_num_db = db.DB()
tree_num_db = db.DB()
hash_num_db.open(hash_file_name, None, db.DB_HASH,  db.DB_CREATE)
tree_num_db.open(tree_file_name, None, db.DB_BTREE, db.DB_CREATE)

for n in tqdm(range(rec_num)):
    key = n.to_bytes(4, byteorder='big')  # str(n).encode('ASCII')
    value = nw.to_cardinal(n).encode('UTF-8')
    hash_num_db.put(key, value)
    tree_num_db.put(key, value)

hash_num_db.close()
tree_num_db.close()
