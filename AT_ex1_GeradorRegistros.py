import os
import random
import string
from faker import Faker

faker = Faker()

# Função para gerar registros aleatórios
def gerar_registros_aleatorios(nome_arquivo: str, quantidade: int = 10000):
    # Garantir que o diretório exista
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    
    # Gerar registros e salvar no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(quantidade):
            id_produto = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            nome_produto = faker.word().capitalize() + " " + faker.word().capitalize()
            preco = round(random.uniform(10, 1000), 2)
            arquivo.write(f"{id_produto},{nome_produto},{preco}\n")

# Gerar o arquivo de registros
gerar_registros_aleatorios("registros/registros.txt")