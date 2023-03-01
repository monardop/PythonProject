"""
Cual es la probabilidad de que, tirando dos dados, 
la suma de sus caras sea menor o igual que 9
"""

def ej1():
    dice1 = list(range(1,7))
    dice2 = list(range(1,7))

    posibilidades = []
    for x in dice1:
        for y in dice2:
            posibilidades.append(x+y)

    print(
        "De",len(posibilidades), "posibilidades,", 
        len([n for n in posibilidades if n <= 9]), "cumplen")

    p =  len([n for n in posibilidades if n <= 9]) / len(posibilidades) 
    print(p)


def ej2():
    dice1 = list(range(1,7))
    dice2 = list(range(1,7))

    posibilidades = []
    for x in dice1:
        for y in dice2:
            posibilidades.append(x+y)

    print(
        "De",len(posibilidades), "posibilidades,", 
        len([n for n in posibilidades if n == 6 ]), "cumplen")

    p =  len([n for n in posibilidades if n == 6]) / len(posibilidades) 
    print(p)

ej2()