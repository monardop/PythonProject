def staircase(n):
    # Write your code here
    spaces = ' '
    tag = '#'
    for line in range(n):
        print(spaces * ((n - 1) - line) + tag * (1 + line))


# Insert a number here
staircase()
