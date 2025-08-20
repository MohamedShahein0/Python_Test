def add():
    while True:
        try:
            number1 = int(input('First number:   '))
            number2 = int(input('Second number:   '))
            answer = number1 + number2 
            print(answer)
            break
        except ValueError:
            print('Please enter valid numbers.')
        
def sub():
    while True:
        try:
            number1 = int(input('First number:   '))
            number2 = int(input('Second number:   '))
            answer = number1 - number2 
            print(answer)
            break
        except ValueError:
            print('Please enter valid numbers.')

def mult():
    while True:
        try:
            number1 = int(input('First number:   '))
            number2 = int(input('Second number:   '))
            answer = number1 * number2 
            print(answer)
            break
        except ValueError:
            print('Please enter valid numbers.')

def div():
    while True:
        try:
            number1 = int(input('First number:   '))
            number2 = int(input('Second number:   '))
            if number2 == 0:
                print("Cannot divide by zero.")
                continue
            answer = number1 / number2  
            print(answer)
            break
        except ValueError:
            print('Please enter valid numbers.')

def for_breaking():
    while True:
        ask = input('Do you want to continue (Y or N):   ').lower()
        if ask == 'y':
            return False 
        elif ask == 'n':
            print('Thanks for using.')
            return True  
        else:
            print('Please enter a valid response.')

while True:
    operator = input('Please choose Addition(A), Subtraction(S), Multiplacation(M) or Division(D):   ').lower()
    if operator == 'a':
        add()
    elif operator == 's':
        sub()
    elif operator == 'm':
        mult()
    elif operator == 'd':
        div()
    if for_breaking():
        break