# Palindrome Checker
def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

print("Is 'madam' a palindrome?", is_palindrome("madam"))  
print("Is 'hello' a palindrome?", is_palindrome("hello"))
