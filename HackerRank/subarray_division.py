"""
S es el numero correspondiente a cada elemento
m es los sub grupos que puedo hacer 
d es la suma total del subgrupo para que cuente
"""

def birthday(s: list, d: int, m: int):
    options = 0
    for i in range(len(s) - (m - 1)):
        total = 0
        try: 
            for j in range(m):
                total += s[i + j]
            if total == d:
                options += 1
        except IndexError:
            break;
    return options

print(birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1],18, 7)) # 3