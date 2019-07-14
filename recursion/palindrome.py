def is_palindrome(word):        
    if word == word[::-1]:
        return True
    return False

# TEST
print(is_palindrome('palindrome')) # False
print(is_palindrome('sortros')) # True
