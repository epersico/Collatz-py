#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests1.py
# -------------

# https://docs.python.org/3.5/library/unittest.html
# https://docs.python.org/3.5/library/unittest.html#assert-methods

from unittest import main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% UnitTests1T.py
FFF
======================================================================
FAIL: test_1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 31, in test_1
    self.assertEqual(cycle_length( 1), 1)
  File "UnitTests1.py", line 26, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test_2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 34, in test_2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test_3 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 37, in test_3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
"""
