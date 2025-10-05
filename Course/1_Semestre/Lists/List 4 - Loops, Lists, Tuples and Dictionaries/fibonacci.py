def gerar(qtd):
    if qtd > 0:
        seq = []
        for i in range(qtd):
            if i in [0,1]:
                seq.append(i)
            else:
                seq.append(seq[i-2] + seq[i-1])
        return seq
    else:
        print("Entrada inválida")