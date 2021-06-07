from random import randrange
import os

def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    lives = 3
    MIN = 0
    MAX = 25

    print("Welcome to Guess The Number!")
    print("The computer will use all its computational power to generate a")
    print(f"number between {MIN} and {MAX} (including).")
    print(f"You have {lives} lives. Best not to find out what happens when")
    print("you run out....")
    print("Good Luck!\n")

    chosen = randrange(MIN, MAX)

    checkGuess(MIN, MAX, lives, chosen)

def checkGuess(min, max, lives, chosen):
    print(f'Remaining Lives: {lives}')
    if lives == 0:
        print("No more lives left. You lose.")
        print(f"The number in question was {chosen}")
        quit()

    try:
        print("Please enter your guess: ")
        guess = int(input(""))
    except ValueError:
        print("You entered something that's not a number. Please stop doing that.\n")
        checkGuess(min, max, lives, chosen)

    if guess < min or guess > max:
        print(f"\nYou entered a number outside the range ({min}-{max}). Try again.\n")
        checkGuess(min, max, lives, chosen)

    while guess != chosen:
        if guess < chosen:
            lives -= 1
            print("\nGuess higher!\n")
            checkGuess(min, max, lives, chosen)
        elif guess > chosen:
            lives -= 1
            print("\nGuess lower!\n")
            checkGuess(min, max, lives, chosen)

    print("Winner Winner Chicken Dinner")
    print("Do you want to play again? You seem to be good at it. (y/n)")
    again = input("")
    if again == 'y' or again == 'ye' or again == 'yes':
        game()
    else:
        quit()


if __name__ == "__main__":
    game()
