def str_count(strng, letter):
    contagem = 0
    for i in strng:
        if i == letter:
            contagem += 1
    return contagem
        