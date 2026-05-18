def find_needle(haystack):
    indice = 0
    for i in haystack:  
        if i == 'needle':
            return f'found the needle at position {indice}'
        else:
            indice +=1
        
