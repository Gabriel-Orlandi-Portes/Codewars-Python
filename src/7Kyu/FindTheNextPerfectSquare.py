def find_next_square(sq):
    raiz = sq ** 0.5

    if raiz.is_integer():
        proxima_raiz = raiz + 1
        proximo_quadrado = proxima_raiz ** 2

        return proximo_quadrado

    return -1