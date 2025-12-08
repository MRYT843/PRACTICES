import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    guess = int(input("Enter your guess (1–100): "))

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"🎉 Correct! The number was {number}.")
        print(f"You guessed it in {attempts} tries.")
        break
