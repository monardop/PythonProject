def average(arr: list[int]) -> float:
    return sum(arr)/len(arr)

def stdDev(arr: list[int]) -> float:
    # Print your answers to 1 decimal place within this function
    o = average(arr)
    values = list(map(lambda x: (x - o)**2, arr))
    return round(sum(values)/len(arr),1)
