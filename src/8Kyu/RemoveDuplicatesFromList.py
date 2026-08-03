def distinct(seq):
    sequencia = []
    for i in seq:
        if i not in sequencia:
            sequencia.append(i)
        else:
            pass
    
    return sequencia