""""
John Watson knows of an operation called a right circular rotation on an array 
of integers. One rotation operation moves the last array element to the first 
position and shifts all remaining elements right one. To test Sherlock's 
abilities, Watson provides Sherlock with an array of integers. Sherlock is to 
perform the rotation operation a number of times then determine the value of 
the element at a given position.

For each array, perform a number of right circular rotations and return the 
values of the elements at the given indices.
"""

# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a: list, k: int, queries: list) -> list:
    # Write your code here  
    x = len(a) - k 
    a = a[x:] + a[0:x]

    return [a[n] for n in queries]
    
(circularArrayRotation(list(range(100)), 10, [1,2]))
