idade = int(input("Digite a idade: "))
idade_responsavel = int(input("Digite a idade_resp: "))

comprou_o_ingresso = True
documento_e_valido = False

if comprou_o_ingresso and documento_e_valido:
    print("NÃO PASSA")
elif idade < 18 and idade_responsavel >= 18:
    print("PASSA")
else:
    print("NUM FAÇO IDEIA")