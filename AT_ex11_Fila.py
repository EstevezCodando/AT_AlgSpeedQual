from collections import deque
import csv

class SistemaAtendimento:
    def __init__(self):
        """
        Inicializa o sistema de atendimento com uma fila.
        """
        self.fila = deque()

    def carregar_chamados(self, nome_arquivo):
        """
        Carrega os chamados de um arquivo CSV e os adiciona à fila.
        
        :param nome_arquivo: Caminho do arquivo CSV contendo os chamados.
        """
        with open(nome_arquivo, 'r') as arquivo_csv:
            reader = csv.DictReader(arquivo_csv)
            for linha in reader:
                # Adicionar cada chamado à fila
                self.fila.append(linha)

    def adicionar_chamado(self, chamado):
        """
        Adiciona um chamado à fila.
        
        :param chamado: Dicionário contendo as informações do chamado.
        """
        self.fila.append(chamado)
        print(f"Chamado '{chamado['id_chamado']}' adicionado à fila.")

    def atender_chamado(self):
        """
        Atende e remove o chamado mais antigo da fila.
        
        :return: O chamado atendido ou uma mensagem indicando que a fila está vazia.
        """
        if self.fila:
            chamado = self.fila.popleft()
            print(f"Chamado '{chamado['id_chamado']}' atendido.")
            return chamado
        else:
            print("Nenhum chamado na fila para atender.")
            return None

    def exibir_fila(self):
        """
        Exibe o estado atual da fila de chamados.
        
        :return: Lista com os chamados na fila.
        """
        return list(self.fila)





# Criar o sistema de atendimento
sistema = SistemaAtendimento()

# Carregar chamados do arquivo CSV
sistema.carregar_chamados("registros/chamados.csv")

# Exibir os 5 primeiros chamados da fila
print("Chamados na fila inicial:")
for chamado in sistema.exibir_fila()[:5]:
    print(chamado)

# Simular atendimento de 3 chamados
print("\nAtendendo chamados:")
for _ in range(3):
    sistema.atender_chamado()

# Adicionar um novo chamado
novo_chamado = {
    "id_chamado": "101",
    "cliente": "Novo Cliente",
    "data_abertura": "2023-12-06",
    "prioridade": "Alta",
    "descricao": "Problema crítico reportado."
}
sistema.adicionar_chamado(novo_chamado)

# Exibir estado atual da fila
print("\nEstado atual da fila:")
for chamado in sistema.exibir_fila():
    print(chamado)
