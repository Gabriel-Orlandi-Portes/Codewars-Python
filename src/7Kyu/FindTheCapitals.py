def capitals(word):
    indices = []

    for i in range(len(word)):
        letra = word[i]

        if letra.isupper():
            indices.append(i)

    return indices