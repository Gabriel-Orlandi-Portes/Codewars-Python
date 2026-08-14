def correct(s):
    resultado = ''
    for i in s:
        if i == '5':
            resultado += 'S'
        elif i == '0':
            resultado += 'O'
        elif i == '1':
            resultado += 'I'
        else:
            resultado += i
    
    return resultado