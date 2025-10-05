valor_total = float(input("Valor da compra: "))
e_cliente_fidelidade = bool(input("Você é cliente de fidelidade? "))

if valor_total > 1000:
    print("15%")
elif valor_total > 500:
    print("10%")

if e_cliente_fidelidade:
    print("desconto extra de 15%")
else:
    print("0 desconto")
    

#do maior para o menor