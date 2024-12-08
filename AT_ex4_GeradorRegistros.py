import os
import random
from faker import Faker

fake = Faker()

# Função para gerar livros aleatórios
def gerar_livros_aleatorios(nome_arquivo: str, quantidade: int = 100000):
    """
    Gera uma lista de livros com títulos, autores e ISBNs únicos.
    Salva os livros em um arquivo no formato ordenado por ISBN.
    
    :param nome_arquivo: Caminho do arquivo onde os livros serão salvos.
    :param quantidade: Quantidade de livros a serem gerados.
    """
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    livros = []

    for _ in range(quantidade):
        titulo = fake.catch_phrase()
        autor = fake.name()
        isbn = fake.unique.isbn13(separator="-")
        livros.append((isbn, titulo, autor))

    # Ordenar os livros pelo ISBN
    livros.sort(key=lambda x: x[0])

    # Salvar no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        for isbn, titulo, autor in livros:
            arquivo.write(f"{isbn},{titulo},{autor}\n")

# Gerar a lista de livros ordenada por ISBN
gerar_livros_aleatorios("registros/livrosOrdenados.txt")
