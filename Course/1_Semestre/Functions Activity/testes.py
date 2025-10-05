import Listas as l

assert l.criar_lista() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

assert l.adicionar_elemento([1, 2, 3, 4, 5, 6], 7) == [1, 2, 3, 4, 5, 6, 7]
assert l.adicionar_elemento(["Flamengo", "Vasco", "Palmeiras"], "Corinthians") == ["Flamengo", "Vasco", "Palmeiras", "Corinthians"]
assert l.adicionar_elemento([4.5, 2.9, 7.3, 5.8, 53.67], 8.3) == [4.5, 2.9, 7.3, 5.8, 53.67, 8.3]

assert l.remover_elemento([4, 6, 43, 8, 10], 43) == [4, 6, 8, 10]
assert l.remover_elemento([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
assert l.remover_elemento(["Não", "remova", "o", "nome", "Carlos", "daqui"], "Carlos") == ["Não", "remova", "o", "nome", "daqui"]

assert l.contar_ocorrencias([200, 500, 400, 200, 200, 800], 200) == 3
assert l.contar_ocorrencias(["pão", "linguiçeta", "linguiçeta", "molho", "pão"], "linguiçeta") == 2
assert l.contar_ocorrencias([7, 5, 9, 4, 6, 3], 4) == 1

assert l.contem_elemento(["Vermelho", "Verde", "Ciano", "Roxo"], "Ciano") == True
assert l.contem_elemento([7, 4, 2, 0], 1) == False
assert l.contem_elemento(["Pai", "Mãe", "Filho", "Filha"], "Filho") == True

assert l.inverter_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert l.inverter_lista([33, 50, 57, 1, 4]) == [4, 1, 57, 50, 33]
assert l.inverter_lista(["Robert", "Thalia", "Arnaldo", "Sérgio"]) == ["Sérgio", "Arnaldo", "Thalia", "Robert"]

assert l.ordenar_crescente([50, 40, 30, 20, 10]) == [10, 20, 30, 40, 50]
assert l.ordenar_crescente([100, 95, 90, 85, 80]) == [80, 85, 90, 95, 100]
assert l.ordenar_crescente([29, 48, 67, 17]) == [17, 29, 48, 67]

assert l.ordenar_crescente([50, 40, 30, 20, 10]) == [10, 20, 30, 40, 50]
assert l.ordenar_crescente([100, 95, 90, 85, 80]) == [80, 85, 90, 95, 100]
assert l.ordenar_crescente([29, 48, 67, 17]) == [17, 29, 48, 67]

assert l.somar_lista([1, 3, 5, 7, 9]) == 25
assert l.somar_lista([2, 4, 6, 8]) == 20
assert l.somar_lista([3, 7, 11]) == 21

assert l.media_lista([3.5, 6.7, 9.2, 1.7]) == 5.3
assert l.media_lista([1, 2, 3]) == 2.0
assert l.media_lista([7.8, 5.4, 9.1, 6.3, 8.0]) == 7.3

assert l.filtrar_pares([4, 9, 12, 7, 6, 15, 8]) == [4, 12, 6, 8]
assert l.filtrar_pares([1, 2, 3, 5, 8, 13, 21]) == [2, 8]
assert l.filtrar_pares([10, 3, 14, 7, 2, 11, 6]) == [10, 14, 2, 6]

assert l.quadrados([-3, 0, 1.5, 2, -4.2, 5, 7.1]) == [9, 0, 2.25, 4, 17.64, 25, 50.41]
assert l.quadrados([2, 3, 5, 7, 11, 13, 17]) == [4, 9, 25, 49, 121, 169, 289]
assert l.quadrados([4, 1.2, -5, 0, 3.5, 6]) == [16, 1.44, 25, 0, 12.25, 36]

assert l.copiar_lista(["O", "professor", "Duda", "é", "sensacional"]) == ["O", "professor", "Duda", "é", "sensacional"]
assert l.copiar_lista(["Suas", "aulas", "são", "sempre", "incríveis"]) == ["Suas", "aulas", "são", "sempre", "incríveis"]
assert l.copiar_lista(["Duda", "me", "dá", "um", "estágio"]) == ["Duda", "me", "dá", "um", "estágio"]

assert l.concatenar_listas(["O", "Duda", "é"], ["mais", "arretado", "que", "pimenta", "malagueta!"]) == ["O", "Duda", "é", "mais", "arretado", "que", "pimenta", "malagueta!"]
assert l.concatenar_listas(["O", "Duda", "é"], ["BARRIL", "DOBRADO"]) == ["O", "Duda", "é", "BARRIL", "DOBRADO"]
assert l.concatenar_listas(["O", "Duda", "é"], ["um", "cabra", "da", "peste"]) == ["O", "Duda", "é", "um", "cabra", "da", "peste"]

assert l.limpar_lista([17, 13, 11, 7, 5, 3, 2]) == []
assert l.limpar_lista([49, 6.25, 0.64, 100, 1, 9]) == []
assert l.limpar_lista([9, -4, 2.2, 0, 5.5, -3]) == []

import Matrizes as m

assert m.criar_matriz_3x3() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert m.soma_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
assert m.soma_matriz([[10, 20, 30], [40, 50, 60], [70, 80, 90]]) == 450
assert m.soma_matriz([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 5

assert m.maior_menor_matriz([[1, 2], [3, 4]]) == (4, 1)
assert m.maior_menor_matriz([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == (9, 1)
assert m.maior_menor_matriz([[0, -10], [20, 5]]) == (20, -10)

assert m.diagonal_principal([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]) == [1, 13, 15, 7]
assert m.diagonal_principal([[2, 3, 5, 7], [43, 0, 0, 11], [41, 0, 0, 13], [37, 31, 29, 17]]) == [2, 0, 0, 17]
assert m.diagonal_principal([['H', '*', '*', '*', '*'], ['*', 'E', '*', '*', '*'], ['*', '*', 'L', '*', '*'], ['*', '*', '*', 'L', '*'], ['*', '*', '*', '*', 'O']]) == ['H', 'E', 'L', 'L', 'O']

assert m.diagonal_secundaria([[0, 0, 0, 0, 'W'], [0, 0, 0, 'O', 0], [0, 0, 'R', 0, 0], [0, 'L', 0, 0, 0], ['D', 0, 0, 0, 0]]) == ['W', 'O', 'R', 'L', 'D']
assert m.diagonal_secundaria([['-', '-', '-', '-', 'S'], ['-', '-', '-', 'T', '-'], ['-', '-', 'A', '-', '-'], ['-', 'R', '-', '-', '-'], ['T', '-', '-', '-', '-']]) == ['S', 'T', 'A', 'R', 'T']
assert m.diagonal_secundaria([['.', '.', '.', 'H'], ['.', '.', 'E', '.'], ['.', 'R', '.', '.'], ['E', '.', '.', '.']]) == ['H', 'E', 'R', 'E']

assert m.transposta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert m.transposta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
assert m.transposta([[7]]) == [[7]]

assert m.matriz_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) == True
assert m.matriz_simetrica([[1, 2, 3], [0, 4, 5], [7, 8, 9]]) == False
assert m.matriz_simetrica([[5, 0, 7], [0, 4, 5], [7, 5, 7]]) == True

assert m.multiplicar_matriz([[1, 2], [3, 4]], 2) == [[2, 4], [6, 8]]
assert m.multiplicar_matriz([[0, -1], [5, 7]], 3) == [[0, -3], [15, 21]]
assert m.multiplicar_matriz([[10]], 5) == [[50]]

assert m.contar_pares_matriz([[1, 2], [3, 4]]) == 2
assert m.contar_pares_matriz([[2, 4], [6, 8]]) == 4
assert m.contar_pares_matriz([[1, 3], [5, 7]]) == 0

assert m.matriz_identidade(1) == [[1]]
assert m.matriz_identidade(2) == [[1, 0], [0, 1]]
assert m.matriz_identidade(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

assert m.soma_linhas([[3, 6, 9], [12, 15, 18], [21, 24, 27]]) == [18, 45, 72]
assert m.soma_linhas([[1, 2, 4], [8, 16, 32], [64, 128, 256]]) == [7, 56, 448] 
assert m.soma_linhas([[1, 3, 5], [7, 9, 11], [13, 15, 17]]) == [9, 27, 45] 

assert m.soma_colunas([[3, 6, 9], [12, 15, 18], [21, 24, 27]]) == [36, 45, 54]
assert m.soma_colunas([[1, 4, 9], [16, 25, 36], [49, 64, 81]]) == [66, 93, 126]
assert m.soma_colunas([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == [18, 15, 12]

assert m.contem_valor([[4, 7, 2], [9, 1, 6], [3, 8, 5]], 10) == False
assert m.contem_valor([['😊', '🚀', '🌟'], ['🔥', '💡', '🎯'], ['📚', '🎵', '🌍']], '💡') == True
assert m.contem_valor([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 'H') == True

assert m.substituir_negativos([[1, -2], [-3, 4]]) == [[1, 0], [0, 4]]
assert m.substituir_negativos([[0, -1], [-5, -6]]) == [[0, 0], [0, 0]]
assert m.substituir_negativos([[2, 3], [4, 5]]) == [[2, 3], [4, 5]]


import Dicionários as d

assert d.obter_valor({"nome": "Ana", "idade": 25}, "idade") == 25
assert d.obter_valor({"cidade": "Recife", "estado": "PE"}, "país") == None
assert d.obter_valor({}, "qualquer") == None

assert d.chave_existe({"dog": "chien", "cat": "chat", "rat": "souris", "horse": "cheval"}, "cat") == True
assert d.chave_existe({"nome": "Maria", "idade": 30, "cidade": "São Paulo"}, "estado") == False
assert d.chave_existe({"nome": "XR-17", "função": "exploração espacial", "ativo": True, "energia": 87.5, "ferramentas": ["laser", "braço mecânico", "analisador químico"]}, "função") == True

assert d.adicionar_par({"igreja": "Igreja Adventista do Sétimo Dia", "criador": "Deus", "profetisa": "Ellen G. White", "dia_de_culto": "sábado"}, "mensagem", "três anjos") == {"igreja": "Igreja Adventista do Sétimo Dia", "criador": "Deus", "profetisa": "Ellen G. White", "dia_de_culto": "sábado", "mensagem": "três anjos"}
assert d.adicionar_par({"livro": "Gênesis", "personagem": "Moisés", "versículo": "João 3:16", "tema": "redenção"}, "idioma_original", "hebraico") == {"livro": "Gênesis", "personagem": "Moisés", "versículo": "João 3:16", "tema": "redenção", "idioma_original": "hebraico"}
assert d.adicionar_par({"autora": "Ellen G. White", "livro_principal": "O Grande Conflito", "dom": "profecia", "instituição": "Casa Publicadora"}, "mensagem_central", "testemunho de Jesus") == {"autora": "Ellen G. White", "livro_principal": "O Grande Conflito", "dom": "profecia", "instituição": "Casa Publicadora", "mensagem_central": "testemunho de Jesus"}

assert d.remover_chave({"rede": "TCP/IP", "linguagem": "Python", "banco_dados": "PostgreSQL", "sistema": "Linux", "metodologia": "Scrum"}, "sistema") == {"rede": "TCP/IP", "linguagem": "Python", "banco_dados": "PostgreSQL", "metodologia": "Scrum"}
assert d.remover_chave({"linguagem": "JavaScript", "framework": "React", "estilo": "CSS", "markup": "HTML", "ferramenta": "Figma"}, "framework") == {"linguagem": "JavaScript", "estilo": "CSS", "markup": "HTML", "ferramenta": "Figma"}
assert d.remover_chave({"linguagem": "Python", "framework": "Django", "banco_dados": "MySQL", "api": "REST", "autenticação": "JWT"}, "api") == {"linguagem": "Python", "framework": "Django", "banco_dados": "MySQL", "autenticação": "JWT"}

assert d.contar_chaves({"idioma": "francês", "alfabeto": "latino", "saudação": "bonjour"}) == 3
assert d.contar_chaves({"cidade": "Paris", "comida": "croissant", "monumento": "Torre Eiffel", "arte": "Louvre", "festa": "14 juillet"})== 5
assert d.contar_chaves({"despedida": "au revoir", "educação": "politesse", "filósofo": "Voltaire", "escritor": "Victor Hugo", "música": "chanson française", "filme": "Amélie", "moda": "Haute couture"})== 7

assert d.inverter_dicionario({"lista": "dinâmica", "fila": "FIFO", "pilha": "LIFO", "grafo": "não direcionado"}) == {'dinâmica': 'lista', 'FIFO': 'fila', 'LIFO': 'pilha', 'não direcionado': 'grafo'}
assert d.inverter_dicionario({"modelo": "redes neurais", "algoritmos": 5, "campo": "machine learning", "ano_popularização": 2012}) == {'redes neurais': 'modelo', 5: 'algoritmos', 'machine learning': 'campo', 2012: 'ano_popularização'}
assert d.inverter_dicionario({"Windows": "Microsoft", "Linux": "comunidade", "macOS": "Apple", "processos": 128}) == {'Microsoft': 'Windows', 'comunidade': 'Linux', 'Apple': 'macOS', 128: 'processos'}

assert d.mesclar_dicionarios({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
assert d.mesclar_dicionarios({}, {"x": 9}) == {"x": 9}
assert d.mesclar_dicionarios({"x": 1}, {}) == {"x": 1}

assert d.contar_ocorrencias(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
assert d.contar_ocorrencias([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
assert d.contar_ocorrencias([]) == {}

assert d.chaves_em_ordem_alfabetica({'idioma': 'inglês', 'moeda': 'dólar', 'feriado': 'Thanksgiving'}) == ['feriado', 'idioma', 'moeda']
assert d.chaves_em_ordem_alfabetica({"esporte": "baseball", "bebida": "Coca-Cola", "música": "jazz", "comida": "fast-food"}) == ['bebida', 'comida', 'esporte', 'música']
assert d.chaves_em_ordem_alfabetica({"cidade": "New York", "comida": "hambúrguer", "cinema": "Hollywood", "universidade": "Harvard", "tecnologia": "Silicon Valley"}) == ['cidade', 'cinema', 'comida', 'tecnologia', 'universidade']

assert d.remover_chaves_vazias({"lanças": "", "frutas_coletadas": 75, "pedras_lisas": 33, "fogueiras_acesas": None, "gritos_de_guerra": 12}) == {"frutas_coletadas": 75, "pedras_lisas": 33,"gritos_de_guerra": 12}
assert d.remover_chaves_vazias({"campo": "ciência", "método": None, "ambiente": "universidade", "documento": "", "meta": None}) == {"campo": "ciência", "ambiente": "universidade"}
assert d.remover_chaves_vazias({"escola": "estoicismo", "século": -3, "pensador": None, "obras_estudadas": 7, "tema_central": "virtude"}) == {"escola": "estoicismo", "século": -3, "obras_estudadas": 7, "tema_central": "virtude"}

assert d.somar_valores({"adultos": 2, "crianças": 5, "adolescentes": 3}) == 10
assert d.somar_valores({"oxigenio": 120, "combustivel": 300, "kits_primeiros_socorros": 25, "rações": 80, "peças_de_reposição": 50}) == 575
assert d.somar_valores({"frascos_azuis": 13, "fios_soltos": 87, "robôs_quebrados": 4, "experimentos_falhos": 21}) == 125

assert d.maiores_que({"a": 10, "b": 5, "c": 20}, 8) == {"a": 10, "c": 20}
assert d.maiores_que({"x": 3, "y": 9, "z": 12}, 5) == {"y": 9, "z": 12}
assert d.maiores_que({"brasil": 211, "canada": 38, "méxico": 128}, 100) == {"brasil": 211, "méxico": 128}

assert d.agrupar_por_tamanho(["sol", "lua", "céu", "estrela", "mar"]) == {3: ["sol", "lua", "céu", "mar"], 7: ["estrela"]}
assert d.agrupar_por_tamanho(["oi", "tchau", "olá", "sim", "não"]) == {2: ["oi"], 5: ["tchau"], 3: ["olá", "sim", "não"]}
assert d.agrupar_por_tamanho([]) == {}

assert d.encontrar_chave_por_valor({"a": 1, "b": 2, "c": 3}, 2) == "b"
assert d.encontrar_chave_por_valor({"x": 10, "y": 20}, 30) == None
assert d.encontrar_chave_por_valor({}, 1) == None

assert d.contar_letras("Olá, mundo!") == {'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
assert d.contar_letras("A B C A B C") == {'a': 2, 'b': 2, 'c': 2}
assert d.contar_letras("") == {}