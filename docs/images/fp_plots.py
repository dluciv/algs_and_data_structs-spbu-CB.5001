#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as plt


densconst = 2.0**23

def density(x):
    return 2.0 ** -(-math.floor(-math.log(x)/math.log(2.0))) * densconst

def deltaa(x):
    return 1.0/2.0/density(x)

def deltar(x):
    return deltaa(x) / x


def plot_density():
    xs = numpy.r_[1/10.0:10.0:1/100.0]

    c, = plt.plot(xs, list(map(lambda x: densconst/x, xs)))
    d, = plt.plot(xs, list(map(density, xs)))

    plt.xlabel('Значение')
    plt.legend([c, d], ['По идее', 'На самом деле'])

    plt.savefig("fp-density.svg")

def plot_deltas():
    xs = numpy.r_[1/100.0:20.0:1/100.0]

    a, = plt.plot(xs, list(map(deltaa, xs)))
    r, = plt.plot(xs, list(map(deltar, xs)))

    plt.xlabel('Значение')
    plt.legend([a, r], ['Δ', 'δ'])

    plt.savefig("fp-deltas.svg")


if __name__ == '__main__':
    plt.switch_backend('agg')  # to run headless
    plot_density()
    plt.clf()
    plot_deltas()
