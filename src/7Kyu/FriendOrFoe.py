def friend(x):
    amigo = []
    
    for nome in x:
        if len(nome) == 4:
            amigo.append(nome)
    
    return amigo
