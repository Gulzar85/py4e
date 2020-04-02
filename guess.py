import random
number = random.randrange(1, 10)
attempts = 0
print('You have three attempts to guess the number!')
while attempts < 3:
    guess = int(input('Please enter your guess: '))
    attempts = attempts + 1
    if guess < number:
        print('too low...')
    elif guess > number:
        print('too hight...')
    elif guess == number:
        print('Good Job!')
        quit()
print('\nYou lost the game....')