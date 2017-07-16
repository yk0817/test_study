import unittest 

class PyTest(unittest.TestCase):

    def test_do_something(self):
        one = 1
        self.assertEqual(one,1, "one is 1")
        
if __name__ == "__main__":
    unittest.main()
