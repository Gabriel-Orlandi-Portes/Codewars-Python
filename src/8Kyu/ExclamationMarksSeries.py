def replace_exclamation(st):
    vogal = 'aeiou'
    novo = ''
    for i in st:
        if i.lower() in vogal:
            novo += '!'
        else:
            novo += i
    return novo
        