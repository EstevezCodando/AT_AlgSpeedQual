import os
import csv
from faker import Faker

fake = Faker()

# Gerador de registros de pessoas para rede social
def gerar_registros_redesocial(nome_arquivo: str, quantidade: int):
    """
    Gera registros de pessoas com atributos aleatórios e salva em um arquivo CSV.
    
    :param nome_arquivo: Caminho do arquivo onde os registros serão salvos.
    :param quantidade: Quantidade de registros a serem gerados.
    """
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        # Escrever cabeçalhos
        writer.writerow(["id", "username", "nome", "email", "idade", "cidade"])
        
        # Gerar registros
        for i in range(1, quantidade + 1):
            id_pessoa = i
            username = fake.user_name()
            nome = fake.name()
            email = fake.email()
            idade = fake.random_int(min=18, max=80)
            cidade = fake.city()
            
            # Escrever registro no CSV
            writer.writerow([id_pessoa, username, nome, email, idade, cidade])

# Gerar registros e salvar no arquivo
gerar_registros_redesocial("registros/redesocial.csv", 1000)

