def count_positives_sum_negatives(arr):
    neg = 0
    pos = 0
    
    if not arr:
            return []
      
    for i in arr:      
        if i > 0:
            pos += 1
        elif i < 0:
            neg += i
        else:
            pass
        
    
    return [pos, neg]
        
