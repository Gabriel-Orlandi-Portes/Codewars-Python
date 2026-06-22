def accum(st):
    resultado = []

    for i in range(len(st)):
        bloco = st[i].upper() + st[i].lower() * i
        resultado.append(bloco)

    return "-".join(resultado)