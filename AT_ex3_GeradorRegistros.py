import os
from faker import Faker

fake = Faker()

# Função para gerar registros aleatórios
def gerar_registros_aleatorios(nome_arquivo: str, quantidade: int = 1000):
    # Garantir que o diretório exista
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

    # Gerar registros e salvar no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(quantidade):
            nome = fake.name()
            telefone = fake.phone_number()
            arquivo.write(f"{nome},{telefone}\n")

# Gerar o arquivo de registros
gerar_registros_aleatorios("registros/registrosContatos.txt")