class HashTable:
    def __init__(self, tamanho=1000):
        """
        Inicializa a tabela hash com um tamanho definido.
        
        :param tamanho: Tamanho da tabela hash.
        """
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanho = tamanho

    def hash_func(self, chave):
        """
        Função de hash simples que retorna o índice da tabela.
        
        :param chave: Chave para calcular o hash.
        :return: Índice na tabela hash.
        """
        return hash(chave) % self.tamanho

    def inserir(self, chave):
        """
        Insere uma chave na tabela hash, se ainda não estiver presente.
        
        :param chave: Chave a ser inserida.
        """
        indice = self.hash_func(chave)
        if chave not in self.tabela[indice]:
            self.tabela[indice].append(chave)

    def contem(self, chave):
        """
        Verifica se a chave está na tabela hash.
        
        :param chave: Chave a ser verificada.
        :return: True se a chave estiver presente, False caso contrário.
        """
        indice = self.hash_func(chave)
        return chave in self.tabela[indice]


def verificar_duplicatas(lista):
    """
    Verifica se há duplicatas em uma lista usando uma tabela hash personalizada.
    
    :param lista: Lista de elementos a ser verificada.
    :return: True se houver duplicatas, False caso contrário.
    """
    tabela_hash = HashTable()
    for elemento in lista:
        if tabela_hash.contem(elemento):
            return True
        tabela_hash.inserir(elemento)
    return False


# Exemplo de uso
lista_teste = [1, 2, 3, 4, 5, 6, 2]
resultado = verificar_duplicatas(lista_teste)
print("Há duplicatas:", resultado)
