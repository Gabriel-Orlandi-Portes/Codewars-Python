def min_value(digits):
    numeros = set(digits)
    numeros = sorted(numeros)

    resultado = ""

    for numero in numeros:
        resultado += str(numero)

    return int(resultado)