def celsius_p_fahrenheit():
    while True:
        try:
            celsius = int(input("Enter the value of celsius: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    fahrenheit = celsius * 9/5 + 32
    print(f"This value in fahrenheit is: {fahrenheit}")
celsius_p_fahrenheit()

def fahrenheit_p_celsius():
    while True:
        try:
            fahrenheit = int(input("Enter the value of the fahrenheit: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    celsius = (fahrenheit - 32) * 5/9
    print(f"This value in celsius is: {celsius}")
fahrenheit_p_celsius()

def km_p_milhas():
    while True:
        try:
            km = int(input("Enter the value of the km: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    calc = km/8
    milhas = calc*5
    print(f"This value in miles is: {milhas}")
km_p_milhas()

def milhas_p_km():
    while True:
        try:
            milhas = int(input("Enter the value of the miles: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    km = milhas/5
    print(f"This value in km is: {km}")
milhas_p_km()

def kg_p_lb():
    while True:
        try:
            kg = int(input("Enter the value of the kg: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    calc = kg*2
    calc2 = calc*0.10
    lb = calc+calc2
    print(f"This value in lb: {lb}")
kg_p_lb()

def lb_p_kg():
    while True:
        try:
            lb = int(input("Enter the value of the lb: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    kg = lb/2.2
    print(f"This value in kg is: {kg}")
lb_p_kg()