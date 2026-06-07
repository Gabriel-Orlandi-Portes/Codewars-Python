def sort_array(source_array):
    impares = []

    for num in source_array:
        if num % 2 != 0:
            impares.append(num)

    impares.sort()

    indice = 0

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = impares[indice]
            indice += 1

    return source_array