pin = input("Type a the pin: ")

if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
    print(True)
else:
    print(False)