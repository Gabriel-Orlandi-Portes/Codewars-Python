def dig_pow(n, p):
    soma = 0

    for i in str(n):
        soma += int(i) ** p
        p += 1

    if soma % n == 0:
        return soma // n
    else:
        return -1