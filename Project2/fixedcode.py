from random import randint

class GuessingGame:
    def __init__(self):
        self.secret_number = randint(1, 100)
        self.attempts = 0

    def start(self):
        print("--- Welcome to the Guessing Game! ---")
        print("Guess a number between 1 and 100 (or enter 0 to exit)")

        while True:
            try:
                user_guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            self.attempts += 1

            if user_guess == 0:
                print("Exiting the Guessing game. Goodbye!")
                break

            if user_guess > self.secret_number:
                print("Lower number please!")
            elif user_guess < self.secret_number:
                print("Higher number please!")
            else:
                print(f"Correct Guess: {user_guess}!")
                print(f"It took you {self.attempts} attempts.")
                break

if __name__ == "__main__":
    game = GuessingGame()
    game.start()