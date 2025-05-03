#Write a function count_vowels(text) that counts the number of vowels (a, e, i, o, u) in the given text and returns the count.

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print("Vowel count:", count_vowels("Beautiful")) 
