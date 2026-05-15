def validate_pin(pin):
    if len(pin) ==  4 or len(pin) == 6:
        for i in pin:
            if i < '0' or i > '9':
                return False
                break
            else:
                pass
        return True
    else:
        return False
