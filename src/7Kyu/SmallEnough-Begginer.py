def small_enough(array, limit):
    maior = 0
    for i in array:
        if i > limit:
            maior += 1
            
    
    if maior > 0:
        return False
    else:
        return True