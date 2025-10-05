def fila_de_atendimento(atendiment, actions):
    verbs = actions.split(', ')
    positions = atendiment.split(', ')
    for i in positions:
        if i.startswith("PRIORITARIO"):
            positions.remove(i)
            positions.insert(0, i)
            break
    
    verbs = ['ATENDE', 'ATENDE']
    positions = ['PRIORITARIO João', 'CHEGA Ana', 'CHEGA Bia']
    q_atend = len(verbs)
    premier = positions[:q_atend]
    resto = positions[q_atend:]

    last_list = []
    for item in premier:
        new_spliter = item.split(' ')
        last_list.append(new_spliter)
    
    new_list = []
    for small_list in last_list:
        new_small = []
        for word in small_list:
            if word != "PRIORITARIO" and word != "CHEGA":
                new_small.append(word)
        new_list.append(new_small)
    
    derniere_list = []
    for iten in resto:
        nouveau_spliter = iten.split(' ')
        derniere_list.append(nouveau_spliter)

    nouvelle_list = []
    for petit_list in derniere_list:
        nouveau_petit = []
        for parole in petit_list:
            if parole != "PRIORITARIO" and parole != "CHEGA":
                nouveau_petit.append(parole)
        nouvelle_list.append(nouveau_petit)
    
    attended_list = []
    for list in new_list:
        for name in list:
            attended_list.append(name)
    attended = ", ".join(attended_list)

    remaining_list = []
    for liste in nouvelle_list:
        for nom in liste:
            remaining_list.append(nom)
    remaining = ", ".join(remaining_list)
        
    print(f"Atendidos: {attended}; Na fila: {remaining}")

fila_de_atendimento('CHEGA Ana, CHEGA Bia, PRIORITARIO João', 'ATENDE, ATENDE')