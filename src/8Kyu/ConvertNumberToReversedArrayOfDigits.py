def digitize(n):
    n = str(n)
    n = n[::-1]
    
    resultado = []
    
    for numero in n:
        resultado.append(int(numero))
    
    return resultado