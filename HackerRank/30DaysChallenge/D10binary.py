"""
Task
Given a base-10 integer, , convert it to binary (base-2). 
Then find and print the base- integer denoting the maximum number of 
consecutive 's in 's binary representation.
"""
def to_binary(number: int) -> str:
    bin_number = ""
    while number//2 != 0:
        bin_number += str(number%2)
        number //= 2
    bin_number += "1"
    return bin_number[::-1]

def max_num_consecurive(number: int) -> int:
    pass
