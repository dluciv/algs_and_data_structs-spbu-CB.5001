#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as plt
import itertools


def plot_r_p():
    xs = ys = [0, 1]
    plt.ylabel('Репа')
    plt.xlabel('Потроха')
    plt.plot(xs, ys)
    plt.savefig("../12.linear-can.svg")

def plot_r_p_nl():
    xs = numpy.r_[0:1:1/100.0]
    ys = xs*xs

    plt.ylabel('Репа')
    plt.xlabel('Потроха')
    plt.plot(xs, ys)
    plt.savefig("../12.linear-cant.svg")


def sigmoid(x):
    return 1 / (1 + math.exp(x))

def plot_sin(z):
    xs = numpy.r_[0:math.pi:1/200.0]
    ys = list(map(math.sin, xs))

    plt.ylabel('sin x')
    plt.xlabel('x')
    plt.plot(xs, ys)
    plt.savefig("../12.linear-sin-1.svg")


    if z:
        ys = list(map(lambda x: round(math.sin(x)*10)/10, xs))
        plt.plot(xs, ys)
        plt.savefig("../12.linear-sin-2.svg")
    else:
        pass


if __name__ == '__main__':
    plt.switch_backend('agg')  # to run headless
    plot_r_p()
    plt.clf()
    plot_r_p_nl()
    plt.clf()
    plot_sin(True)
    plt.clf()

