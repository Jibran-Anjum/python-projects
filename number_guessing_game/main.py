import random

guess_val = random.randint(0, 9)
count = 0

while True:
    guess = int(input('Enter your guess: '))
    count += 1
    if guess == guess_val:
        break
    elif guess > 9 or guess < 0:
        print('Wrong input try again')
        print('And remember, that the value is between 0 and 9, and make sure that the input is integer type')
    elif guess < guess_val:
        print('Too low\nTry again!')
    elif guess > guess_val:
        print('Too high\nTry again!')

print('Number of Attempts:', count)
print('Congrats')
