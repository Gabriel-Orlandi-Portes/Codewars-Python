def points(games):
    pontos = 0
    for i in games:
        if i[0] > i[2]:
            pontos += 3
        elif i[0] == i[2]:
            pontos += 1
        else:
            pontos += 0
    return pontos
            
