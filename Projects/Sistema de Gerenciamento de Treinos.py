import json
import sys
import os

# --- Função para tocar som de erro ---
def tocar_som_erro():
    try:
        import winsound
        caminho_erro = r"C:\Users\Cyntia Trindade\Downloads\erro.wav"
        if os.path.exists(caminho_erro):
            winsound.PlaySound(caminho_erro, winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            print("Arquivo de som não encontrado.")
    except ImportError:
        print("Som de erro indisponível neste sistema.")
    except Exception as e:
        print(f"Erro ao tocar som: {e}")


# --------------------- LISTAS BASE POR GRUPO MUSCULAR ---------------------
try:
    lista_peito_triceps_ombro = [
        'Supino reto',
        'Supino inclinado com halteres',
        'Crossover ou crucifixo',
        'Crucifixo inclinado com halteres',
        'Flexão de braços',
        'Supino declinado',
        'Supino com pegada fechada',
        'Flexão diamante',
        'Peck deck (máquina voador)',
        'Flexão pliométrica',
        'Desenvolvimento de ombros',
        'Elevação lateral',
        'Elevação frontal',
        'Encolhimento de ombros',
        'Desenvolvimento Arnold',
        'Desenvolvimento militar (barra)',
        'Face pull',
        'Crucifixo inverso (posterior)',
        'Elevação lateral inclinada',
        'Remada alta (barra ou halteres)',
        'Tríceps testa',
        'Tríceps pulley',
        'Mergulho entre bancos',
        'Tríceps francês',
        'Tríceps coice com halter',
        'Tríceps na corda (polia alta)',
        'Mergulho nas paralelas',
        'Tríceps kickback unilateral',
        'Supino fechado',
        'Tríceps no banco com peso no colo'
    ]

    lista_biceps_costas_antebraco = [
        'Remada baixa',
        'Puxada frontal (barra ou polia)',
        'Remada curvada',
        'Puxada neutra na polia',
        'Barra fixa',
        'Remada unilateral com halter',
        'Levantamento terra',
        'Puxada atrás da nuca (barra/polia)',
        'Pullover com halteres',
        'Remada cavalinho (T-bar row)',
        'Rosca direta',
        'Rosca alternada com halteres',
        'Rosca martelo',
        'Rosca concentrada',
        'Rosca Scott',
        'Rosca 21 (técnica)',
        'Rosca inversa (pegada pronada)',
        'Rosca spider (no banco inclinado,)',
        'Rosca em polia baixa',
        'Rosca com corda (polia)'
    ]

    lista_abdomen = [
        'Prancha',
        'Abdominal infra',
        'Abdominal oblíquo',
        'Abdominal canivete',
        'Ab wheel (roda abdominal)',
        'Elevação de pernas suspenso',
        'Prancha lateral',
        'Bicicleta no ar',
        'Crunch tradicional',
        'Russian twist (torção russa)'
    ]

    lista_perna = [
        'Agachamento livre',
        'Leg press',
        'Stiff ou levantamento terra romeno',
        'Avanços (lunges)',
        'Elevação de panturrilha',
        'Cadeira extensora',
        'Cadeira flexora',
        'Agachamento sumô com halteres',
        'Afundo búlgaro',
        'Agachamento hack machine',
        'Levantamento terra sumô',
        'Passada no step (step up)'
    ]

    # --------------------- TREINOS AUTOMÁTICOS ---------------------
    exercicios_emagrecer = [
        'Peito',
        "1. Supino reto - 3 séries de 12-15 repetições",
        "2. Supino inclinado com halteres - 3 séries de 12-15 repetições",
        "3. Crossover ou crucifixo - 3 séries de 15-20 repetições",
        'Costas',
        "4. Remada baixa - 3 séries de 12-15 repetições",
        "5. Puxada frontal (barra ou polia) - 3 séries de 12-15 repetições",
        "6. Remada curvada - 3 séries de 12-15 repetições",
        'Ombros',
        "7. Desenvolvimento de ombros - 3 séries de 12-15 repetições",
        "8. Elevação lateral - 3 séries de 15-20 repetições",
        "9. Elevação frontal - 3 séries de 15-20 repetições",
        'Bíceps',
        "10. Rosca direta - 3 séries de 12-15 repetições",
        "11. Rosca alternada com halteres - 3 séries de 12-15 repetições",
        "12. Rosca martelo - 3 séries de 12-15 repetições",
        'Tríceps',
        "13. Tríceps testa - 3 séries de 12-15 repetições",
        "14. Tríceps pulley - 3 séries de 12-15 repetições",
        "15. Mergulho entre bancos - 3 séries de 12-15 repetições",
        'Pernas',
        "16. Agachamento livre - 3 séries de 12-15 repetições",
        "17. Leg press - 3 séries de 12-15 repetições",
        "18. Stiff ou levantamento terra romeno - 3 séries de 12-15 repetições",
        "19. Avanços (lunges) - 3 séries de 15 repetições por perna",
        "20. Elevação de panturrilha - 3 séries de 20 repetições",
        'Abdômen',
        "21. Prancha - 3 séries de 30-45 segundos",
        "22. Abdominal infra - 3 séries de 15-20 repetições",
        "23. Abdominal oblíquo - 3 séries de 15-20 repetições",
        "24. Abdominal canivete - 3 séries de 15 repetições"
    ]

    exercicios_ideal = [
        'Peito',
        "1. Supino reto - 4 séries de 8-12 repetições",
        "2. Supino inclinado com halteres - 4 séries de 8-12 repetições",
        "3. Crossover ou crucifixo - 3 séries de 12-15 repetições",
        'Costas',
        "4. Remada baixa - 4 séries de 8-12 repetições",
        "5. Puxada frontal (barra ou polia) - 4 séries de 8-12 repetições",
        "6. Remada curvada - 3 séries de 8-12 repetições",
        'Ombros',
        "7. Desenvolvimento de ombros - 4 séries de 8-12 repetições",
        "8. Elevação lateral - 3 séries de 12-15 repetições",
        "9. Elevação frontal - 3 séries de 12-15 repetições",
        'Bíceps',
        "10. Rosca direta - 4 séries de 8-12 repetições",
        "11. Rosca alternada com halteres - 3 séries de 8-12 repetições",
        "12. Rosca martelo - 3 séries de 8-12 repetições",
        'Tríceps',
        "13. Tríceps testa - 3 séries de 8-12 repetições",
        "14. Tríceps pulley - 3 séries de 8-12 repetições",
        "15. Mergulho entre bancos - 3 séries de 10-12 repetições",
        'Pernas',
        "16. Agachamento livre - 4 séries de 8-12 repetições",
        "17. Leg press - 4 séries de 8-12 repetições",
        "18. Stiff ou levantamento terra romeno - 3 séries de 8-12 repetições",
        "19. Avanços (lunges) - 3 séries de 12 repetições por perna",
        "20. Elevação de panturrilha - 4 séries de 15-20 repetições",
        'Abdômen',
        "21. Prancha - 3 séries de 30-60 segundos",
        "22. Abdominal infra - 3 séries de 15-20 repetições",
        "23. Abdominal oblíquo - 3 séries de 15-20 repetições",
        "24. Abdominal canivete - 3 séries de 12-15 repetições"
    ]

    exercicios_ganhar_peso = [
        'Peito',
        "1. Supino reto - 4 séries de 6-10 repetições",
        "2. Supino inclinado com halteres - 4 séries de 6-10 repetições",
        "3. Crossover ou crucifixo - 3 séries de 8-12 repetições",
        'Costas',
        "4. Remada baixa - 4 séries de 6-10 repetições",
        "5. Puxada frontal (barra ou polia) - 4 séries de 6-10 repetições",
        "6. Remada curvada - 3 séries de 8-12 repetições",
        'Ombros',
        "7. Desenvolvimento de ombros - 4 séries de 6-10 repetições",
        "8. Elevação lateral - 3 séries de 8-12 repetições",
        "9. Elevação frontal - 3 séries de 8-12 repetições",
        'Bíceps',
        "10. Rosca direta - 4 séries de 6-10 repetições",
        "11. Rosca alternada com halteres - 3 séries de 8-12 repetições",
        "12. Rosca martelo - 3 séries de 8-12 repetições",
        'Tríceps',
        "13. Tríceps testa - 3 séries de 8-12 repetições",
        "14. Tríceps pulley - 3 séries de 8-12 repetições",
        "15. Mergulho entre bancos - 3 séries de 8-12 repetições",
        'Pernas',
        "16. Agachamento livre - 4 séries de 6-10 repetições",
        "17. Leg press - 4 séries de 6-10 repetições",
        "18. Stiff ou levantamento terra romeno - 3 séries de 8-12 repetições",
        "19. Avanços (lunges) - 3 séries de 8-12 repetições por perna",
        "20. Elevação de panturrilha - 4 séries de 12-15 repetições",
        'Abdômen',
        "21. Prancha - 3 séries de 30-60 segundos",
        "22. Abdominal infra - 3 séries de 12-15 repetições",
        "23. Abdominal oblíquo - 3 séries de 12-15 repetições",
        "24. Abdominal canivete - 3 séries de 12 repetições"
    ]

    # --------------------- INICIALIZAÇÃO ---------------------
    print('/////////////////////////////////////////////////////////////////////////////////////////// Sharp-Fit //////////////////////////////////////////////////////////////////////////////////////////')
    print('Seja bem-vindo ao melhor aplicativo para academia!\n')

    # Carregar ou criar cadastro
    dados_do_usuario = []
    try:
        with open('cadastro.json', 'r', encoding='utf-8') as f:
            dados_do_usuario = json.load(f)
        print(f"Bem-vindo de volta, {dados_do_usuario[1]}!")
    except FileNotFoundError:
        genero = input('Por favor, nos diga seu gênero: ')
        nome = input('Por favor, nos diga seu nome: ')
        altura = float(input('Por favor, nos diga sua altura em metros: '))
        peso = int(input('Por favor, nos diga seu peso em kg: '))
        idade = int(input('Por favor, nos diga sua idade: '))
        imc = round(peso / (altura ** 2), 2)
        dados_do_usuario = [genero, nome, imc, idade]
        with open('cadastro.json', 'w', encoding='utf-8') as f:
            json.dump(dados_do_usuario, f, indent=4, ensure_ascii=False)

        if imc < 18.5:
            print(f"{nome}, você está na classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            print(f"{nome}, você está na classificação: Peso ideal")
        else:
            print(f"{nome}, você está na classificação: Acima do peso")

    # --------------------- ESCOLHA DO TIPO DE TREINO ---------------------
    escolha = int(input("\nDeseja um treino recomendado [1] ou criar seu próprio treino [2]? "))

    if escolha == 1:
        imc = dados_do_usuario[2]
        if imc < 18.5:
            print("\nRecomendado: Exercícios para GANHO DE MASSA MUSCULAR")
            for item in exercicios_ganhar_peso:
                print(item)
        elif 18.5 <= imc < 24.9:
            print("\nRecomendado: Exercícios para DEFINIÇÃO")
            for item in exercicios_ideal:
                print(item)
        else:
            print("\nRecomendado: Exercícios para PERDA DE PESO")
            for item in exercicios_emagrecer:
                print(item)

        while True:
            print("\nDeseja ver outra categoria?")
            print("1 - Lista para ganho de massa muscular")
            print("2 - Lista para definição")
            print("3 - Lista para perda de peso")
            print("0 - Sair")
            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                print("\nExercícios para ganho de massa:")
                for item in exercicios_ganhar_peso: print(item)
            elif opcao == "2":
                print("\nExercícios para definição:")
                for item in exercicios_ideal: print(item)
            elif opcao == "3":
                print("\nExercícios para perda de peso:")
                for item in exercicios_emagrecer: print(item)
            elif opcao == "0":
                print("\nObrigado por usar o app!")
                exit()
            else:
                print("Opção inválida, tente novamente.")

    # --------------------- GERENCIAMENTO MANUAL POR GRUPO ---------------------
    else:
        # Estrutura de treino por grupo
        estrutura_grupos = {
            "peito_triceps_ombro": [],
            "biceps_costas_antebraco": [],
            "abdomen": [],
            "perna": []
        }

        # Carregar treino existente
        try:
            with open('exercicios.json', 'r', encoding='utf-8') as f:
                estrutura_grupos = json.load(f)
        except FileNotFoundError:
            pass  # Começa vazio

        # Mapeamento de opções
        grupos_opcoes = {
            '0': ("peito_triceps_ombro", lista_peito_triceps_ombro),
            '1': ("biceps_costas_antebraco", lista_biceps_costas_antebraco),
            '2': ("abdomen", lista_abdomen),
            '3': ("perna", lista_perna)
        }

        while True:
            print("\n=== GERENCIAR TREINO PERSONALIZADO ===")
            print("Escolha uma ação:")
            print("0 - Adicionar exercício")
            print("1 - Remover exercício")
            print("2 - Atualizar exercício")
            print("3 - Buscar exercício")
            print("4 - Listar todos os exercícios")
            print("5 - Sair")
            acao = input("Opção: ").strip()

            if acao == "5":
                print("Treino salvo! Até a próxima.")
                break

            if acao == "4":  # Listar todos
                print("\n--- TREINO COMPLETO ---")
                vazio = True
                for grupo_nome, exercicios in estrutura_grupos.items():
                    if exercicios:
                        vazio = False
                        print(f"\n{grupo_nome.upper()}:")
                        for i, ex in enumerate(exercicios, 1):
                            print(f"  {i}. {ex['Exercício']} → {ex['S']} séries, {ex['R']} reps, {ex['P']} kg")
                if vazio:
                    print("Nenhum exercício adicionado ainda.")
                continue

            # Escolher grupo
            print("\nEscolha o grupo muscular:")
            print("0 - Peito, Tríceps e Ombro")
            print("1 - Bíceps, Costas e Antebraço")
            print("2 - Abdômen")
            print("3 - Pernas")
            grupo_escolha = input("Grupo: ").strip()
            if grupo_escolha not in grupos_opcoes:
                print("Grupo inválido.")
                continue

            chave_grupo, lista_disponivel = grupos_opcoes[grupo_escolha]

            if acao == "0":  # Adicionar
                print(f"\nExercícios disponíveis em {chave_grupo}:")
                for i, ex in enumerate(lista_disponivel, 1):
                    print(f"{i}. {ex}")
                num = input("\nNúmero do exercício ('sair' para cancelar): ")
                if num.lower() == "sair":
                    continue
                if num.isdigit() and 1 <= int(num) <= len(lista_disponivel):
                    exercicio = lista_disponivel[int(num) - 1]
                    s = input("Séries: ")
                    r = input("Repetições: ")
                    p = input("Peso (kg, 0 se não usar): ")
                    if s.isdigit() and r.isdigit() and p.isdigit():
                        estrutura_grupos[chave_grupo].append({
                            "Exercício": exercicio,
                            "S": int(s),
                            "R": int(r),
                            "P": int(p)
                        })
                        print(f"✅ Adicionado: {exercicio}")
                    else:
                        print("Valores inválidos. Use apenas números.")
                else:
                    print("Número inválido.")

            elif acao == "1":  # Remover
                 exercicios = estrutura_grupos[chave_grupo]
                 if not exercicios:
                    print("Nenhum exercício neste grupo.")
                    continue
                 else:
                    estrutura_grupos[chave_grupo].clear()
                    print(f" Todos os exercícios do grupo '{chave_grupo}' foram removidos.")

            elif acao == "2":  # Atualizar
                exercicios = estrutura_grupos[chave_grupo]
                if not exercicios:
                    print("Nenhum exercício neste grupo.")
                    continue
                print(f"\nExercícios em {chave_grupo}:")
                for i, ex in enumerate(exercicios, 1):
                    print(f"{i}. {ex['Exercício']} → {ex['S']}s, {ex['R']}r, {ex['P']}kg")
                num = input("Número para atualizar ('sair' para cancelar): ")
                if num.lower() == "sair":
                    continue
                if num.isdigit() and 1 <= int(num) <= len(exercicios):
                    idx = int(num) - 1
                    s = input(f"Novas séries (atual: {exercicios[idx]['S']}): ") or str(exercicios[idx]['S'])
                    r = input(f"Novas repetições (atual: {exercicios[idx]['R']}): ") or str(exercicios[idx]['R'])
                    p = input(f"Novo peso (atual: {exercicios[idx]['P']}): ") or str(exercicios[idx]['P'])
                    if s.isdigit() and r.isdigit() and p.isdigit():
                        exercicios[idx].update({"S": int(s), "R": int(r), "P": int(p)})
                        print("✅ Atualizado com sucesso!")
                    else:
                        print("Valores inválidos.")
                else:
                    print("Número inválido.")

            elif acao == "3":  # Buscar
              termo = input("Digite o nome (ou parte do nome) do grupo muscular: ").strip().lower()

              grupo_encontrado = None
              for nome_grupo in estrutura_grupos.keys():
                    if termo in nome_grupo.lower():
                        grupo_encontrado = nome_grupo
                        break

              if grupo_encontrado:
                    exercicios = estrutura_grupos[grupo_encontrado]
                    if exercicios:
                        print(f"\n--- {grupo_encontrado.upper()} ---")
                        for ex in exercicios:
                            print(f"  • {ex['Exercício']} → {ex['S']} séries, {ex['R']} reps, {ex['P']} kg")
                    else:
                        print(f"O grupo '{grupo_encontrado}' está vazio.")
              else:
                    print("Nenhum grupo muscular encontrado.")
            
except Exception as e:
    print(f"\n❌ Ocorreu um erro inesperado: {e}")
    tocar_som_erro()  # <<<--- Chama aqui
    input("Pressione Enter para sair...")
    sys.exit(1)             