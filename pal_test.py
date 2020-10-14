import unittest
from pal import isPalindrome,add
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(isPalindrome('abc'), False)
        self.assertEqual(isPalindrome('aba'), 1)
        self.assertEqual(isPalindrome('123'), 0)
        self.assertEqual(isPalindrome('121'), 1)
        self.assertEqual(add(5,7), 12)
        self.assertEqual(add(5,7), 15)
        
if __name__ == '__main__':
    unittest.main()
    #ss
