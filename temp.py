def switch(argument):
    switcher = {
        "a": 0,     "b": 1,     "c": 2,
        "d": 3,     "e": 4,     "f": 5,
        "g": 6,     "h": 7,     "i": 8,
        "j": 9
    }
    return switcher.get(argument, "Invalid place")


def translate(pozycja):
    ''' Przekszałca pozycję z "a7" na " 0 , 7 " '''
    if len(pozycja) != 2:
        print("Podana niepoprawna pozycja")
        return 'abc', 'cbc'
    else:
        row = int(pozycja[1])
        column = int(switch(pozycja[0]))
        return row, column

def sprawdzPozycje(x, y):
    if x > -1 and x < 10:
        if y > -1 and y < 10:
            return True
    return False
