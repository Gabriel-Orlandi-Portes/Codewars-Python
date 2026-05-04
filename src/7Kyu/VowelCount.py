def get_count(sentence):
    count = 0
    
    for vogal in sentence:
        if vogal in 'aeiou':
            count += 1
    return count
