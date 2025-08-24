todolist = []

import os

file_path = os.path.join(os.path.dirname(__file__), "todolist.txt")

try:
    with open(file_path, 'r') as file:
        for line in file:
            todolist.append(line.strip())
except FileNotFoundError:
    pass

def save_tasks():
    with open(file_path, 'w')as file:
        for task in todolist:
            file.write(task + '\n')

while True:
    ask = input('\nWhat do you want to do:\n1.Add task\n2.View\n3.Remove task\n4.Quit\n50.Remove all tasks\n--->   ')
    if ask == '1':
        new_task = input('What do you want to add:   ')
        todolist.append(new_task)
        save_tasks()
    elif ask == '2':
        for i, task in enumerate(todolist, 1):
            print(f"{i}. {task}")
    elif ask == '3':
        if not todolist:
            print('The to do list is empty please add a task first.')
        else:
            for i, task in enumerate(todolist, 1):
                print(f"{i}. {task}")
            while True:
                try:
                    remove = int(input('What number do you want to remove:   '))
                    if remove > 0:
                        todolist.pop(remove - 1)
                        break
                    elif remove == 0:
                        print('Please enter a number bigger than 0.')
                except ValueError:
                    print('Please enter a valid number.')
                except IndexError:
                    print('Please enter a number in the list.')
        save_tasks()
    elif ask == '4':
        save_tasks()
        break
    elif ask == '50':
        confirm = input('Are you sure you want to remove all tasks? (Y/N): ').lower()
        if confirm == 'y':
            todolist.clear()
            save_tasks()
            print('All tasks removed')
        elif confirm == 'n':
            pass
    else:
        print('Please enter 1, 2, 3, 4 or 50')