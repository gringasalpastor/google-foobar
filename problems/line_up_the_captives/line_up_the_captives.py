#!/usr/bin/python

import math

'''
*divide the problem*
divide the problem into 2 parts by considering the position of the tallest rabbit
fixed at position j

..........|.........
1         j        N

we can itterate over all possible fixed positions. So this is not a big issue.
After placing the left j rabbits we are left some N-j rabbits for the right side.
These all have differnt sizes so they will work the same way for the right side.

*solve the left side*
so now we have to answer how many configerations we can make that have x-1 visible
from the left side given N-1 rabbites. see configerations()

'''


def configerations(N, num_visible):
    '''
    Given N rabbits and we want to have num_visible visable from one side, return the number
    of configerations that satisify this

    N           number of rabbits
    num_visible number that we want to have visible from one side
    '''
    if (N, num_visible) in configerations.cache:
        return configerations.cache[(N, num_visible)]

    # there is only one way to arrange them to have all visible
    # x=N --> 1,2,3,4,5,6,7,...,N
    if num_visible == N:
        return 1

    # we can't have more visible the totel number of rabbits
    if num_visible > N:
        return 0

    # if we want to have exactly 1 rabbit visible, then we have to put the tallest first.
    # the remaining N-1 can be placed in (N-1)! ways
    if num_visible == 1:
        return math.factorial(N - 1)

    # we have a summation here because were are considering all possible fixed values for j
    # to place the next tallest rabbit
    # after placing the next tallest we have j-1 rabbits and num_visible -1 ==>
    # configerations(j - 1, num_visible - 1)
    # there are choose(N - 1, j - 1) possible ways to pick these rabbits
    # and the remaining can be in any position, so (N - j)!

    # ......j...j'.....
    # \    / \ /
    #  \ /    remaining rabbits --> math.factorial(N - j)
    #   recursive step ---> configerations(j - 1, num_visible - 1)

    # choose(N - 1, j - 1) *                 # possible ways to pick rabbits to put into the j-1 holes
    # configerations(j - 1, num_visible - 1) * \ # ways to place these rabbits after we pick them
    # math.factorial(N - j)                     # ways to place the remaining
    # rabbits

    sum = 0
    for j in xrange(1, N + 1):
        sum += choose(N - 1, j - 1) * configerations(j - 1,
                                                     num_visible - 1) * math.factorial(N - j)

    configerations.cache[(N, num_visible)] = sum
    return sum


configerations.cache = {}


def choose(m, n):
    return math.factorial(m) / math.factorial(n) / math.factorial(m - n)


def answer(x, y, N):
    # we have a summation here because were are considering all possible fixed values for j
    # to place the tallest rabbit and divide the problem
    # there are choose(N - 1, j - 1) possible ways to pick these rabbits
    # number of possilbe left configeration ===>  configerations(j - 1, x - 1)
    # number of possilbe right configeration ===> configerations(N - j, y - 1)
    sum = 0
    for j in xrange(1, N + 1):
        sum += choose(N - 1, j - 1) * configerations(j - 1,
                                                     x - 1) * configerations(N - j, y - 1)

    print sum
    return str(sum)


# assert("2" == answer(2, 2, 3))
# assert("24" == answer(1, 2, 6))
# assert("7326560149480" == answer(5, 10, 20))
# assert("15437033962912768350798353700" == answer(5, 10, 30))
# assert("430261933676748324019225559566957794937562112" == answer(7, 8, 40))
