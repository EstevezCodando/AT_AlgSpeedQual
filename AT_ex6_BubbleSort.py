import os
import random
import time
import csv


# Bubble Sort com medição de desempenho

def bubble_sort(precos):
    """
    Ordena uma lista de preços usando o algoritmo Bubble Sort.
    
    :param precos: Lista de preços a ser ordenada.
    :return: Lista ordenada.
    """
    n = len(precos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if precos[j] > precos[j + 1]:
                precos[j], precos[j + 1] = precos[j + 1], precos[j]
    return precos

def medir_desempenho_bubble_sort(nome_entrada: str, nome_saida: str):
    """
    Mede o tempo de execução do Bubble Sort em um conjunto de dados.
    
    :param nome_entrada: Arquivo contendo os preços a serem ordenados.
    :param nome_saida: Caminho do CSV onde os resultados serão salvos.
    """
    os.makedirs(os.path.dirname(nome_saida), exist_ok=True)

    # Carregar os preços do arquivo
    with open(nome_entrada, 'r') as arquivo:
        precos = [float(linha.strip()) for linha in arquivo]

    # Medir tempo de execução
    inicio = time.time()
    bubble_sort(precos)
    fim = time.time()
    tempo_execucao = fim - inicio

    # Salvar os resultados em CSV
    with open(nome_saida, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([nome_entrada, len(precos), tempo_execucao])

# Caminho do arquivo de saída
saida_csv = "saidas/ex6_dadosBubblesort.csv"

# Criar o arquivo CSV com cabeçalhos
with open(saida_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Arquivo", "Tamanho", "Tempo (s)"])

# Medir desempenho para os dois conjuntos de dados
medir_desempenho_bubble_sort("registros/precos_1k.txt", saida_csv)
medir_desempenho_bubble_sort("registros/precos_10k.txt", saida_csv)

saida_csv
