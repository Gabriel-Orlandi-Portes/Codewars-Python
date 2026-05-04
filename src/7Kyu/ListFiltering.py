def filter_list(l):
    nova_lista = []
    
    for item in l:
        if type(item) != str:
            nova_lista.append(item)
    
    return nova_lista