def hurdleRace(k, height):
    height.sort()
    return  height[-1] - k if  height[-1] - k > 0 else 0