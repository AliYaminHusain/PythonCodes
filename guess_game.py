import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('guess a number between 1 and 10 >> '))
        if guess < random_number:
            print('Bit low , guess again')
        elif guess > random_number:
            print('Bit high , guess again')

    print(  "yay you guessed the correct number")

guess(10)
