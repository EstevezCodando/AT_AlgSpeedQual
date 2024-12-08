class NavegacaoNavegador:
    def __init__(self):
        """
        Inicializa duas pilhas: uma para o histórico (voltar) e outra para o futuro (avançar).
        """
        self.historico = []  # Pilha para armazenar páginas visitadas
        self.futuro = []  # Pilha para armazenar páginas futuras

    def visitar_pagina(self, pagina):
        """
        Adiciona uma nova página ao histórico e limpa a pilha de páginas futuras.
        
        :param pagina: URL da página a ser visitada.
        """
        if self.historico and self.historico[-1] == pagina:
            return  # Evita adicionar a mesma página consecutivamente
        self.historico.append(pagina)
        self.futuro.clear()

    def voltar(self):
        """
        Move uma página do histórico para a pilha de páginas futuras.
        
        :return: A página anterior ou uma mensagem indicando que não é possível voltar.
        """
        if len(self.historico) > 1:
            pagina_atual = self.historico.pop()
            self.futuro.append(pagina_atual)
            return self.historico[-1]  # Página anterior
        return "Não é possível voltar."

    def avancar(self):
        """
        Move uma página da pilha de páginas futuras de volta para o histórico.
        
        :return: A próxima página ou uma mensagem indicando que não é possível avançar.
        """
        if self.futuro:
            proxima_pagina = self.futuro.pop()
            self.historico.append(proxima_pagina)
            return proxima_pagina
        return "Não é possível avançar."

    def exibir_historico(self):
        """
        Exibe o histórico completo de navegação.
        
        :return: Lista de páginas no histórico.
        """
        return self.historico

    def exibir_futuro(self):
        """
        Exibe as páginas futuras disponíveis para avançar.
        
        :return: Lista de páginas futuras.
        """
        return self.futuro


# Exemplo de uso
navegador = NavegacaoNavegador()
navegador.visitar_pagina("pagina1.com")
navegador.visitar_pagina("pagina2.com")
navegador.visitar_pagina("pagina3.com")

# Voltar
voltar1 = navegador.voltar()  # Voltar para pagina2.com
voltar2 = navegador.voltar()  # Voltar para pagina1.com

# Avançar
avancar1 = navegador.avancar()  # Avançar para pagina2.com

# Visitar nova página
navegador.visitar_pagina("pagina4.com")

voltar2 = navegador.voltar()

# Exibir histórico e futuro
historico = navegador.exibir_historico()
futuro = navegador.exibir_futuro()

print(historico) # historico da pilha de paginas visitadas
print(futuro) # pagina 4 que foi visitada possivel pagina futura