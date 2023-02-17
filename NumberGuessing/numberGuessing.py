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

def game():
    for turn in range(1, difficulty):
        print(f"Try number {turn}")
        if evaluate(valid_number()):
            break
    print(f"Game over! The number was {winner}")

play = True
while play:
    difficulty = 6
    winner: int = randint(1,100)
    game()
    x = input("Enter 0 to end, else it will continue.")
    if x != 0:
        play = False
    system('cls')

