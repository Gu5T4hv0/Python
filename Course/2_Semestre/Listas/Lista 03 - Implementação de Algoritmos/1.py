def class_bulletin(N, bulletin):
    average = sum(bulletin) / N
    greater = max(bulletin)
    lower = min(bulletin)

    summing = 0
    for number in bulletin:
        summing += (number - average)**2
    st_dev = (summing/N)**0.5

    counter = 0
    zero_ate_dois = 0
    dois_ate_quatro = 0
    quatro_ate_seis = 0
    seis_ate_oito = 0
    oito_ate_dez = 0
    
    for i in bulletin:
        if i > 7:
            counter += 1
        if 0 <= i < 2:
            zero_ate_dois += 1
        elif 2 <= i < 4:
            dois_ate_quatro += 1
        elif 4 <= i < 6:
            quatro_ate_seis += 1
        elif 6 <= i < 8:
            seis_ate_oito += 1
        elif 8 <= i <= 10:
            oito_ate_dez += 1
            
    print(f"media={average:.2f}, maior={greater}, menor={lower}, desvio-padrão={st_dev:.2f}, acima_media={counter}\nfaixas: [0-2)={zero_ate_dois}, [2-4)={dois_ate_quatro}, [4-6)={quatro_ate_seis}, [6-8)={seis_ate_oito}, [8-10]={oito_ate_dez}")

class_bulletin(6, [7.5, 9.0, 4.0, 6.5, 8.0, 5.0])