#!/usr/bin/python

import math


def num_squares(n):
    root = math.sqrt(n)
    root_floor = int(root)
    s = math.pow(root_floor, 2)
    if s == n:
        return 1
    else:
        return 1 + num_squares(n - s)


def answer(n):
    return num_squares(n)

# print answer(24)
# print answer(160)
