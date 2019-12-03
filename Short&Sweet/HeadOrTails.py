import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if guess == 'heads':
    guess = 1
else:
    guess = 0
logging.debug('Start of factorial(%s%%)'  % (toss))

while True:
    if toss == guess:
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
        guess = input()
        if guess == 'heads':
            guess = 1
        else:
            guess = 0
        if toss == guess:
            print('You got it!')
            break
        else:
            print('Nope. You are really bad at this game.')
            break