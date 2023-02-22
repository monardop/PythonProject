def sockMerchant(n, ar) -> int:
    """
    :param n: socks in the pile
    :param ar: colors of each sock
    :return: number of pairs
    """
    pairs = {}
    for pair in ar:
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    ans = 0
    for amount in pairs.values():
        ans += amount // 2
    return ans
