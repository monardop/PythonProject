def miniMaxSum(arr):
    # Write your code here
    size_arr = len(arr)

    # Busco max
    max_sum = 0
    for i in range(size_arr):
        total_sum = 0
        for x in range(size_arr):
            if x == i:
                total_sum += 0
            else:
                total_sum += arr[x]
        if total_sum > max_sum:
            max_sum = total_sum

    min_sum = max_sum    
    for i in range(size_arr):
        total_sum = 0
        for x in range(size_arr):
            if x == i:
                total_sum += 0
            else:
                total_sum += arr[x]
        if total_sum < min_sum:
            min_sum = total_sum
    
    print(f"{min_sum} {max_sum}")
        

miniMaxSum([1,2,3,4,5])