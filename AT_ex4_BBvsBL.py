import os
import csv

# Função para carregar livros do arquivo
def carregar_livros(nome_arquivo: str):
    """
    Carrega a lista de livros de um arquivo e retorna como uma lista de dicionários.
    
    :param nome_arquivo: Caminho do arquivo contendo os livros.
    :return: Lista de dicionários com ISBN, título e autor.
    """
    livros = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            isbn, titulo, autor = linha.strip().split(",", 2)
            livros.append({"isbn": isbn, "titulo": titulo, "autor": autor})
    return livros

# Algoritmo de busca binária
def busca_binaria(livros, isbn_procurado):
    """
    Realiza uma busca binária para encontrar um livro pelo ISBN.
    
    :param livros: Lista de livros ordenada por ISBN.
    :param isbn_procurado: ISBN do livro a ser buscado.
    :return: O livro encontrado ou None se não for encontrado.
    """
    esquerda, direita = 0, len(livros) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        isbn_atual = livros[meio]["isbn"]
        if isbn_atual == isbn_procurado:
            return livros[meio]
        elif isbn_atual < isbn_procurado:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

# Algoritmo de busca linear
def busca_linear(livros, isbn_procurado):
    """
    Realiza uma busca linear para encontrar um livro pelo ISBN.
    
    :param livros: Lista de livros.
    :param isbn_procurado: ISBN do livro a ser buscado.
    :return: O livro encontrado ou None se não for encontrado.
    """
    for livro in livros:
        if livro["isbn"] == isbn_procurado:
            return livro
    return None

# Carregar os livros gerados
livros_ordenados = carregar_livros("registros/livrosOrdenados.txt")

# Escolher um ISBN aleatório para buscar
isbn_a_buscar = livros_ordenados[50000]["isbn"]

# Medir o tempo de execução das buscas
import time

# Busca binária
inicio_binaria = time.time()
resultado_binaria = busca_binaria(livros_ordenados, isbn_a_buscar)
tempo_binaria = time.time() - inicio_binaria

# Busca linear
inicio_linear = time.time()
resultado_linear = busca_linear(livros_ordenados, isbn_a_buscar)
tempo_linear = time.time() - inicio_linear

# Criar a pasta de saída, se não existir
os.makedirs("saidas", exist_ok=True)

# Salvar resultados no arquivo CSV
saida_csv = "saidas/ex_4.csv"

# Dados a serem salvos
dados = [
    ["ISBN buscado", isbn_a_buscar],
    ["Resultado Busca Binária", resultado_binaria],
    ["Tempo Busca Binária", tempo_binaria],
    ["Resultado Busca Linear", resultado_linear],
    ["Tempo Busca Linear", tempo_linear]
]

# Escrever no arquivo CSV
with open(saida_csv, mode='w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(["Descrição", "Valor"])
    for descricao, valor in dados:
        writer.writerow([descricao, valor])

saida_csv

