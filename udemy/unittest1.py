import unittest
import docktest

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = docktest.Cal()
        self.assertEqual(cal.add_num_and_double(1,1),4)

# command:python -m unittest unittest1.py

"""값이 4일때
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""

"""값이 5일때
======================================================================
FAIL: test_add_num_and_double (unittest1.CalTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jeonsuhyeon/projects/Study-Python/udemy/unittest1.py", line 7, in test_add_num_and_double
    self.assertEqual(cal.add_num_and_double(1,1),5)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 1 test in 0.000s
"""
