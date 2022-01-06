import unittest
import docktest

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = docktest.Cal()
        self.assertEqual(cal.add_num_and_double(1,1),4)

    # def test_add_num_and_double_raise(self):
    #     cal = docktest.Cal()
    #     cal.add_num_and_double('1','1')

# ======================================================================
# ERROR: test_add_num_and_double_raise (unittestException.CalTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/jeonsuhyeon/projects/Study-Python/udemy/unittestException.py", line 11, in test_add_num_and_double_raise
#     cal.add_num_and_double('1','1')
#   File "/Users/jeonsuhyeon/projects/Study-Python/udemy/docktest.py", line 15, in add_num_and_double
#     raise ValueError
# ValueError

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (errors=1)

    def test_add_num_and_double_raise(self): #예외처리 test시에는 with를 사용한다.
        cal = docktest.Cal()                 #ValueError가 나오면 통과!
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1','1')

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# OK

