def sum_array(arr):

    if not arr or len(arr) <= 1:
        return 0

    maior = arr[0]
    menor = arr[0]

    for i in arr:
        if i > maior:
            maior = i

        if i < menor:
            menor = i

    soma = 0
    for i in arr:
        soma += i

    total = soma - maior - menor

    return total
