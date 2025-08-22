while True:
    user_action = input('Type \'add\', \'show\', \'edit\', \'complete\', or \'exit\': ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('./todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
        case 'edit':
            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
            print('Choose a the number you want to edit!')
            to_edit = int(input('>> '))
            edited = input('New value: ')
            todos[to_edit-1] = edited
        case 'complete':
            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
            print('Choose a number that you completed!')
            todo_completed = int(input('>> '))
            todos.pop(todo_completed-1)
        case 'exit':
            break
        case _:
            print('Hey, you\'ve entered an unknown command.')

print('Bye')