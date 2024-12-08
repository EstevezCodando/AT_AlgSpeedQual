class Node:
    def __init__(self, key):
        """
        Inicializa um nó da árvore binária.
        
        :param key: Valor (código do produto).
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
        Insere uma nova chave na árvore binária.
        
        :param key: Código do produto a ser inserido.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._inserir(self.root, key)

    def _inserir(self, current_node, key):
        """
        Insere um valor de forma recursiva.
        
        :param current_node: Nó atual da árvore.
        :param key: Código do produto a ser inserido.
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

    def remover(self, key):
        """
        Remove uma chave da árvore binária.
        
        :param key: Código do produto a ser removido.
        """
        self.root = self._remover(self.root, key)

    def _remover(self, current_node, key):
        """
        Remove um valor de forma recursiva.
        
        :param current_node: Nó atual da árvore.
        :param key: Código do produto a ser removido.
        :return: O nó atualizado.
        """
        if current_node is None:
            return current_node

        if key < current_node.key:
            current_node.left = self._remover(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._remover(current_node.right, key)
        else:
            # Caso 1: Nó folha
            if current_node.left is None and current_node.right is None:
                return None

            # Caso 2: Nó com um filho
            if current_node.left is None:
                return current_node.right
            if current_node.right is None:
                return current_node.left

            # Caso 3: Nó com dois filhos
            successor = self._min_value_node(current_node.right)
            current_node.key = successor.key
            current_node.right = self._remover(current_node.right, successor.key)

        return current_node

    def _min_value_node(self, node):
        """
        Encontra o menor valor na subárvore à direita.
        
        :param node: Nó raiz da subárvore.
        :return: Nó com o menor valor.
        """
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def exibir_em_ordem(self):
        """
        Exibe os valores da árvore em ordem crescente.
        
        :return: Lista com os valores em ordem crescente.
        """
        resultados = []
        self._em_ordem(self.root, resultados)
        return resultados

    def _em_ordem(self, current_node, resultados):
        """
        Percorre a árvore em ordem crescente.
        
        :param current_node: Nó atual.
        :param resultados: Lista para armazenar os valores em ordem.
        """
        if current_node is not None:
            self._em_ordem(current_node.left, resultados)
            resultados.append(current_node.key)
            self._em_ordem(current_node.right, resultados)


# Implementação da árvore
codigos = [45, 25, 65, 20, 30, 60, 70]
bst = BST()

# Inserir os códigos na árvore
for codigo in codigos:
    bst.inserir(codigo)

# Remoção e exibição
resultados = {}

# Remover 20 (nó folha)
bst.remover(20)
resultados["Após remover 20"] = bst.exibir_em_ordem()

# Remover 25 (nó com um filho)
bst.remover(25)
resultados["Após remover 25"] = bst.exibir_em_ordem()

# Remover 45 (nó com dois filhos)
bst.remover(45)
resultados["Após remover 45"] = bst.exibir_em_ordem()

print(resultados)
