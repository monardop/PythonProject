# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X: list, W: list) -> float:
    # Write your code here
    nominator = 0
    denominator = sum(W)
    for x, y in zip(X, W):
        nominator += x * y
    return round(nominator / denominator, 1)

print(weightedMean([10,40,30,50,20], [1,2,3,4,5]))