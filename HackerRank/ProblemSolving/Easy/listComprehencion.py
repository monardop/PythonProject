"""
Let's learn about list comprehensions! 
You are given three integers  and  representing the dimensions of a cuboid 
long with an integer n. Print a list of all possible coordinates given by 
(i,j,k) on a 3D grid where the sum of  is not equal to . Here,
0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
Please use list comprehensions rather than multiple loops, 
as a learning exercise.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i, j, k = list(range(x+1)), list(range(y+1)), list(range(z+1))
    new_list = []
    # for a in i:
    #     for b in j:
    #         for c in k:
    #             if a + b + c != n:
    #                 new_list.append([a,b,c])
    list_comprehension = [[a,b,c] for a in i for b in j for c in k if (a+b+c) != n]
    print(list_comprehension)