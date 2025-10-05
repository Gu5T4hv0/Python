def converter(valor, de, para):
    currency = {
        'USD': 5,
        'EUR': 5.50,
        'BRL': 1
    }
    if de not in currency or para not in currency:
        print("We don't have these currencies in our system")
        return
    if de == 'USD' and para == 'BRL':
        result = valor * currency['USD']
    elif de == 'BRL' and para == 'USD':
        result = valor / currency['USD']
    elif de == 'BRL' and para == 'EUR':
        result = valor * currency['EUR']
    elif de == 'EUR' and para == 'BRL':
        result = valor / currency['EUR']
    
    print(f"{result:.2f}")
converter(100, 'USD', 'BRL')