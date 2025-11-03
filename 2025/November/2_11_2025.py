'''
Given a string input_string, your task is to write a function that transforms all the lowercase letters to uppercase and all the uppercase letters to lowercase. If the character is not a letter, do not transform it.

The transformation should be done without using any built-in Python methods, it is not allowed to use built-in Python functions like lower(), upper(), or similar in your code.

For example, for the input string "HelLo WoRld 123", the output should be "hELlO wOrLD 123".
'''

# Main solution
def solution(sample):
    new_text = ""
    for word in sample:
        if 65 <= ord(word) <= 90:
            new_text += chr(ord(word) + 32)
        elif 97 <= ord(word) <= 122:
            new_text += chr(ord(word) - 32)
        else:
            new_text += word
    
    return new_text


# If lower() and upper() were allowed:
def solution(sample):
    new_text = ''
    for word in sample:
        if word.islower():
            new_text += word.upper()
        elif word.isupper():
            new_text += word.lower()
        else:
            new_text += word
    
    return new_text
