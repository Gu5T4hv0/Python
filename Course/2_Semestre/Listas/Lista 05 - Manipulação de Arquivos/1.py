def criar_arquivo():
    with open("contatos.txt", "w", encoding="utf-8") as file:
        file.writelines()

def obtercomando(comando:str):
    comando = comando.split()