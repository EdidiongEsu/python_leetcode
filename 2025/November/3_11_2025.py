'''
Given a string input_string, return a new string in which all occurrences of character c1 in the original string replaced by c2. You cannot use any built-in string methods or functions in Python, such as replace().

Here's an example:

print(replace_character("hello, world", "o", "a"))  
# Output: "hella, warld

Solution:
'''



def replace_character(input_string, c1, c2):
    # TODO: Replace all occurrences of character `c1` in `input_string` with `c2`
    new_word = ""
    for word in input_string:
    if word is c1:
        new_word += c2
    else:
        new_word += word

    return new_word
            
