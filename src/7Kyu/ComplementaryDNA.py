def DNA_strand(dna):
    result = ''
    for i in dna:
        if i == 'A':
            result += 'T'
        elif i == 'T':
            result += 'A'
        elif i == 'G':
            result += 'C'
        elif i == 'C':
            result += 'G'
        
    return result