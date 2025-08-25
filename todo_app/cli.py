# from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%b, %d, %Y, %H:%M:%S')
print("It is", now)

while True:
    commands = input('Type add, show, edit, complete or exit command with value: ')
    commands = commands.strip()

    if commands.startswith('add'):
        todo = commands[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif commands.startswith('show'):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f'{index + 1}. {todo}')
    elif commands.startswith('edit'):
        try:
            todos = functions.get_todos()

            edit_todo = int(commands[5:])

            edited_todo = input('Enter the new value: ') + '\n'
            todos[edit_todo - 1] = edited_todo

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid!')
            continue
    elif commands.startswith('complete'):
        try:
            todos = functions.get_todos()

            index = int(commands[9:]) - 1

            removed_todo = todos[index].strip()

            todos.remove(todos[index])

            functions.write_todos(todos)

            print(f'Todo: \'{removed_todo}\' is removed from the todos list.')
        except IndexError:
            print('There is no Item with that number.')
            continue
    elif commands.startswith('exit'):
        break
    else:
        print('Command is invalid!')

print('Bye!')