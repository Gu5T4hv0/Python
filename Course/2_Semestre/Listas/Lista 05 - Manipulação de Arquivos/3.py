def contagem_severidades(arquivo, arquivo2):
    counter = {}
    with open(arquivo, "r", encoding="UTF-8") as file:
        reader = file.read().split()
        # print(reader)
        for i in reader:
            if i == "INFO" or i == "WARN" or i == "ERROR" or i == "DEBUG":
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] += 1
        print(f"Severidades = {counter}\n")
    
    with open(arquivo2, "r", encoding="UTF-8") as filo:
        reader2 = filo.read().splitlines()
        # print(reader2)
        lister_error = []
        for j in reader2:
            if j.startswith("ERROR"):
                lister_error.append(j)
        without_error = []
        for k in lister_error:
            remover = k.replace("ERROR", "")
            stripped = remover.strip()
            without_error.append(stripped)
        last_elements = without_error[-5:]
        print(f"Últimos \"ERROR\": {last_elements}")

contagem_severidades("log.txt", "log.txt")