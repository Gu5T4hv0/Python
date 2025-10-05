import shutil
def copiar_arquivo(origem, destino):
    shutil.copy(origem, destino)
    
copiar_arquivo("1.txt", "3.txt")