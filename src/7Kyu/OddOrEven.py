def odd_or_even(arr):
    soma = sum(arr)
    
    if soma % 2 == 0:
        return 'even'
    else:
        return 'odd'
