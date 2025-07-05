"""
Write a Python program that simulates a
handheld calculator. Your program should
process input from the Python console
representing buttons that are "pushed",
and then output the contents of the screen
after each operation is performed. Minimally,
your calculator should be able to process
the basic arithmetic operations and a
reset/clear operation.
"""

def handheld_calc():
    """Creating a handheld calculator.

    Variables;

    screen       displays the user input
    button       takes input from the user
    result       stores the result after the arithmetic operation
    expression   stores the expression
    """
    screen = ''
    button = ''
    result = 0
    expression = ''

    while True:
        button = input('button: ')
        if button.upper() == 'C':    # clears the expresion, result, and screen if true
            screen = ''
            result = 0
            expression = ''
        
        if button.upper() == 'Q':    # exits the program
            print('Closing handheld calculator')
            quit()

        if len(button) == 1:         # The button input will be of length 1
            if button in '1234567890.+*/-':    # the input should be from '1234567890.+x/-'
                expression += button           # each button entered by the user will be concatenated to the expression
                screen = expression            # the screen will reference the expression
                print('Screen:', screen)       # and print it to the screen
                continue

        if button == '=':
            try:                               # Checking for error
                result = eval(expression)      # calculate the expression and apply the arithmetic operation
                screen = str(result)           # store the result as string in the screen variable
                expression = str(result)       # store the result as string in expression variable
                print('Screen:', screen)       # print the result to the screen
            except:                            # if error found
                screen = 'Error'               # screen will store the value 'Error'
                expression = ''                # Expression will be ''
                print(screen)                  # print the error to the screen
                continue



if __name__ == '__main__':
    handheld_calc()        # function execution
