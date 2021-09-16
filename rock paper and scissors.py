import random

user_wins = 0
computer_wins = 0

option = ['rock', 'paper', 'scissors']

while True:
    user = input('ROCK , PAPER OR SCISSORS >>  ').lower

    random_number = random.randint(0, 2)
    computer = option[random_number]
    print('Computer Picked', computer + '.')

    if user == "rock" and computer == "scissor":
        print('you won')
        user_wins += 1

    elif user == 'paper' and computer == 'rock':
        print('you won')
        user_wins += 1

    elif user == 'scissor' and computer == "paper":
        print('you won')
        user_wins += 1

    else:
        print('hehe you lost')
        computer_wins += 1


