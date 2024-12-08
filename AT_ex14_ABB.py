class Node:
    def __init__(self, key):
        """
        Inicializa um nó da árvore binária de busca.
        
        :param key: Chave (preço do produto).
        """
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        """
        Inicializa a árvore binária de busca.
        """
        self.root = None

    def inserir(self, key):
        """
        Insere uma nova chave na árvore binária de busca.
        
        :param key: Chave a ser inserida.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._inserir(self.root, key)

    def _inserir(self, current_node, key):
        """
        Insere uma chave de forma recursiva.
        
        :param current_node: Nó atual da árvore.
        :param key: Chave a ser inserida.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._inserir(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._inserir(current_node.right, key)

    def buscar(self, key):
        """
        Busca uma chave na árvore binária de busca.
        
        :param key: Chave a ser buscada.
        :return: True se a chave for encontrada, False caso contrário.
        """
        return self._buscar(self.root, key)

    def _buscar(self, current_node, key):
        """
        Busca uma chave de forma recursiva.
        
        :param current_node: Nó atual da árvore.
        :param key: Chave a ser buscada.
        :return: True se a chave for encontrada, False caso contrário.
        """
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._buscar(current_node.left, key)
        else:
            return self._buscar(current_node.right, key)


# Implementação da BST
precos = [100, 50, 150, 30, 70, 130, 170]
bst = BST()

# Inserir preços na árvore
for preco in precos:
    bst.inserir(preco)

# Verificar se o preço 70 está disponível
preco_disponivel = bst.buscar(70)
print(preco_disponivel)
