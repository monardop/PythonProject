# How many handshakes do I need.
# This function accepts an int, returns an int

def handshake(n: int):
    count = 0
    for x in range(n):
        n -= 1
        count += n
    return count


print(handshake(10))