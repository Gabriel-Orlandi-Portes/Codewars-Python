def number(lines):
    contador = 0
    lines_1 = []
    for i in range (len(lines)):
        lines_1.append(f'{i+1}: {lines[i]}')
    
    return(lines_1)