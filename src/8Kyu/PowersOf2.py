def powers_of_two(n):
    resul = []
    
    for i in range(0, n+1, 1):
        pot = 2 ** i
        resul.append(pot)
    
    return resul
    
    
