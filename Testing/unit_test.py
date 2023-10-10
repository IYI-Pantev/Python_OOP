import unittest # test framework

class Test_Demo(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(4, 4)
    
    def test_decrement(self):
        self.assertEqual(3, 4)

    
if __name__ == '__main__ ':
    unittest.main()