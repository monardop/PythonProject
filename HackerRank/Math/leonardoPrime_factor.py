def primeCount(n: int):
    # Write your code here
    prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    product = 1
    count = 0
    for number in prime:
        product *= number
        if product <= n:
            count +=1
        else:
            return count

print(primeCount(100))
