import unittest
from pal import isPalindrome
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(isPalindrome('abc'), 0)
        self.assertEqual(isPalindrome('aba'), 1)
        self.assertEqual(isPalindrome('123'), 0)
        self.assertEqual(isPalindrome('121'), 1)
        
if __name__ == '__main__':
    unittest.main()
