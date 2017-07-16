import unittest 

class PyTest(unittest.TestCase):
    
    def test_equal(self):
        one = 1
        self.assertEqual(one,1, "one is 1")
    
    def test_not_equal(self):
        two = 2
        self.assertNotEqual(two,3,"2 not equal 3")
        
    def test_almost_equal(self):
        three = 3.1
        self.assertAlmostEqual(three,3,0,"3.1 almost equal 3")
    
    def test_assert_regex(self):
        sentence = "test作業はつまらない。じゃなくて、楽しいぞ〜"
        self.assertRegex(sentence,'test.+楽.{1,}〜$',"test作業:マッチ")
        
if __name__ == "__main__":
    unittest.main()