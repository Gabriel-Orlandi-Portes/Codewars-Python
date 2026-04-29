def fake_bin(x):
    sequencia = []
    for i in x:
        if int(i) < 5:
            sequencia.append('0')
        else:
            sequencia.append('1')
    return join(sequencia)
        
