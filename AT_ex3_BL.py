# Função para carregar contatos do arquivo
def carregar_contatos_de_arquivo(nome_arquivo):
    """
    Carrega os contatos de um arquivo e os organiza em uma lista de dicionários.

    :param nome_arquivo: Caminho do arquivo contendo os contatos.
    :return: Lista de dicionários representando os contatos.
    """
    contatos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, telefone = linha.strip().split(",", 1)  # Dividir por vírgula
            contatos.append({"nome": nome, "telefone": telefone})
    return contatos

# Algoritmo de busca linear
def buscar_contato_por_nome(contatos, nome_procurado):
    """
    Realiza a busca linear de um contato pelo nome.

    :param contatos: Lista de contatos (dicionários com nome e telefone).
    :param nome_procurado: Nome do contato a ser buscado.
    :return: Telefone do contato se encontrado, ou None caso contrário.
    """
    for contato in contatos:
        if contato["nome"] == nome_procurado:
            return contato["telefone"]
    return None

# Carregar lista de contatos do arquivo
contatos_gerados = carregar_contatos_de_arquivo("registros/registrosContatos.txt")

# Testar busca
nome_a_buscar = contatos_gerados[10]["nome"]  # Pegando um nome existente para testar
telefone_encontrado = buscar_contato_por_nome(contatos_gerados, nome_a_buscar)

# Resultados
print(f"Nome buscado: {nome_a_buscar}")
print(f"Telefone encontrado: {telefone_encontrado}")
