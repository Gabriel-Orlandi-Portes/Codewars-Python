def multi_table(number):
    resultado = ''
    
    for i in range(1, 11):
        if i != 10:  
            resultado += f'{i} * {number} = {i*number}' + '\n'
        else:
            resultado += f'{i} * {number} = {i*number}'
    
    return resultado
        