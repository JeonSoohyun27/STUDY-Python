import unittest
import docktest

class CalTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.cal = docktest.Cal()

    def tearDown(self):
        print('clean up')
        self.cal

    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1,1),4)


    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

# setup
# clean up
# .setup
# clean up
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s


