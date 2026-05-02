def get_sum(a, b):
    soma = 0
    for i in range(min(a, b), max(a, b) + 1):
        soma += i
    return soma