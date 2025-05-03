#Write a function is_palindrome(word) that checks whether a given string is a palindrome (reads the same forward and backward).Return True if it is, else False.

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))  
print("Is 'hello' a palindrome?", is_palindrome("hello"))  
