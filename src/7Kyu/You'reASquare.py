import math

def is_square(n):
    if n < 0:
        return False

    raiz = math.sqrt(n)
    return raiz == int(raiz)