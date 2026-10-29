import time
history = []
print('Hello!')
time.sleep(1)
def name():
    name1 = input('Your name?: ')
    time.sleep(1)
    birthday = input('Birthday?: ')
    return name1, birthday
while True:
    info = name()
    history.append(info)
    time.sleep(1)
    print(f"{info[0]},{info[1]}")
    time.sleep(1)
    choice = input('Do you wish to be done? (Yes/No): ')
    if choice == 'Yes':
        break
    else:
        continue







