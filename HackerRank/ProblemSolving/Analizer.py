"""
In the first line, print True if  has any alphanumeric characters. 
In the second line, print True if  has any alphabetical characters.
In the third line, print True if  has any digits. 
In the fourth line, print True if  has any lowercase characters.
In the fifth line, print True if  has any uppercase characters. 
"""


def str_analizer(s: str):
    print(any(True for n in s if n.isalnum()))
    print(any(True for n in s if n.isalpha()))
    print(any(True for n in s if n.isdigit()))
    print(any(True for n in s if n.islower()))
    print(any(True for n in s if n.isupper()))


if __name__ == '__main__':
    s = input()
    str_analizer(s)
