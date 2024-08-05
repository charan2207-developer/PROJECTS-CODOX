import random
number = random.randint(1, 100)
print("Guess the number between 1 and 100!")
guess = int(input("Your guess: "))
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
elif guess==number :
    print("Congratulations! You guessed it!")

