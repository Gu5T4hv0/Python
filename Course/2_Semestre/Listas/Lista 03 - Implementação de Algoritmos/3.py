def controle_de_estoque(initial_stock, operations):
    invalid = 0

    for operation in operations:
        parts = operation.split(' ')
        op = parts[0]
        key = parts[1]
        value = int(parts[2])
    
        if op == 'E':
            if key in initial_stock:
                initial_stock[key] += value
            else:
                initial_stock[key] == value
        else:
            if key in initial_stock and value <= initial_stock[key]:
                initial_stock[key] -= value
            else:
                invalid += 1
    print(f"New stock = {initial_stock}, Invalides = {invalid}")

controle_de_estoque({'A':10, 'B':3}, ['E A 5', 'S B 2', 'S A 20'])