#!/usr/bin/python


def ways(cur_pos, moves_remaining, end):
    if (cur_pos, moves_remaining) in ways.cache:
        return ways.cache[(cur_pos, moves_remaining)]
    if cur_pos < 1 or cur_pos > end:
        return 0
    if moves_remaining < end - cur_pos:
        return 0
    if cur_pos == end:
        return 1
    if moves_remaining == 0:
        return 0

    ways.cache[(cur_pos, moves_remaining)] = \
        (ways(cur_pos - 1, moves_remaining - 1, end) +
         ways(cur_pos + 1, moves_remaining - 1, end) +
         ways(cur_pos, moves_remaining - 1, end)) % 123454321

    return ways.cache[(cur_pos, moves_remaining)]


ways.cache = {}


def answer(t, n):
    ways.cache = {}
    # Warm up the cache
    for i in xrange(0, n + 1):
        ways(n - i + 1, min(500, t - n + i + 1), n)

    return ways(1, t, n)

# assert(1 == answer(9, 10))
# assert(10 == answer(10, 10))
# assert(63 == answer(11, 10))
# assert(20636 == answer(15, 10))
# assert(28107209 == answer(21, 10))
# assert(87854134 == answer(22, 10))
# assert(60996905 == answer(500, 100))

# assert(0 == answer(0, 2))
# assert(0 == answer(0, 10))
# print answer(1, 2)
# print answer(1, 3)
# print answer(1000, 501)


# for n in xrange(2,1001):
# 	print (1000, n)
# 	print answer(1000, n)

# print answer(2, 2)
# print answer(3, 2)
# print answer(4, 2)
# print answer(1, 3)
# print answer(2, 3)
# print answer(3, 3)
# print answer(4, 3)
# print answer(10, 4)
# print answer(100, 4)
# print answer(100, 100)
# print answer(950, 950)
# print answer(1000, 1000)
# print answer(1000, 950)
# print answer(1000, 3)
# print answer(1000, 501)

# print answer(1000, 2)
# print answer(1000, 100)
# print answer(1000, 200)
# print answer(1000, 300)
# print answer(1000, 400)
# print answer(1000, 500)
# print answer(1000, 600)
# print answer(1000, 700)
# print answer(1000, 800)
# print answer(1000, 900)
# print answer(1000, 950)
# print answer(1000, 1000)
