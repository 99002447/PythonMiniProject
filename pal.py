def isPalindrome(inputUser):
    array = []
    palindrome_input = inputUser
    rev = ''.join(reversed(palindrome_input))
    if palindrome_input == rev:
        return True
    return False


ans = isPalindrome("BOB")
if ans:
    print("It's a palindrome\n")

else:
    print("It's not a palindrome\n")

# assert palindromeCheck('aba') == 1
