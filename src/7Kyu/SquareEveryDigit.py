def square_digits(num):
    resultado = ""

    for i in str(num):
        resultado += str(int(i) ** 2)

    return int(resultado)
