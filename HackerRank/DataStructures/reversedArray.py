def builtin_method(arr: list):
    return reversed(arr)

def own_reversed(arr: list) -> list:
    new_array = []
    for n in range(-1, - len(arr) - 1, -1):
        new_array.append(arr[n])
    return new_array

def other_option(arr: list) -> list:
    new_array = []
    for _ in range(len(arr)):
        new_array.append(arr.pop())
    return new_array

print(own_reversed([1,2,3,4]))
print(other_option([1,2,3,4]))