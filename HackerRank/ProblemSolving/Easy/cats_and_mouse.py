def catAndMouse(x, y, z):
    diff1 = abs(z-x)
    diff2 = abs(y-x)
    if diff1 == diff2:
        return "Mouse C"
    elif diff1 > diff2:
        return "Cat B"
    else:
        return "Cat A"