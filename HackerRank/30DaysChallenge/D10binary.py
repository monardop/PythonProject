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
    bin_number: str = to_binary(number)
    group = []
    count = 0
    for pos, bit in enumerate(bin_number):
        if bit == '1':
            count += 1
        if bit == '0' and count > 0:
            group.append(count)
            count = 0
            if len(bin_number) - pos < max(group):
                break  # To prevent unnecessary cycles
    return max(group)

print(max_num_consecurive(200))