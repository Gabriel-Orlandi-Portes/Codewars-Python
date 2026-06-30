geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    resultado = []

    for bird in birds:
        if bird not in geese:
            resultado.append(bird)

    return resultado
