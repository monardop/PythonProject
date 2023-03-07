# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d: posiciones a la izquierda
#  2. INTEGER_ARRAY arr lista a modificar
#

def rotateLeft(d: int, arr: list):
    # Write your code here
    new_array = []
    # First I create the new array
    for n in range(len(arr)):
        new_array.append(0)
    
    for i, element in enumerate(arr):
        new_array[i - d] = element
    
    return new_array

# Alternativas:
def rotateLeft(d, arr):
    
    while d > 0:
        arr.append(arr.pop(0))
        d -=1 
   
    return arr 

def rotateLeft(d, arr):
    return arr[d:]+arr[:d]