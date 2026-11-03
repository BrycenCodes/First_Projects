import random
import time
tally = 0
print('Welcome to your mental math practice!')
time.sleep(1)
print('Made by yours truly.. Brycen!')
while True:
        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)
        calculate = int(input(f'{first_number} + {second_number} = : '))
        if calculate == first_number + second_number:
            print('Good job!')
            tally += 1
            print(f'Streak : {tally}')
            continue
        else:
            time.sleep(1)
            print('Wrong')
            tally = 0
            print(f'Streak : {tally}')
            continue
