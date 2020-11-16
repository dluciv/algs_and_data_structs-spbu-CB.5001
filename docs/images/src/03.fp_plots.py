#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as plt


densconst = 2.0**23

def density(x):
    return 2.0 ** -(-math.floor(-math.log(x)/math.log(2.0))) * densconst

def deltaa(x):
    return 1.0/2.0/density(x) / 2.0

def deltar(x):
    return deltaa(x) / x


def plot_density():
    xs = numpy.r_[1/8.0:10.0:1/100.0]

    c, = plt.plot(xs, list(map(lambda x: densconst/x, xs)))
    d, = plt.plot(xs, list(map(density, xs)))

    xt = [0, 1/8, 1/4, 1/2, 1, 2, 4, 8]
    plt.xticks(xt, ['0', '', '', '$\\frac{1}{2}$', '1', '2', '4', '8'])
    xty = xt[1:5]
    plt.yticks(
        [0] + [density(n + 1/8) for n in xty],
        ['0'] + [f"$2^{{{round(math.log2(density(n)))}}}$" for n in xty]
    )

    plt.ylabel('Плотность')
    plt.xlabel('Значение')
    plt.legend([c, d], ['По идее', 'На самом деле'])

    plt.grid(which='major')

    plt.savefig("../03.fp-density.svg")

def plot_deltas():
    xs = numpy.r_[1/8.0:10.0:1/100.0]

    ax = plt.axes()

    xt = [0, 1/8, 1/4, 1/2, 1, 2, 4, 8]
    plt.xticks(xt, ['0', '', '', '$\\frac{1}{2}$', '1', '2', '4', '8'])

    ytl = [f"$2^{{{n}}}$" for n in range(-24, -20)]
    ytl[0] = "$\\frac{\\varepsilon}{2}$ = " + ytl[0]
    plt.yticks([0] + [2**n for n in range(-24, -20)], ['0'] + ytl, rotation=60)
   
    ax.grid(which='major')

    a, = plt.plot(xs, list(map(deltaa, xs)))
    r, = plt.plot(xs, list(map(deltar, xs)))

    plt.ylabel('Погрешности')
    plt.xlabel('Значение')
    plt.legend([a, r], ['Δ', 'δ'])

    plt.savefig("../03.fp-deltas.svg")


def plot_cplx_reim():
    r = numpy.linspace(-1, 1, 61)
    i = numpy.linspace(-1, 1, 61)
    X, Y = numpy.meshgrid(r, i)

    dv = numpy.array([min(abs(1/x/y),10.0) for x in r for y in i])
    Z = dv.reshape(61, 61)

    plt.gca().set_aspect('equal')
    plt.pcolor(X, Y, Z)
    plt.savefig("../03.fp-compvec.svg")

    plt.clf()

    dp = numpy.array([min(1/(x**2 + y**2),10.0) for x in r for y in i])
    Z = dp.reshape(61, 61)

    plt.gca().set_aspect('equal')
    plt.pcolor(X, Y, Z)
    plt.savefig("../03.fp-comppol.svg")


if __name__ == '__main__':
    plt.switch_backend('agg')  # to run headless
    plot_density()
    plt.clf()
    plot_deltas()
    plt.clf()
    plot_cplx_reim()
