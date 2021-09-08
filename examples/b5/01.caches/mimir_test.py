#!/usr/bin/env python3

from PyMimircache import Cachecow

if __name__=='__main__':
    c = Cachecow()
    c.vscsi("trace.vscsi")      # this file is in the data folder on GitHub, other data types also supported
    print(c.stat())
    print(c.get_reuse_distance())
    print(c.get_hit_ratio_dict("LRU", cache_size=20))

    c.plotHRCs(["LRU", "LFU", "Optimal"])
    c.heatmap('r', "hit_ratio_start_time_end_time", time_interval=10000000, cache_size=2000)
