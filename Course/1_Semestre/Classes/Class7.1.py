dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

dia_da_semana = int(input("Digite um número de 1 a 7 para o dia da semana: "))

if dia_da_semana >= 1 and dia_da_semana <= 7:
    print(dias[dia_da_semana - 1])
else:
    print("Entrada inválida")