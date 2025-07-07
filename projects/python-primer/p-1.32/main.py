"""
Write a python program that can simulate a simple
calculator, using the console as the exclusive
input and output device. That is, each input to
the calculator, be it a number, like 12.34 or
1034, or an operator, like + or =, can be done on
a seperate line. After each such input, you should
output to the python console what would be
displayed on your calculator.
"""


def calculator():
    """Calculator that takes input line by line.
    
    It displays the output after every operation.
    """
    print('Type \'C\' to clear, type \'Q\' to quit')
    operator = ''
    result = 0

    while True:
        input_values = input('>> ')    # Takes user input

        if result == 0 and input_values.isnumeric():    # Check if the result is 0 and the input is numeric
            result = float(input_values)    # result will hold the initial value if it's empty

        elif input_values == '+' or input_values == '-' or input_values == '/' or input_values == 'x' or input_values == '=':    # Check if the input is any of the operators

            operator = input_values                 # operator will hold the operator that is given or input by the user
            input_values = input('>> ')             # ask for user input
            if operator == '+':                     # if operator is '+' then addition will take place
                result += float(input_values)
            elif operator == '-':                   # if operator is '-' then subtraction will take place
                result -= float(input_values)
            elif operator == '/':                   # if operator is '/' then division will take place
                result /= float(input_values)
            elif operator == 'x':                   # if operator is 'x' then multiplication will take place
                result *= float(input_values)
            elif operator == '=':                   # if operator is '=' then the result will be printed
                print(f'Display: {result}')
                continue

        elif input_values.upper() == 'Q':           # if the input value is 'Q' then exit the calculator
            print('Exiting Calculator.')
            quit()
        elif input_values.upper() == 'C':           # if the input value is 'C' then clear the result
            result = 0
        else:
            print('Invalid input!')

        print(f'Display: {result}')                 # display the result
    


if __name__ == '__main__':
    """Function Execution."""
    calculator()
