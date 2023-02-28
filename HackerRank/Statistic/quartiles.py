def median(arr):
    if len(arr)%2 == 0:
        mean = (arr[len(arr)//2 -1] + arr[len(arr)//2]) / 2
        return mean, [[n for n in arr if n < mean], [n for n in arr if n > mean]]
    else:
        new_len = len(arr)//2
        return arr[new_len], [arr[0:new_len], arr[new_len + 1:]]


def quartiles(arr) -> list[int]:
    arr.sort()
    q2, new_group = median(arr)
    q1, quartile_1_2 = median(new_group[0])
    q3, quartile_3_4 = median(new_group[1])
    return [int(q1), int(q2), int(q3)]

print(quartiles([9,5,7,1,3]))