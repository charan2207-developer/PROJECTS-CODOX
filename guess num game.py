import random
number = random.randint(1, 15)
print("Guess the number between 1 and 15!")
x = int(input("Your guess: "))
if x < number:
    print("Too low!")
elif x > number:
    print("Too high!")
elif x == number:
    print("Congratulations! You guessed it!")

