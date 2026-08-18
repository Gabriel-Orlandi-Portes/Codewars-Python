def get_middle(string):
    meio = len(string) // 2

    if len(string) % 2 != 0:
        return string[meio]
    else:
        return string[meio - 1:meio + 1]