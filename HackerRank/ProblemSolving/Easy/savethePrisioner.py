"""
A jail has a number of prisoners and a number of treats to pass out to them. 
Their jailer decides the fairest way to divide the treats is to seat the 
prisoners around a circular table in sequentially numbered chairs. 
A chair number will be drawn from a hat. Beginning with the prisoner in that 
chair, one candy will be handed to each prisoner sequentially around the 
table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks 
like all the others, but it tastes awful. Determine the chair number 
occupied by the prisoner who will receive that candy.
"""
def saveThePrisoner(n: int, m: int, s: int) -> int:
    """
    :param n: number of prisioners
    :param m: number of sweets
    :param s: the chair number to begin

    :return: chair number of prisioner to warn
    """
    return (m - 1  + s - 1 ) % n + 1

print(saveThePrisoner(7, 19, 2)) # 6
print(saveThePrisoner(3, 7, 3)) # 3
