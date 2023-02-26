def mean() -> float:
    return round(sum(array)/n, 1)


def median() -> float:
    if n % 2 == 0:
        return round((array[n//2] + array[(n//2) - 1]) / 2, 1)
    else:
        index = int(round(n//2, 0))
        return array[index]


def mode() -> int:
    repetitions = {}
    # First, count each number appears
    for element in array:
        if element in repetitions:
            repetitions[element] += 1
        else:
            repetitions[element] = 1
    # now, i get a list
    key_list = [n for n in repetitions.keys()]
    appear_list = [n for n in repetitions.values()]

    index = appear_list.index(max(appear_list))
    return key_list[index]


n = int(input())
array = input().split()
array = list(map(lambda x: int(x), array))
array.sort()
print(mean())
print(median())
print(mode())
