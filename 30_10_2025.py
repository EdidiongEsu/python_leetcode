"""
Given a string, you need to return a new string where every letter is shifted to its right by one place in alphabetical order. The last letters z and Z should be replaced with the first ones: a and A, respectively. If the character isn't a letter, it should stay the same.

It is not allowed to use string built-in methods here.

For example, given the string "abc123XYz!", the function should return "bcd123YZa!".

"""

def solution(text_word):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    # text_word = "izAA#!b"
    new_word = ""

    for alp in text_word:
        if alp.lower() in alphabets:
            vowels_position = alphabets.index(alp.lower())
            # next_char = alphabets[vowels_position + 1] if vowels_position + 1 < len(alphabets) else alphabets[0]
            if vowels_position + 1 < len(alphabets):
                next_char = alphabets[vowels_position + 1]
            else:
                next_char = alphabets[0]
    
            if alp.islower():
                new_word += next_char.lower()
            else:
                new_word += next_char.upper()
        else:
            new_word += alp

    return new_word
    
