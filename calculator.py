
def welcome():
    print("""
    WELCOME TO CALCULTOR
    Beep Boop + - * / Math JA """)

def calculate():
    operation = input("""
    Please type in the math operation you would like to complete
    + for addition
    - for subtraction
    * for multiplcation
    / for division
    ** for power
    % modulo
    exit to quit
    """)

    if operation == 'exit':
        quit 
    
    else:
        number_1 = float(input('Enter your first number: '))
        number_2 = float(input('Enter your second number: '))

        if operation == '+':    # Addition
            print('{} + {} = ' .format(number_1, number_2))
            print(number_1 + number_2)

        elif operation == '-':  # Substraction

            print('{} - {} = ' .format(number_1, number_2))
            print(number_1 - number_2)

        elif operation == '*':  # Multiplication
            print('{} * {} = ' .format(number_1, number_2))
            print(number_1 * number_2)
        
        elif operation == '/':  # Division
            print('{} / {} = ' .format(number_1, number_2))
            print(number_1 / number_2)

        elif operation == '**': # POWAHAHAH
            print('{} ** {} = ' .format(number_1, number_2))
            print(number_1 ** number_2)

        elif operation == '%': # Modulo
            print('{} % {} = ' .format(number_1, number_2))
            print(number_1 % number_2)

        else:
            print("You have not typed in a valid operator, please run the program again!")

welcome()
calculate()