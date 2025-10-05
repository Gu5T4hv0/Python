import heapq

def adicionar():
    tarefas = {}
    continuo = True
    while continuo:
        numero = int(input("digite a prioridade da sua tarefa, sendo 1 mais importante e 10 menos: "))
        tarefa = str(input("digite a sua tarefa: "))
        continuidade = str(input("Se deseja continuar adicionando digite True, caso não, False: "))
        if continuidade.lower() == "false":
            continuo = False
        tarefas[numero] = tarefa
    return tarefas

def listar(tarefas):
    print("\nLista de tarefas:")
    listadas = {}
    for prioridade, tarefa in sorted(tarefas.items()):
        listadas[prioridade] = tarefa
    return listadas

def executar_proxima(listadas):
    listadas


tarefas = adicionar()
listadas = listar(tarefas)
executar_proxima(listadas)