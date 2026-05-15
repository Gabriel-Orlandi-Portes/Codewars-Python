def is_isogram(string):
    string.lower()
    isogama = []
    for i in string.lower():
        if i not in isogama:
            isogama.append(i)
        else:
            return False
    return True
