#!/usr/bin/python

from collections import defaultdict


def answer(meetings):
    end_time_map = defaultdict(list)

    end_times = list()
    for i in xrange(0, len(meetings)):
        end_time_map[meetings[i][1]].append(i)
        end_times.append(meetings[i][1])

    end_times.sort()
    left_wall = 0
    num_packed = 0

    for i in end_times:
        for m in end_time_map[i]:
            if meetings[m][0] >= left_wall:
                left_wall = i
                num_packed += 1
                continue

    return num_packed


# print answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43], [0, 1], [1, 2], [2, 3], [3, 5], [4, 5]])
# print answer([[0, 1000000], [42, 43], [0, 1000000]])
# print answer([ [0, 1], [1, 2], [2, 3], [3, 5], [4, 5]])
