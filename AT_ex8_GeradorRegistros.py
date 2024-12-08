import os
import random

# 1. Gerar registros de jogadores
def gerar_registros_jogadores(nome_arquivo: str, quantidade: int):
    """
    Gera registros de jogadores com nome e pontuação aleatórios.
    
    :param nome_arquivo: Caminho do arquivo onde os registros serão salvos.
    :param quantidade: Quantidade de registros a serem gerados.
    """
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    with open(nome_arquivo, 'w') as arquivo:
        for i in range(quantidade):
            nome = f"Jogador_{i+1}"
            pontuacao = random.randint(0, 10000)  # Pontuações entre 0 e 10.000
            arquivo.write(f"{nome},{pontuacao}\n")

# Gerar um arquivo com registros de 100 jogadores
gerar_registros_jogadores("registros/registros_jogadores.txt", 100)
