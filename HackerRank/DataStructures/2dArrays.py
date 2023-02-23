# constraints: list's are 6x6
# need the max hourglass sum
def hourglassSum(arr: list):
    max_sum = [] # len: 16 int. 
    for i in range(4):
        for j in range(4):
            sumatoria = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            sumatoria += arr[i + 1][j + 1]
            sumatoria += arr[i+2][j] + arr[i+2][j + 1] + arr[i+2][j + 2]
            max_sum.append(sumatoria)
    return max(max_sum)

test_list  = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglassSum(test_list))