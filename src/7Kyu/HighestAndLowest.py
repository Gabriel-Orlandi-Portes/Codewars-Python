def high_and_low(numbers):
    numbers = numbers.split()

    lista = []

    for i in numbers:
        lista.append(int(i))

    high = lista[0]
    low = lista[0]

    for i in lista:
        if i > high:
            high = i

        if i < low:
            low = i

    return f"{high} {low}"
