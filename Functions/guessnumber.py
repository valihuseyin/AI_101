import random

def guess_number_game():
    number_to_guess = random.randint(1, 9)
    guesses_taken = 0

    print("I'm thinking of a number between 1 and 9. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses_taken += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {guesses_taken} tries.")
                break
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")

if __name__ == "__main__":
    guess_number_game()
    