"""
Given an array of integers, find the minimum absolute difference between any two elements in the array.
"""

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    difference_array = []
    for index in enumerate(arr):
        for element in enumerate(arr):
            if element == index:
                pass
            else:
               difference_array.append(abs(arr[index] - arr[element])) 

    return min(difference_array)


minimumAbsoluteDifference([-2,2,4])