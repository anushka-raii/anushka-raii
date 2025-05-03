#Write a function repeat_word(word, times) that prints the given word exactly times times.

def repeat_word(word, times):
    for _ in range(times):
        print(word)
repeat_word("hello", 3)
