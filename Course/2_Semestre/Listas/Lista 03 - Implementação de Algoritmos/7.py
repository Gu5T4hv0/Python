def analise_de_temperaturas(temps, L):
    average = sum(temps)/len(temps)
    over_avg = 0
    for temp in temps:
        if temp > average:
            over_avg += 1
    
    streak = 0
    max_streak = 0
    for i in temps:
        if i > L:
            streak += 1
            if streak > max_streak:
                max_streak = streak
        else:
            streak = 0
    print(f"media={average:.2f}, acima_media={over_avg}, maior_sequencia_acima_L={max_streak}.")
analise_de_temperaturas([28, 31, 33, 29, 30, 34], 30)