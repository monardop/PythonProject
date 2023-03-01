import quartiles

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    new_array = []
    for pos, value in enumerate(values):
        for n in range(freqs[pos]):
            new_array.append(value)
    new_array.sort()
    ans = quartiles.quartiles(new_array)
    return round(float(ans[2] - ans[0]), 1)


if __name__ == '__main__':
    a = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
    print(interQuartile(a,b))