def filter_function(a: list, b: list,candidate: int) -> bool:
    for n in a:
        if candidate % n !=0:
            return False
    for n in b:
        if n % candidate != 0:
            return False
    return True

def getTotalX(a: list, b: list) -> int:
    count = 0
    for number in range(max(a), min(b) + 1):
        if filter_function(a, b, number):
            count += 1
    return count


    
