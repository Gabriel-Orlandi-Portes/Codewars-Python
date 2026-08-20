def queue_time(customers, n):
    caixas = [0] * n

    for cliente in customers:
        menor_caixa = caixas.index(min(caixas))
        caixas[menor_caixa] += cliente

    return max(caixas)