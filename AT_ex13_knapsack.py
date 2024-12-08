def knapsack(capacidade, pesos, valores, n):
    """
    Resolve o problema da mochila usando programação dinâmica.
    
    :param capacidade: Capacidade máxima da mochila.
    :param pesos: Lista dos pesos dos itens.
    :param valores: Lista dos valores dos itens.
    :param n: Número de itens disponíveis.
    :return: O valor máximo que pode ser carregado na mochila.
    """
    # Criar uma matriz para armazenar os resultados dos subproblemas
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preencher a matriz iterativamente
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]


# Dados de exemplo
pesos = [1, 2, 3, 2]
valores = [10, 15, 40, 25]
capacidade = 5
n = len(pesos)

# Resolver o problema da mochila
resultado = knapsack(capacidade, pesos, valores, n)
print(resultado)
