def nb_dig(n, d):
    total = 0
    
    for k in range(n + 1):
        quadrado = str(k ** 2)
        total += quadrado.count(str(d))
    
    return total