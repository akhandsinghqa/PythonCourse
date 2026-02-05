# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module
from random import randint


class GuessingGame:
    num = randint(1, 100)

    attempt = 0
    inputnum = 1
    while inputnum != 0:
        inputnum = int(input("Enter your guess number :"))
        attempt += 1
        if inputnum == 0:
            print("Exiting the Guessing game !!!!!!!!")
            break
        elif inputnum > num:
            print("Lower number please ! or enter 0 to exit.")
        elif inputnum < num:
            print("Higher number please ! or enter 0 to exit")
        elif inputnum == num:
            print(f"Correct Guess : {inputnum} \tTotal number of guesses : {attempt}")
            inputnum = 0
