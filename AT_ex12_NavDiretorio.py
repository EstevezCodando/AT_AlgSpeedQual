import os

def listar_arquivos_recursivamente(caminho):
    """
    Percorre todos os subdiretórios de um diretório dado e lista somente os arquivos.

    :param caminho: Caminho do diretório a ser percorrido.
    :return: Lista de caminhos absolutos de arquivos encontrados.
    """
    arquivos = []
    for item in os.listdir(caminho):
        item_caminho = os.path.join(caminho, item)
        if os.path.isfile(item_caminho):
            arquivos.append(item_caminho)
        elif os.path.isdir(item_caminho):
            arquivos.extend(listar_arquivos_recursivamente(item_caminho))
    return arquivos


diretorio_base = os.getcwd()  # Diretório atual para teste
arquivos_encontrados = listar_arquivos_recursivamente(diretorio_base)
print(arquivos_encontrados)
