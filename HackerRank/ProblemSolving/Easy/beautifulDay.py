#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i: int, j: int, k: int) -> int:
    # Write your code here
    beautiful = 0
    for day in range(i, j + 1):
        inverse = str(day)
        inverse = int(inverse[::-1])
        if (day - inverse) % k == 0:
            beautiful += 1
    return beautiful

print(beautifulDays(20,23,6))