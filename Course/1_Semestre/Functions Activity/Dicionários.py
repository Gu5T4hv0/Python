# 1.def obter_valor(dicionario, chave): → Retorne o valor associado a uma chave em um dicionário. Se a chave não existir, retorne None.
def obter_valor(dicionario, chave):
    return dicionario.get(chave)
# 2.def chave_existe(dicionario, chave): → Verifique se uma determinada chave existe no dicionário.
def chave_existe(dicionario, chave):
    if chave in dicionario:
        return True
    else:
        return False
# 3.def adicionar_par(dicionario, chave, valor): → Adicione ou atualize um par chave-valor em um dicionário e retorne o dicionário atualizado.
def adicionar_par(dicionario, chave, valor):
    dicionario.update({chave: valor})
    return dicionario
# 4.def remover_chave(dicionario, chave): → Remova uma chave do dicionário, se ela existir, e retorne o novo dicionário.
def remover_chave(dicionario, chave):
    dicionario.pop(chave)
    return dicionario
# 5.def contar_chaves(dicionario): → Retorne a quantidade de chaves existentes no dicionário.
def contar_chaves(dicionario):
    quantidade = len(dicionario)
    return quantidade
# 6.def inverter_dicionario(dicionario): → Retorne um novo dicionário com as chaves e valores invertidos.
def inverter_dicionario(dicionario):
    new_dict = {}
    for i, j in dicionario.items():
        new_dict[j] = i
    return new_dict
# 7.def mesclar_dicionarios(d1, d2): → Retorne um novo dicionário contendo os pares de d1 e d2, priorizando os valores de d2 em caso de conflito.
def mesclar_dicionarios(d1, d2):
    novo = d1.copy()
    novo.update(d2)
    return novo
# 8.def contar_ocorrencias(lista): → Receba uma lista e retorne um dicionário com a contagem de ocorrências de cada elemento.
def contar_ocorrencias(lista):
    ocorrencias = {}
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1
        else:
            ocorrencias[item] = 1
    return ocorrencias
# 9.def chaves_em_ordem_alfabetica(dicionario): → Retorne uma lista com as chaves do dicionário em ordem alfabética.
def chaves_em_ordem_alfabetica(dicionario):
    ordem = sorted(dicionario)
    return ordem
# 10.def remover_chaves_vazias(dicionario): → Remova as chaves que possuem valores None ou strings vazias do dicionário.
def remover_chaves_vazias(dicionario):
    new = {}
    for i, j in dicionario.items():
        if j != "" and j is not None:
            new[i] = j
    return new
# 11.def somar_valores(dicionario): → Retorne a soma de todos os valores numéricos do dicionário.
def somar_valores(dicionario):
    total = sum(dicionario.values())
    return total
# 12.def maiores_que(dicionario, limite): → Retorne um novo dicionário com os pares cujo valor seja maior que um valor-limite fornecido.
def maiores_que(dicionario, limite):
    new = {}
    for i, j in dicionario.items():
        if j > limite:
            new[i] = j
    return new
# 13.def agrupar_por_tamanho(palavras): → Agrupe palavras de uma lista por tamanho, retornando um dicionário onde as chaves são os comprimentos das palavras.
def agrupar_por_tamanho(palavras):
    agrupadas = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho in agrupadas:
            agrupadas[tamanho].append(palavra)
        else:
            agrupadas[tamanho] = [palavra]
    return agrupadas
# 14.def encontrar_chave_por_valor(dicionario, valor): → Retorne a chave correspondente ao valor fornecido. Se não existir, retorne None.
def encontrar_chave_por_valor(dicionario, valor):
    for chave, val in dicionario.items():
        if val == valor:
            return chave
    return None
# 15.def contar_letras(frase): → Retorne um dicionário com a contagem de cada letra em uma frase (ignorar espaços e pontuação).
import string

def contar_letras(frase):
    contagem = {}
    for char in frase.lower():
        if char.isalpha():
            contagem[char] = contagem.get(char, 0) + 1
    return contagem