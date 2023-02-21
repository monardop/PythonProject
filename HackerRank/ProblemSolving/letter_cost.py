""" 
Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs. 
She can perform them any number of times to construct a new string:
    Append a character to the end of string  at a cost of 1 dollar.
    Choose any substring of p and append it to the end of  at no charge. 
"""
def stringConstruction(s):
    # every new letter cost 1dls
    char_list = [] 
    for letter in s:
        if letter not in char_list:
            char_list.append(letter)
    
    return len(char_list)
