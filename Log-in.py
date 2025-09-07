log_info = []

import os

file_path = os.path.join(os.path.dirname(__file__), "log_info.txt")

try:
    with open(file_path, 'r') as file:
        for line in file:
            name, email, password = line.strip().split(',')
            log_info.append({"name": name, "email": email, "password": password})
except FileNotFoundError:
    pass

def save_account():
    with open(file_path, 'w') as file:
        for account in log_info:
            file.write(f"{account['name']},{account['email']},{account['password']}\n")

while True:
    choice = input('1.Make account\n2.Log in\n3.Exit\n---->   ')
    if choice == '1':
        fullb = False
        while True:
            if fullb:
                break
            account = {}
            account['name'] = input('Please enter your name:   ').strip()
            account['email'] = input('Please enter your email:   ').strip()
            account['password'] = input('Please enter your password:   ').strip()
            log_info.append(account)
            save_account()
            while True:
                ask = input('Do you want to add an other account(Y or N):   ').lower()
                if ask == 'y':
                    break
                elif ask == 'n':
                    fullb = True
                    break
                else:
                    print('Please enter a valid input.')
    elif choice == '2':
        found = False
        fullb1 = False
        fullb2 = False
        fullb3 = False
        while True:
            if fullb2:
                break
            elif fullb3:
                break
            entered_email = input('Enter your email:   ')
            entered_password = input('Enter your password:   ')
            for account in log_info:
                if fullb1:
                    break
                elif account['email'] == entered_email and account['password'] == entered_password:
                    found = True
                    break
                elif account['email'] == entered_email and account['password'] != entered_password:
                    print('Wrong password.')
                    while True:
                        try_again1 = input('Do you want to try again(Y or N):   ').lower()
                        if try_again1 == 'y':
                            break
                        elif try_again1 == 'n':
                            fullb1 = True
                            fullb2 = True
                            break
                        else:
                            print('Please eneter a valid input.')
            if found:
                print('Logged in!')
                break
            elif not found:
                print('Account not found')
                while True:
                    try_again3 = input('Do you want to try again(Y or N):   ').lower()
                    if try_again3 == 'y':
                        break
                    elif try_again3 == 'n':
                        fullb3 = True
                        break
                    else:
                        print('Please eneter a valid input.')
    elif choice == '3':
        print('Exiting.')
        save_account()
        break
    else:
        print('Please eneter a valid input.')
    