exercicios = {
    "Supino reto": "4 séries de 6-10 repetições",
    "Supino inclinado com halteres": "4 séries de 6-10 repetições"
}
while True:
    exercicio = input("Qual é o exercicio você deseja buscar?: ")
    if len(exercicios) == 0:
        print("A lista está vazia, adicione algo antes")
        break
    else:
        for key, value in exercicios.items():
            if key.lower() == exercicio.lower():
                print(f"{key} -> {exercicios[key]}")
                break
        else:
            print("O exercicio mencionado não está na lista")
            break

    buscar_outro = input("Deseja buscar outro item?(sim/não): ")
    if buscar_outro != "sim":
        break