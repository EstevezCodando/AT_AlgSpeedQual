def carregar_registros(nome_arquivo: str):
    """
    Carrega os registros de jogadores de um arquivo.
    
    :param nome_arquivo: Caminho do arquivo com os registros.
    :return: Lista de dicionários contendo nome e pontuação.
    """
    registros = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, pontuacao = linha.strip().split(",")
            registros.append({"nome": nome, "pontuacao": int(pontuacao)})
    return registros

def selection_sort(jogadores):
    """
    Ordena os jogadores por pontuação usando o algoritmo Selection Sort.
    
    :param jogadores: Lista de jogadores (dicionários com nome e pontuação).
    :return: Lista ordenada por pontuação.
    """
    n = len(jogadores)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if jogadores[j]["pontuacao"] < jogadores[min_idx]["pontuacao"]:
                min_idx = j
        jogadores[i], jogadores[min_idx] = jogadores[min_idx], jogadores[i]
    return jogadores

# Carregar os registros gerados
jogadores = carregar_registros("registros/registros_jogadores.txt")

# Ordenar os registros com Selection Sort
jogadores_ordenados = selection_sort(jogadores)

# Visualizar os registros ordenados (exibindo os 10 primeiros)
print(jogadores_ordenados[:10])
