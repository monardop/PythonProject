"""
Luke is daydreaming in Math class. He has a sheet of graph paper with n rows 
and m columns, and he imagines that there is an army base in each cell for a 
n.m total of  bases. He wants to drop supplies at strategic points on the sheet, 
marking each drop point with a red dot. If a base contains at least one package
inside or on top of its border fence, then it's considered to be supplied.
"""
from math import ceil

def gameWithCells(n, m):
    a = ceil(n/2)
    b = ceil(m/2)
    return (a*b)


print(gameWithCells(70,123))