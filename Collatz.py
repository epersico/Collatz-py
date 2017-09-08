#!/usr/bin/env python3

# ----------------------------------
# projects/python/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ----------------------------------

from io import StringIO
# import cProfile
# ------------
# collatz_read
# ------------
# import numpy as np
def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_cycleLength(n):
    cycleLength = 1
    while n != 1:
        cycleLength += 1
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return cycleLength

# def collatz_eval (i,j) : 
#     currentCycleLength = 0
#     maxCycleLength = 0
#     for num in range(i,j+1):
#         currentCycleLength = collatz_cycleLength(num)
#         if currentCycleLength > maxCycleLength:
#             maxCycleLength = currentCycleLength
#     return maxCycleLength

def collatz_iterate(n):
    if n%2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    return n

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    maxCycleLength = 0
    cycleLengthDict = {1 : 1}

    for n in range(i, j+1):
        cycleLength = 1
        cycle = []
        # cycle = np.zeroes(550,numpy.int32)
        # cycle = array
        while True:
            cycle.append(n)
            # cycle[cycleLength] = n
            if n in cycleLengthDict:
                cycleLength += cycleLengthDict[n] - 1
                # print("hit",n,"which was in dict with cycle length",cycleLengthDict[n])
                break
            cycleLength += 1
            n = collatz_iterate(n)
        # print("Cycle length for",num, "is", cycleLength)
        # print(cycle)
        
        # if cycleLength > maxCycleLength:
        #     maxCycleLength = cycleLength  

        for i in range(0, len(cycle)):
            # if cycle[i+1] not in cycleLengthDict:
            if cycle[i] not in cycleLengthDict:
                cycleLengthDict[cycle[i]] = cycleLength
                # print("for ", element, "cycle length was",cycleLength)
            cycleLength -= 1
         
    return max(cycleLengthDict.values())


# -------------
# collatz_print
# -------------

def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

import sys
if __name__ == "__main__":
        r = StringIO("1 100\n100 2000\n201 2100\n900 10000\n")
        w = StringIO()
        collatz_solve(r, sys.stdout)
    # collatz_solve(sys.stdin, sys.stdout)
