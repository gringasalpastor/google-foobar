#!/usr/bin/python

from collections import defaultdict


def min_max(terms, term_map):
    _min = ("***", 999999)
    _max = ("***", -999999)

    for t in terms:
        if term_map[t][0] < _min[1]:
            _min = (t, term_map[t][0])
        if term_map[t][0] > _max[1]:
            _max = (t, term_map[t][0])
    return (_min, _max)


def answer(document, searchTerms):
    terms = set(searchTerms)
    term_map = defaultdict(list)

    tokens = document.split()
    for i in xrange(0, len(tokens)):
        if tokens[i] in terms:
            term_map[tokens[i]].append(i)

    sol = min_max(terms, term_map)
    sol_size = sol[1][1] - sol[0][1]  # max - min
    curr_sol = sol
    while(True):
        size = curr_sol[1][1] - curr_sol[0][1]
        if size < sol_size:
            sol_size = size
            sol = curr_sol

        if len(term_map[curr_sol[0][0]]) == 1:
            break
        else:
            del term_map[curr_sol[0][0]][0]
            curr_sol = min_max(terms, term_map)

    ret = ""
    for i in xrange(sol[0][1], sol[1][1] + 1):
        ret += " " + tokens[i]
    return ret.strip()

# print answer("a b c d a", ["a", "c", "d"])
# print answer("many google employees can program", ["google", "program"])
