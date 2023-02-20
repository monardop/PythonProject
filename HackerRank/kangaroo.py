def kangaroo(x1, v1, x2, v2):

    for n in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
    
    return "NO"
    