def xo(s):
    x = 0
    o = 0
    s = s.lower()
    for i in s:
        if i == 'x':
            x +=1
        elif i == 'o':
            o +=1
    
    if x == o:
        return True
    else:
        return False
        
