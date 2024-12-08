class Node:
    def __init__(self, key):
        """
        Inicializa um nó da árvore binária.
        
        :param key: Valor (nota do estudante).
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
        
        :param key: Valor (nota) a ser inserido.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._inserir(self.root, key)

    def _inserir(self, current_node, key):
        """
        Insere um valor de forma recursiva.
        
        :param current_node: Nó atual da árvore.
        :param key: Valor (nota) a ser inserido.
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

    def encontrar_minimo(self):
        """
        Encontra o valor mínimo na árvore.
        
        :return: Valor mínimo (nota).
        """
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.key

    def encontrar_maximo(self):
        """
        Encontra o valor máximo na árvore.
        
        :return: Valor máximo (nota).
        """
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.key


# Implementação da árvore
notas = [85, 70, 95, 60, 75, 90, 100]
bst = BST()

# Inserir as notas na árvore
for nota in notas:
    bst.inserir(nota)

# Encontrar as notas mínima e máxima
nota_minima = bst.encontrar_minimo()
nota_maxima = bst.encontrar_maximo()

print("Nota Minima: ", nota_minima," Nota Maxima: ", nota_maxima)
