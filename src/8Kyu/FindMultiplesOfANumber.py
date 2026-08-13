def find_multiples(integer, limit):
    lista = []
    for i in range(1, limit+1, 1):
        conta = i * integer
        if conta <= limit:
            lista.append(conta)
        else:
            break
    
    return lista
        