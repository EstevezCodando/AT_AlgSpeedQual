import os
import random


def gerar_precos(nome_arquivo: str, quantidade: int):
    """
    Gera uma lista de preços aleatórios e salva em um arquivo.
    
    :param nome_arquivo: Caminho do arquivo onde os preços serão salvos.
    :param quantidade: Quantidade de preços a serem gerados.
    """
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(quantidade):
            preco = round(random.uniform(1.0, 1000.0), 2)  # Preço entre 1.00 e 1000.00
            arquivo.write(f"{preco}\n")


gerar_precos("registros/precos_1k.txt", 1000)
gerar_precos("registros/precos_10k.txt", 10000)

