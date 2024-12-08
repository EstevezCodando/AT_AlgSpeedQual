class NoArvore:
    """
    Classe que representa um nó da Árvore de Busca Binária.
    """
    def __init__(self, chave, dados):
        self.chave = chave  # Chave usada para comparação (ID do produto neste caso)
        self.dados = [dados]  # Lista de dados (para armazenar duplicados)
        self.esquerda = None  # Filho à esquerda
        self.direita = None  # Filho à direita


class ArvoreBuscaBinaria:
    """
    Implementação de uma Árvore de Busca Binária para armazenar registros de produtos.
    """
    def __init__(self):
        self.raiz = None  # Raiz da árvore

    def inserir(self, chave, dados):
        """
        Insere um novo nó na Árvore de Busca Binária.
        :param chave: Chave do nó (usada para comparação)
        :param dados: Dados a serem armazenados no nó
        """
        if self.raiz is None:
            self.raiz = NoArvore(chave, dados)
        else:
            self._inserir(self.raiz, chave, dados)

    def _inserir(self, no, chave, dados):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = NoArvore(chave, dados)
            else:
                self._inserir(no.esquerda, chave, dados)
        elif chave > no.chave:
            if no.direita is None:
                no.direita = NoArvore(chave, dados)
            else:
                self._inserir(no.direita, chave, dados)
        else:
            no.dados.append(dados)

    def buscar(self, chave):
        """
        Busca um nó pela sua chave na Árvore de Busca Binária.
        :param chave: Chave a ser buscada
        :return: Lista de dados associados à chave ou None se não encontrado
        """
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.dados
        elif chave < no.chave:
            return self._buscar(no.esquerda, chave)
        else:
            return self._buscar(no.direita, chave)


# Função para carregar os registros do arquivo para a árvore
def carregar_registros_para_arvore(nome_arquivo: str):
    arvore = ArvoreBuscaBinaria()
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            id_produto, nome_produto, preco = linha.strip().split(',')
            arvore.inserir(id_produto, {"nome": nome_produto, "preco": float(preco)})
    return arvore


# Carregar a árvore com os registros gerados
arvore_produtos = carregar_registros_para_arvore("registros/registros.txt")

# A árvore agora está pronta para buscas
a =arvore_produtos.buscar('00213LVNLG')
print(a)


def listar_todos_ids(arvore):
    nomes = []

    def em_ordem(no):
        if no is not None:
            em_ordem(no.esquerda)
            nomes.append(no.dados)
            em_ordem(no.direita)

    em_ordem(arvore.raiz)
    return nomes

# Listar todos os IDs na árvore
todos_ids = listar_todos_ids(arvore_produtos)
print("IDs armazenados na árvore:", todos_ids[:20])  # Exibe os primeiros 20 IDs para inspeção

