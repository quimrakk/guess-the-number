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
    multiplier = randrange(1, 5)
    if chosen % 2 == 0:
        divisible2 = True
    else:
        divisible2 = False
    if chosen % 3 == 0:
        divisible3 = True
    else:
        divisible3 = False
    multiple = chosen * multiplier


    checkGuess(MIN, MAX, lives, chosen, divisible2, divisible3, multiple)

def checkGuess(min, max, lives, chosen, divisible2, divisible3, multiple):
    if lives == 3:
        if divisible2:
            print("Hint: Our number is divisible by 2\n")
        else:
            print("Hint: Our number is NOT divisible by 2\n")
    if lives == 2:
        if divisible3:
            print("Hint: Our number is divisible by 3\n")
        else:
            print("Hint: Our number is NOT divisible by 3\n")
    if lives == 1:
        print(f'{multiple} is a multiple of our number')

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
        checkGuess(min, max, lives, chosen, divisible2, divisible3, multiple)

    if guess < min or guess > max:
        print(f"\nYou entered a number outside the range ({min}-{max}). Try again.\n")
        checkGuess(min, max, lives, chosen, divisible2, divisible3, multiple)

    while guess != chosen:
        if guess < chosen:
            lives -= 1
            print("\nGuess higher!\n")
            checkGuess(min, max, lives, chosen, divisible2, divisible3, multiple)
        elif guess > chosen:
            lives -= 1
            print("\nGuess lower!\n")
            checkGuess(min, max, lives, chosen, divisible2, divisible3, multiple)

    print("\nWinner Winner Chicken Dinner")
    print("Do you want to play again? You seem to be good at it. (y/n)")
    again = input("")
    if again == 'y' or again == 'ye' or again == 'yes':
        game()
    else:
        quit()


if __name__ == "__main__":
    game()
