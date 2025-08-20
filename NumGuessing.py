import random
job = False
def easy():
    bob = False
    while True:
        if bob == True:
            break
        ez = random.randint(1, 10)
        ask = int(input('Choose the first number:   '))
        while True:
            if ask < ez:
                ask = int(input('The number is greater:   '))
            elif ask > ez:
                ask = int(input('The number is smaller:   '))
            elif ask == ez:
                print('Correct the number was', ez)
                bob = True
                break

def medium():
    bob = False
    while True:
        if bob == True:
            break
        med = random.randint(1, 100)
        ask = int(input('Choose the first number:   '))
        while True:
            if ask < med:
                ask = int(input('The number is greater:   '))
            elif ask > med:
                ask = int(input('The number is smaller:   '))
            elif ask == med:
                print('Correct the number was', med)
                bob = True
                break

def hard():
    bob = False
    while True:
        if bob == True:
            break
        har = random.randint(1, 1000)
        ask = int(input('Choose the first number:   '))
        while True:
            if ask < har:
                ask = int(input('The number is greater:   '))
            elif ask > har:
                ask = int(input('The number is smaller:   '))
            elif ask == har:
                print('Correct the number was', har)
                bob = True
                break


while True:
    if job == True:
        break
    choice = input('Choose easy(E), medium(M), hard(H):   ').lower()
    if choice == 'e':
        easy()
        while True:
            cont = input('Do you want to continue(Y or N):   ').lower()
            if cont == 'y':
                continue
            elif cont == 'n':
                print('Thanks for playing!!')
                job = True
                break
            else:
                print('Please enter a valid response.')
    elif choice == 'm':
        medium()
        while True:
            cont = input('Do you want to continue(Y or N):   ').lower()
            if cont == 'y':
                continue
            elif cont == 'n':
                print('Thanks for playing!!')
                job = True
                break
            else:
                print('Please enter a valid response.')
    elif choice == 'h':
        hard()
        while True:
            cont = input('Do you want to continue(Y or N):   ').lower()
            if cont == 'y':
                continue
            elif cont == 'n':
                print('Thanks for playing!!')
                job = True
                break
            else:
                print('Please enter a valid response.')
    else:
        print('Please Enter E, M, or H')