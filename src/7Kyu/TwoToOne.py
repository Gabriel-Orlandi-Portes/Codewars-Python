def longest(a1, a2):
    letras = set(a1 + a2)
    resultado = ""

    for letra in sorted(letras):
        resultado += letra

    return resultado