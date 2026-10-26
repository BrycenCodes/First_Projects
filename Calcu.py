operation = 0
import time
print('Welcome to calc')
time.sleep(1)
print('Operations means how many signs for ex: (1+1) = 1 operation (1+1+1) = 2 operations, etc ')
time.sleep(1)
print('+')
print('-')
print('*')
print('/')
operation_pick = input('What operation would you like to do? (+,-,*,/): ')
operation_number = input('How many operations? (1-4): ')
if operation_number == '1' and operation_pick == '+':
    operation = 1
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    calculate = first_number + second_number
    print(f'{first_number} + {second_number} = {calculate}')
elif operation_number == '2' and operation_pick == '+':
    operation = 2
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    calculate = first_number + second_number + third_number
    print(f'{first_number} + {second_number} + {third_number} = {calculate}')
elif operation_number == '3' and operation_pick == '+':
    operation = 3
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    calculate = first_number + second_number + third_number + forth_number
    print(f'{first_number} + {second_number} + {third_number} + {forth_number} = {calculate}')
elif operation_number == '4' and operation_pick == '+':
    operation = 4
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    fifth_number = int(input('Fifth number?: '))
    calculate = first_number + second_number + third_number + forth_number + fifth_number
    print(f'{first_number} + {second_number} + {third_number} + {forth_number} + {fifth_number} = {calculate}')
if operation_number == '1' and operation_pick == '-':
    operation = 1
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    calculate = first_number - second_number
    print(f'{first_number} - {second_number} = {calculate}')
elif operation_number == '2' and operation_pick == '-':
    operation = 2
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    calculate = first_number - second_number - third_number
    print(f'{first_number} - {second_number} - {third_number} = {calculate}')
elif operation_number == '3' and operation_pick == '-':
    operation = 3
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    calculate = first_number - second_number - third_number - forth_number
    print(f'{first_number} - {second_number} - {third_number} - {forth_number} = {calculate}')
elif operation_number == '4' and operation_pick == '-':
    operation = 4
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    fifth_number = int(input('Fifth number?: '))
    calculate = first_number - second_number - third_number - forth_number - fifth_number
    print(f'{first_number} - {second_number} - {third_number} - {forth_number} - {fifth_number} = {calculate}')
if operation_number == '1' and operation_pick == '*':
    operation = 1
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    calculate = first_number * second_number
    print(f'{first_number} * {second_number} = {calculate}')
elif operation_number == '2' and operation_pick == '*':
    operation = 2
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    calculate = first_number * second_number * third_number
    print(f'{first_number} * {second_number} * {third_number} = {calculate}')
elif operation_number == '3' and operation_pick == '*':
    operation = 3
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    calculate = first_number * second_number * third_number * forth_number
    print(f'{first_number} * {second_number} * {third_number} * {forth_number} = {calculate}')
elif operation_number == '4' and operation_pick == '*':
    operation = 4
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    fifth_number = int(input('Fifth number?: '))
    calculate = first_number * second_number * third_number * forth_number * fifth_number
    print(f'{first_number} * {second_number} * {third_number} * {forth_number} * {fifth_number} = {calculate}')
if operation_number == '1' and operation_pick == '/':
    operation = 1
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    calculate = first_number / second_number
    print(f'{first_number} / {second_number} = {calculate}')
elif operation_number == '2' and operation_pick == '/':
    operation = 2
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    calculate = first_number / second_number / third_number
    print(f'{first_number} / {second_number} / {third_number} = {calculate}')
elif operation_number == '3' and operation_pick == '/':
    operation = 3
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    calculate = first_number / second_number / third_number / forth_number
    print(f'{first_number} / {second_number} / {third_number} / {forth_number} = {calculate}')
elif operation_number == '4' and operation_pick == '/':
    operation = 4
    first_number = int(input('First number?: '))
    second_number = int(input('Second number?: '))
    third_number = int(input('Third number?: '))
    forth_number = int(input('Forth number?: '))
    fifth_number = int(input('Fifth number?: '))
    calculate = first_number / second_number / third_number / forth_number / fifth_number
    print(f'{first_number} / {second_number} / {third_number} / {forth_number} / {fifth_number} = {calculate}')

