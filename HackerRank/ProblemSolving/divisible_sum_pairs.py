def divisibleSumPairs(n: int, k: int, ar: list) -> int:
    """
    Given an array of integers and positive integer k, 
    determine the number of (i,j) pairs where 
    i<j and ar[i] + ar[j] is divisible by k

    :param n:length of array
    :param k: the integer divisor
    :param ar:array of int
    :return: number of pairs
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))