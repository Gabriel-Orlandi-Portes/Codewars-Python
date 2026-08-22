def capitalize(s):
    par = ""
    impar = ""
    
    for i in range (len(s)):
        if i % 2 == 0:
            par += s[i].upper()
            impar += s[i]
        else:
            par += s[i]
            impar += s[i].upper()
    
    return [par, impar]