pin = input('введите пинкод: ')
if len(pin) == 4:
    if pin.isdigit():
        print(1)
    else:
        print(0)
else:
    print(0)




