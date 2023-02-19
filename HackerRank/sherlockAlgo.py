"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""


def isValid(s: str) -> str:
    # Write your code here
    letter_appear: dict = {}
    for letter in s:
        if letter in letter_appear:
            letter_appear[letter] += 1
        else:
            letter_appear[letter] = 1

    apparitions = [n for n in letter_appear.values()]

    if len(set(apparitions)) > 2:
        return "NO"

    if len(apparitions) == 3 and len(set(apparitions)) == 2:
        if 1 in set(apparitions) and apparitions.count(1) == 1:
            pass
        else:
            return "NO"

    for n in set(apparitions):
        if apparitions.count(n) > 1 and len(apparitions) - apparitions.count(n) > 1:
            return "NO"
    return "YES"
