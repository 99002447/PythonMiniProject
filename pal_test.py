import unittest
from pal import isPalindrome
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(isPalindrome('abc'), 0)
        self.assertEqual(isPalindrome('aba'), TRUE)
        self.assertEqual(isPalindrome('123'), FALSE)
        self.assertEqual(isPalindrome('121'), TRUE)
        
if __name__ == '__main__':
    unittest.main()
