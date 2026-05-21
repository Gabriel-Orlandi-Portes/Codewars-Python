def solution(s):
    resultado = []

    for i in range(0, len(s), 2):
        par = s[i:i+2]

        if len(par) == 1:
            par += "_"

        resultado.append(par)

    return resultado
