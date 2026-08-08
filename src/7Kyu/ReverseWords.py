def reverse_words(text):
    palavras = text.split(" ")
    
    for i in range(len(palavras)):
        palavras[i] = palavras[i][::-1]
    
    return " ".join(palavras)