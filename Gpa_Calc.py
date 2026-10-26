import time
grades = 0
total_points = 0
print('Welcome to your personal GPA calculator for school!')
time.sleep(1)
print('When you have put all of your grades type "Done"')
time.sleep(1)
print('You will need to type each grade one by one not all of them on one line')
classes = int(input('Enter how many classes you have: '))
while True:
    grades = input('Enter grade: ').upper()
    if grades == 'DONE':
        break
    if grades == 'A':
        total_points += 4
    elif grades == 'B':
        total_points += 3
    elif grades == 'C':
        total_points += 2
    elif grades == 'D':
        total_points += 1
    elif grades == 'F':
        total_points += 0
calculate = total_points/classes
print(f'Your gpa is {calculate}')







