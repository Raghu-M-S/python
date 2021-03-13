import random
import os

def game():
    number = random.randint(0,500)
    tries = 1
    done = False

    while not done:
        guess = int(input("enter your guess: "))

        if guess == number:
            done = True
            print("You Won!!!")
        else:
            tries+=1
            if guess > number:
                print('actual nunmber is smaller')
            else:
                print("actual number is greater")

    print(f"You used {tries} tries")
game()



