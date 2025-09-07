brake = False
while True:
    if brake:
        break
    try:
        num = int(input('Choose a number to generate a multiplacation table:   '))
        mult = 1
        while True:
            if brake:
                break
            print(f'{num} X {mult} = {num * mult}')
            mult += 1
            if mult == 11:
                break
        while True:
            ask = input('Do you want to enter a new number(Y or N):   ').lower()
            if ask == 'y':
                break
            elif ask == 'n':
                print('Thanks for trying.')
                brake = True
                break
            else:
                print('Please enter (Y or N).')
    except ValueError:
        print('please enter a integer.')