
import os 
import csv  
from faker import Faker
import random  
from datetime import datetime, timedelta

fake = Faker()

def gerar_registros_chamados_ordenados(nome_arquivo: str, quantidade: int):
    """
    Gera registros de chamados com informações aleatórias em ordem cronológica 
    e salva em um arquivo CSV.
    
    :param nome_arquivo: Caminho do arquivo onde os registros serão salvos.
    :param quantidade: Quantidade de registros de chamados a serem gerados.
    """
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        # Escrever cabeçalhos
        writer.writerow(["id_chamado", "cliente", "data_abertura", "prioridade", "descricao"])
        
        # Gerar registros com datas em ordem cronológica
        data_atual = datetime.today() - timedelta(days=180)  # Começar 6 meses atrás
        for i in range(1, quantidade + 1):
            id_chamado = i
            cliente = fake.name()
            data_abertura = data_atual.strftime("%Y-%m-%d")
            prioridade = random.choice(["Baixa", "Média", "Alta", "Crítica"])
            descricao = fake.sentence(nb_words=10)
            
            # Incrementar a data para manter a ordem cronológica
            data_atual += timedelta(days=random.randint(1, 5))
            
            # Escrever registro no CSV
            writer.writerow([id_chamado, cliente, data_abertura, prioridade, descricao])

# Gerar registros de chamados e salvar no arquivo
gerar_registros_chamados_ordenados("registros/chamados.csv", 10)

"registros/chamados.csv"  # Caminho do arquivo gerado.
