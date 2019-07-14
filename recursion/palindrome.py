def is_palindrome(word):        
    # for i in range(len(word)):
    #     if word[i] == word[-1 - i]:
    #         continue
    #     return False
    # return True

    # if word == word[::-1]:
    #     return True
    # return False

    for left in range(len(word) // 2):
        right = len(word) - left -1
        if word[left] != word[right]:
            return False
    return True
