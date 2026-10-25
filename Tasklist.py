 import time
print('Welcome to your task list!')
time.sleep(1)
print('We will do everything for you and make a txt file with your tasks!')
time.sleep(1)
print('Type "Done" to end')
time.sleep(1)
with open('tasks.txt', 'a') as file:
 while True:
  task = input('Enter task: ')
  if task == 'Done':
   break
  file.write(task + '\n')
print('Done! Check for file "tasks.txt" ')
