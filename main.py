import random
from time import sleep

low = 0
high = 50

def gameLoop(low, high):
    lives = 3
    num = random.randrange(low, high)
    while lives != 0:
        try:
            guess = int(input("\n"))
        except ValueError:
            continue

        if guess == num:
            print("Winner")
            break
        else:
            lives -= 1
            if guess < num:
                print("Too low.")
            elif guess > num:
                print("Too high.")

if __name__ == '__main__':
    gameLoop(low, high)
