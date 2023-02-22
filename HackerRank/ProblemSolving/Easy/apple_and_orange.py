def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    """
    :param s: integer, starting point of Sam's house location.
    :param t: integer, ending location of Sam's house location.
    :param a: integer, location of the Apple tree.
    :param b: integer, location of the Orange tree.
    :param apples: integer array, distances at which each apple falls from the tree.
    :param oranges: integer array, distances at which each orange falls from the tree.
    """
    print(len(list(filter(lambda x: (s-a) <= x <= (t-a), apples))))
    print(len(list(filter(lambda x: (s-b) <= x <= (t-b), oranges))))