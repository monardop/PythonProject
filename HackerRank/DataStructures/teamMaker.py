from os import system
from random import randint


def pos_correcta():
    while True:
        try:
            posicion = int(input("Posicion: "))
            if 0 > posicion or posicion > 2:
                raise ValueError
        except ValueError:
            print("Nop")
        else:
            return posicion


def get_players(cant_jugadores: int) -> list:
    jugadores = [[], [], []]
    print("Se ingresa nombre, enter. Luego 0 arq, 1 def, 2 atk")
    for _ in range(cant_jugadores):
        nombre = input("Nombre: ")
        posicion = pos_correcta()
        if posicion == 0 and len(jugadores[0]) == 2:
            print("No hay mas cupo de arqueros")
            posicion = pos_correcta()
        jugadores[posicion].append(nombre)
    return jugadores


def correccion_equipos(equipos:list):
    if flag:
        if len(equipos[0]) > len(equipos[1]):
            diferencia = len(equipos[0]) - len(equipos[1])
            for n in range(diferencia):
                jugador = equipos[0][randint(0,len(equipos[0]))]
                equipos[1].append(jugador)
                equipos[0].remove(jugador)
        elif len(equipos[0]) < len(equipos[1]):
            diferencia = len(equipos[1]) - len(equipos[0])
            for n in range(diferencia):
                jugador = equipos[1][randint(0,len(equipos[1]))]
                equipos[0].append(jugador)
                equipos[1].remove(jugador)
    else:
        if len(equipos[0]) > len(equipos[1]) and len(equipos[0]) > tam_cancha:
            diferencia = len(equipos[0]) - tam_cancha
            for n in range(diferencia):
                jugador = equipos[0][randint(0,len(equipos[0]))]
                equipos[1].append(jugador)
                equipos[0].remove(jugador)
        elif len(equipos[0]) < len(equipos[1]) and len(equipos[0]) > tam_cancha:
            diferencia = len(equipos[1]) - tam_cancha
            for n in range(diferencia):
                jugador = equipos[1][randint(0,len(equipos[1]))]
                equipos[0].append(jugador)
                equipos[1].remove(jugador)
    
    return equipos

def set_teams(defensor:list, delantero:list):
    equipos = [[], []]
    for n in range(defensor):
        jugador = defensor.pop()
        if n % 2 == 0:
            equipos[0].append(jugador)
        else:
            equipos[1].append(jugador)

    for n in range(delantero):
        jugador = defensor.pop()
        if n%2 != 0:
            equipos[0].append(jugador)
        else:
            equipos[1].append(jugador)
    
    # correccion 
    equipos = correccion_equipos(equipos)
    
    return equipos


def mostrar_equipos(equipo: list, arqueros: list):
    print("Arqueros: ", arqueros)
    print("Equipo 1:", equipo[0])
    print("Equipo 2:", equipo[1])




tam_cancha = int(input("Tamaño cancha: "))
glk, deff, atk = get_players(tam_cancha*2)
system('cls')
flag = False
if len(glk) != 2:
    flag = True
while True:
    equ = set_teams(deff, atk)
    mostrar_equipos(equ, glk)
    option = input("0 para finalizar")
    if option == 0 or option == '0':
        break

