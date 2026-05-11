def open_or_senior(data):
    resul = []
    for pessoa in data:
        if pessoa[0] >= 55 and pessoa[1] > 7:
            resul.append('Senior')
        else:
            resul.append('Open')
    return resul
            
