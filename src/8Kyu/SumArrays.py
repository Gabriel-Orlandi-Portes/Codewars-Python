def sum_array(a):
    soma = 0
    if not a:
        return 0
    else:
        for i in a:
            soma += i
        
        return soma