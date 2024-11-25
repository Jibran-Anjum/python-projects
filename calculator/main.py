val_1 = float(input('Value 1: '))
val_2 = float(input('Value 2: '))

op = input('Operation (+, -, x, /): ')

def add(val_1, val_2):
    return val_1 + val_2

def sub(val_1, val_2):
    return val_1 - val_2

def mult(val_1, val_2):
    return val_1 * val_2

def div(val_1, val_2):
    return val_1 / val_2

if op == '+':
    print(add(val_1, val_2))
elif op == '-':
    print(sub(val_1, val_2))
elif op == 'x':
    print(mult(val_1, val_2))
elif op == '/':
    print(div(val_1, val_2))
