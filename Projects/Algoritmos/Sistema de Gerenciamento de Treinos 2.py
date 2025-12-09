import winsound
import json
import sys
import os
from datetime import date, timedelta
from typing import Dict, Any
import time

# --- Função para tocar som de erro ---
def tocar_som_erro():
    try:
        import winsound 
        caminho_erro = r"C:\erro\erro.wav"
        if os.path.exists(caminho_erro):
            winsound.PlaySound(caminho_erro, winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            print("Arquivo de som não encontrado.")
    except ImportError:
        print("Som de erro indisponível neste sistema.")
    except Exception as e:
        print(f"Erro ao tocar som: {e}")

# --- Função para limpar a tela e manter o título centralizado ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    largura = 120  # ajuste conforme necessário
    titulo = "/////////////////////////////////////////////////////////////////////////// Sharp-Fit /////////////////////////////////////////////////////////////////////////////"
    print(titulo.center(largura))
    print("\n")

# ============================ ADICIONAL 2: RASTREAMENTO DE STREAK ============================

def registrar_treino_concluido():
    """Registra o treino de hoje no histórico (se ainda não estiver lá)."""
    try:
        with open('historico_treinos.json', 'r', encoding='utf-8') as f:
            historico = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        historico = []

    data_hoje = date.today().strftime('%Y-%m-%d')
    if data_hoje not in historico:
        historico.append(data_hoje)
        historico.sort(key=lambda d: date.fromisoformat(d), reverse=True) 
        
        with open('historico_treinos.json', 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)
        return True
    return False

def calcular_streak():
    """Calcula a sequência (streak) de dias consecutivos de treino."""
    try:
        with open('historico_treinos.json', 'r', encoding='utf-8') as f:
            historico_datas_str = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    historico_datas = sorted(list(set(
        [date.fromisoformat(d) for d in historico_datas_str]
    )), reverse=True)

    if not historico_datas:
        return 0

    streak_count = 0
    data_referencia = date.today() 

    for data_reg in historico_datas:
        if data_reg == data_referencia:
            streak_count += 1
            data_referencia -= timedelta(days=1)
        elif data_reg < data_referencia:
            break

    return streak_count

# ============================ ADICIONAL 1: RASTREAMENTO DE RP ============================

def carregar_rp_historico() -> Dict[str, Any]:
    """Carrega o histórico de Recordes Pessoais (RP) por exercício."""
    try:
        with open('performance_rp.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_rp_historico(rp_data: Dict[str, Any]):
    """Salva o histórico de Recordes Pessoais (RP)."""
    with open('performance_rp.json', 'w', encoding='utf-8') as f:
        json.dump(rp_data, f, indent=4, ensure_ascii=False)

def atualizar_rp_e_feedback(nome_exercicio: str, nova_carga: float):
    """Verifica e atualiza o RP máximo de carga e retorna a mensagem de feedback."""
    rp_historico = carregar_rp_historico()
    
    # Pega o RP anterior ou 0.0 se não existir
    rp_anterior = rp_historico.get(nome_exercicio, 0.0)
    
    feedback = ""

    if nova_carga > rp_anterior:
        # Atualiza o RP
        rp_historico[nome_exercicio] = nova_carga
        salvar_rp_historico(rp_historico)
        
        if rp_anterior == 0.0:
            feedback = f"\n✅ Primeiro registro de Carga para {nome_exercicio}: {nova_carga} kg."
        else:
            diferenca = nova_carga - rp_anterior
            feedback = f"\n🎉 NOVO RECORDE PESSOAL DE CARGA em {nome_exercicio}! 🚀\n  → {nova_carga} kg (Melhora de +{diferenca:.1f} kg sobre o RP anterior de {rp_anterior} kg)"
            
    elif nova_carga == rp_anterior and nova_carga > 0:
         feedback = f"\n⭐ Carga igual ao seu RP para {nome_exercicio}: {nova_carga} kg. Excelente performance!"
         
    return feedback

try:
    # --------------------- LISTAS BASE POR GRUPO MUSCULAR ---------------------
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

    exercicios_ganhar_massa = [
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

    # ============================ INICIALIZAÇÃO ============================
    limpar_tela()
    print('Seja bem-vindo ao melhor aplicativo para academia!\n')

    # Carregar ou criar cadastro
    dados_do_usuario = []
    try:
        with open('cadastro.json', 'r', encoding='utf-8') as f:
            dados_do_usuario = json.load(f)
        print(f"Bem-vindo de volta, {dados_do_usuario[1]}!")

        # EXIBIÇÃO DO STREAK (ADICIONAL 2)
        streak = calcular_streak()
        if streak > 0:
            print(f"🔥 CONQUISTA: Seu recorde atual de dias seguidos de treino (Streak) é de {streak} dias!")
        else:
            print("💪 Vamos começar a construir seu Streak de treino hoje!")

    except FileNotFoundError:
        genero = input('Por favor, nos diga seu gênero: ')
        nome = input('Por favor, nos diga seu nome: ')
        try:
            altura = float(input('Por favor, nos diga sua altura em metros: '))
            peso = int(input('Por favor, nos diga seu peso em kg: '))
            idade = int(input('Por favor, nos diga sua idade: '))
        except ValueError:
            
            print("Entrada inválida. Altura deve ser número decimal (ex: 1.75) e Peso/Idade números inteiros.")
            tocar_som_erro()
            time.sleep(14)
            sys.exit(1)
            

        limpar_tela()
        if altura <= 0 or peso <= 0 or idade <= 0:
            print("Valores inválidos para cadastro.")
            sys.exit(1)

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
        
    # ============================ ESCOLHA DO TREINO ============================
    rodando = True
    while rodando:    
        try:
            
            escolha = int(input("\nDeseja um treino recomendado [1] ou criar seu próprio treino [2]? "))
        except ValueError:
            tocar_som_erro()
            print("Opção inválida.")
            sys.exit(1)
        #gostaria de usar essa lista
        if escolha == 1:
            imc = dados_do_usuario[2]
            limpar_tela()
            if imc < 18.5:
                print("\nRecomendado: Exercícios para GANHO DE MASSA MUSCULAR")
                for item in exercicios_ganhar_massa:
                    print(item)
                escolha_lista_1 = input('gostaria de usar essa lista ? (sim/não) ')
                if escolha_lista_1 == 'sim':
                    with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                        json.dump(exercicios_ganhar_massa, f, ensure_ascii=False, indent=2)
                    
            elif 18.5 <= imc < 24.9:
                print("\nRecomendado: Exercícios para DEFINIÇÃO")
                for item in exercicios_ideal:
                    print(item)
                escolha_lista_2 = input('gostaria de usar essa lista (sim/não)  ? ')
                if escolha_lista_2 == 'sim':
                    with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                        json.dump(exercicios_ideal, f, ensure_ascii=False, indent=2)
                        
            else:
                print("\nRecomendado: Exercícios para PERDA DE PESO")
                for item in exercicios_emagrecer:
                    print(item)
                escolha_lista_3 = input('gostaria de usar essa lista ? (sim/não)  ')
                if escolha_lista_3 == 'sim':
                    with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                        json.dump(exercicios_emagrecer, f, ensure_ascii=False, indent=2)
            loop_ativo_escolha1 = True
            while loop_ativo_escolha1:
                print("\nDeseja ver outra categoria?")
                print("1 - Lista para ganho de massa muscular")
                print("2 - Lista para definição")
                print("3 - Lista para perda de peso")
                print("4 - Mostrar o treino escolhido anteriormente")
                print("5 - Retornar para o menu")
                print("0 - Sair")
                opcao = input("Digite o número da opção desejada: ")
                limpar_tela()
                if opcao == "5":
                    loop_ativo_escolha1 = False
                    continue
                if opcao == "1":
                    for item in exercicios_ganhar_massa: print(item)
                    escolha_lista_alternativa_1 = input('Deseja salvar essa lista ?[sim/não] ')
                    if escolha_lista_alternativa_1 == 'sim':
                        with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                            json.dump(exercicios_ganhar_massa, f, ensure_ascii=False, indent=2)
                elif opcao == "2":
                    for item in exercicios_ideal: print(item)
                    escolha_lista_alternativa_2 = input('Deseja salvar essa lista ? [sim/não] ')
                    if escolha_lista_alternativa_2 == 'sim':
                        with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                            json.dump(exercicios_ideal, f, ensure_ascii=False, indent=2)
                elif opcao == "3":
                    for item in exercicios_emagrecer: print(item)
                    escolha_lista_alternativa_3 = input('Deseja salvar essa lista ? [sim/não] ')
                    if escolha_lista_alternativa_3 == 'sim':
                        with open('lista_pre_pronta.json', 'w', encoding='utf-8') as f:
                            json.dump(exercicios_emagrecer, f, ensure_ascii=False, indent=2)
                elif opcao == "4":
                    try:
                        with open('lista_pre_pronta.json', 'r', encoding='utf-8') as f:
                            lista_de_exercicios_escolhidos_anteriormente = json.load(f)
                            for item in lista_de_exercicios_escolhidos_anteriormente:
                                print(item)
                    except:
                        print("Nenhum treino foi escolhido anteriormente!")
                
                if opcao == "0":
                    # NOVO PASSO: PERGUNTAR SE DESEJA REGISTRAR O TREINO DE HOJE (ADICIONAL 2)
                    confirma_registro = input("\nO treino de hoje foi concluído? (sim/não): ").strip().lower()
                    if confirma_registro == 'sim':
                        if registrar_treino_concluido():
                            print("Treino registrado! 🎉")
                        else:
                            print("Treino de hoje já estava registrado.")
                    
                    print("\nObrigado por usar o app!")
                    exit()

        else:
            # ============================ GERENCIAMENTO MANUAL ============================
            estrutura_grupos = {
                "peito_triceps_ombro": [],
                "biceps_costas_antebraco": [],
                "abdomen": [],
                "perna": []
            }

            try:
                with open('exercicios.json', 'r', encoding='utf-8') as f:
                    estrutura_grupos = json.load(f)
            except FileNotFoundError:
                pass

            grupos_opcoes = {
                '0': ("peito_triceps_ombro", lista_peito_triceps_ombro),
                '1': ("biceps_costas_antebraco", lista_biceps_costas_antebraco),
                '2': ("abdomen", lista_abdomen),
                '3': ("perna", lista_perna)
            }
            loop_ativo_escolha2 = True
            while loop_ativo_escolha2:
                limpar_tela()
                print("=== GERENCIAR TREINO PERSONALIZADO ===")
                print("Escolha uma ação:")
                print("0 - Adicionar exercício ➕ ")
                print("1 - Remover exercício 🗑 ")
                print("2 - Atualizar exercício 🔄 ")
                print("3 - Buscar exercício 🔎 ")
                print("4 - Listar todos os exercícios 📋 ")
                print("5 - Sair 🔚 ")
                print("6 - Retornar para o menu")
                acao = input("Opção: ").strip()

                if acao == '6':
                    loop_ativo_escolha2 = False
                    continue
                if acao == "5":
                    with open('exercicios.json', 'w', encoding='utf-8') as f:
                        json.dump(estrutura_grupos, f, indent=4, ensure_ascii=False)

                    confirma_registro = input("\nO treino de hoje foi concluído? (sim/não): ").strip().lower()
                    if confirma_registro == 'sim':
                        if registrar_treino_concluido():
                            print("Treino registrado! 🎉")
                        else:
                            print("Treino de hoje já estava registrado.")
                            
                    print("Treino salvo! Até a próxima.")
                    rodando = False
                    break 
        

                if acao == "4":  # Listar todos
                    limpar_tela()
                    print("\n--- TREINO COMPLETO ---")
                    rp_historico = carregar_rp_historico()
                    vazio = True
                    for grupo_nome, exercicios in estrutura_grupos.items():
                        if exercicios:
                            vazio = False
                            print(f"\n{grupo_nome.upper()}:")
                            for i, ex in enumerate(exercicios, 1):
                                rp_atual = rp_historico.get(ex['Exercício'], 0.0)
                                rp_info = f" (RP: {rp_atual:.1f} kg)" if rp_atual > 0 else ""
                                print(f"  {i}. {ex['Exercício']} → {ex['S']} séries, {ex['R']} reps, {ex['P']} kg{rp_info}")
                    if vazio:
                        try:
                                with open('lista_pre_pronta.json','r',encoding='utf-8') as d:
                                    listaes = json.load(d)
                                    print("\n--- LISTA PRÉ-PRONTA ---")

                                    for item in listaes:
                                        item_str = str(item).strip()

                                        if not item_str[:1].isdigit():
                                            print(f"\n{item_str.upper()}:")
    
                                        else:
                                            print(f"  {item_str}")

                        except FileNotFoundError:
                            print("Nenhum exercício adicionado ainda.")
                    input("\nPressione Enter para continuar...")
                    continue
                print("\nEscolha o grupo muscular:")
                print("0 - Peito, Tríceps e Ombro")
                print("1 - Bíceps, Costas e Antebraço")
                print("2 - Abdômen")
                print("3 - Pernas")
                grupo_escolha = input("Grupo: ").strip()
                if grupo_escolha not in grupos_opcoes:
                    print("Grupo inválido.")
                    input("Pressione Enter para continuar...")
                    continue

                chave_grupo, lista_disponivel = grupos_opcoes[grupo_escolha]

                # Adicionar
                if acao == "0":
                    limpar_tela()
                    print(f"\nExercícios disponíveis em {chave_grupo}:")
                    for i, ex in enumerate(lista_disponivel, 1):
                        print(f"{i}. {ex}")
                    num = input("\nNúmero do exercício para adicionar: ").strip()
                    try:
                        num = int(num) - 1
                        if num < 0 or num >= len(lista_disponivel):
                            raise ValueError
                        ex_nome = lista_disponivel[num]
                        S = int(input("Quantas séries? "))
                        R = int(input("Quantas repetições? "))
                        P = float(input("Qual peso (kg)? "))
                        estrutura_grupos[chave_grupo].append({'Exercício': ex_nome, 'S': S, 'R': R, 'P': P})
                        print(f"{ex_nome} adicionado com sucesso!")

                        print(atualizar_rp_e_feedback(ex_nome, P))

                    except ValueError:
                        tocar_som_erro()
                        print("Entrada inválida. Use números inteiros para séries/repetições e números (com ponto ou vírgula) para peso.")
                    except:
                        tocar_som_erro()
                        print("Entrada inválida.")
                    input("Pressione Enter para continuar...")

                # Remover
                elif acao == "1":
                    limpar_tela()
                    descisão = int(input("deseja excluir um exercicio[1] ou o treino inteiro[2]?"))
                    if descisão == 1:
                        if not estrutura_grupos[chave_grupo]:
                            print("Nenhum exercício para remover neste grupo.")
                            input("Pressione Enter para continuar...")
                            continue
                        print(f"Exercícios atuais em {chave_grupo}:")
                        for i, ex in enumerate(estrutura_grupos[chave_grupo], 1):
                            print(f"{i}. {ex['Exercício']}")
                        num = input("Número do exercício para remover: ").strip()
                        try:
                            num = int(num) - 1
                            removido = estrutura_grupos[chave_grupo].pop(num)
                            print(f"{removido['Exercício']} removido com sucesso!")
                        except:
                            tocar_som_erro()
                            print("Entrada inválida.")
                    else:
                        estrutura_grupos[chave_grupo].clear()
                        print("Treino excluído com sucesso.")
                    input("Pressione Enter para continuar...")
                # Atualizar
                elif acao == "2":
                    limpar_tela()
                    if not estrutura_grupos[chave_grupo]:
                        print("Nenhum exercício para atualizar neste grupo.")
                        input("Pressione Enter para continuar...")
                        continue
                    rp_historico = carregar_rp_historico()
                    print(f"Exercícios atuais em {chave_grupo}:")
                    for i, ex in enumerate(estrutura_grupos[chave_grupo], 1):
                        rp_atual = rp_historico.get(ex['Exercício'], 0.0)
                        rp_info = f" (RP: {rp_atual:.1f} kg)" if rp_atual > 0 else ""
                        print(f"  {i}. {ex['Exercício']} → {ex['S']} séries, {ex['R']} reps, {ex['P']} kg{rp_info}")

                    num = input("Número do exercício para atualizar: ").strip()
                    try:
                        num = int(num) - 1
                        selecionado = estrutura_grupos[chave_grupo][num]
                        ex_nome = selecionado.get('Exercício')

                        print(f"séries atuais {selecionado.get('S')}")
                        S = int(input("Quantas séries? "))
                        print(f"Repetições atuais {selecionado.get('R')}")
                        R = int(input("Quantas repetições? "))
                        print(f"Peso atual {selecionado.get('P')}")
                        P = float(input("Qual peso (kg)? "))

                        estrutura_grupos[chave_grupo][num] = {'Exercício': ex_nome, 'S': S, 'R': R, 'P': P}
                        print("Exercício atualizado com sucesso!")

                        print(atualizar_rp_e_feedback(ex_nome, P))

                    except ValueError:
                        tocar_som_erro()
                        print("Entrada inválida. Use números inteiros para séries/repetições e números (com ponto ou vírgula) para peso.")
                    except:
                        tocar_som_erro()
                        print("Entrada inválida.")
                    input("Pressione Enter para continuar...")

                # Buscar
                elif acao == "3":
                    limpar_tela()
                    
                    if chave_grupo in grupos_opcoes[grupo_escolha]:
                        for i, item in enumerate(estrutura_grupos[chave_grupo], start=1):
                            print(f"{i}. {item['Exercício']} — Séries: {item['S']}; Repetições: {item['R']}; Peso: {item['P']}")

                    busca = input("Digite o nome do exercício para buscar: ").strip().lower()
                    encontrado = False
                    rp_historico = carregar_rp_historico()
                    for g, lista in estrutura_grupos.items():
                        for ex in lista:
                            if busca in ex['Exercício'].lower():
                                rp_atual = rp_historico.get(ex['Exercício'], 0.0)
                                rp_info = f" (RP: {rp_atual:.1f} kg)" if rp_atual > 0 else ""
                                print(f"Encontrado no grupo {g}: {ex['Exercício']} → {ex['S']} séries, {ex['R']} reps, {ex['P']} kg{rp_info}")
                                encontrado = True
                    if not encontrado:
                        print("Exercício não encontrado.")
                    input("Pressione Enter para continuar...")
                
                with open('exercicios.json', 'w', encoding='utf-8') as f:
                        json.dump(estrutura_grupos, f, indent=4, ensure_ascii=False)
                

except Exception as e:
    print(f"\n❌ Ocorreu um erro inesperado: {e}")
    tocar_som_erro() 
    input("Pressione Enter para sair...")
    sys.exit(1)