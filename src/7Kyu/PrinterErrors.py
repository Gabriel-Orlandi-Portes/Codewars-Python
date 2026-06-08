def printer_error(s):
    erros = 0

    for letra in s:
        if letra > 'm':
            erros += 1

    return f'{erros}/{len(s)}'