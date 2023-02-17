from random import randint
from os import system


def evaluate(number: int) -> bool:
    if number == winner:
        print("Congrats!")
        return True
    elif abs(number - winner) > 20:
        print("Way too far")
        return False
    elif 20 > abs(number - winner) > 5:
        print("Almost there")
        return False
    else: 
        print("Close enought")
        return False

def valid_number() -> int:
    while True:
        try:
            x = int(input("Guess the number: "))
        except ValueError:
            print("Wrong entry, try again.")
        else:
            return x

def game(tries: int):
    for turn in range(1, tries):
        print(f"Try number {turn}")
        if evaluate(valid_number()):
            break
    print(f"Game over! The number was {winner}")

def set_difficulty() -> tuple:
    difficulty = ((5, 10), (10,50), (5,50), (10,100), (5,100))
    print("Select your level:")
    print("0 - Very Easy (5 attempts, 1->10)")
    print("1 - Easy (10 attempts, 1->50)")
    print("2 - Medium(5 attempts, 1->50)")
    print("3 - Hard(10 attempts, 1->100)")
    print("4 - Very Hard(5 attempts, 1->100)")
    
    level = 0
    while True:
        try:
            level = int(input("Choose: "))
            if 0 > level > 4:
                raise ValueError
        except ValueError:
            print("Wrong entry")
        else:
            break
    return difficulty[level]

play = True
while play:
    difficulty = set_difficulty()
    winner: int = randint(1,difficulty[1])
    game(difficulty[0])
    x = input("Enter 0 to end, else it will continue.")
    if x != 0:
        play = False
    system('cls')

