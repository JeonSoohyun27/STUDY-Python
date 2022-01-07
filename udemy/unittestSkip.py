import unittest
import docktest


#release_name = 'lesson' 
#2번 

class CalTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.cal = docktest.Cal()

    def tearDown(self):
        print('clean up')
        self.cal
        
    @unittest.skip('skip!') #1번
    #@unittest.skipIf(release_name =='lesson','skip!')
    #2번
    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1,1),4)


    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

# ssetup
# clean up
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK (skipped=1)