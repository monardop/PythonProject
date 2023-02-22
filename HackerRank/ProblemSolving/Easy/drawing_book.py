def pageCount(n, p):
    """
    :param n: number of pages
    :param p: page wanted
    """
    counter = [0,0]
    if n % 2 == 0:
        n += 1
    for i in range(0, n, 2):
        if p in [i, i+1]:
            break
        else:
            counter[0] += 1
    for i in range(n, 0, -2):
        if p in [i -1, i]:
            break
        else:
            counter[1] += 1
    return min(counter)

print(pageCount(6,4))