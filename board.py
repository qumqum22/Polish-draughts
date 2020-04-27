from const import *
from punktacja import biale
from punktacja import czarne

def wyswietl():
    ''' Funkcja wyswietla aktualny stan gry '''
    for i in range(SIZE):
        print(i, "\t", plansza[i])

    print("\n\t   a    b    c    d    e    f    g    h    i    j \n")

def ukladPoczatkowy():
    ''' Funkcja inicjalizuje plansze pionkami '''
    for row in range(0, LINES_OF_PAWNS, 1):
        if row % 2:
            for column in range(0, SIZE, 2):
                plansza[row][column] = BLACK_PAWN
        else:
            for column in range(1, SIZE, 2):
                plansza[row][column] = BLACK_PAWN

    for row in range(SIZE - LINES_OF_PAWNS, SIZE, 1):
        if row % 2:
            for column in range(0, SIZE, 2):
                plansza[row][column] = WHITE_PAWN
        else:
            for column in range(1, SIZE, 2):
                plansza[row][column] = WHITE_PAWN
    plansza[1][0] = WHITE_PAWN
    plansza[0][1] = EMPTY_FIELD



def wyniesienie(x, y, gracz):
    global biale
    global czarne
    if gracz == 1:
        if x == 0 and plansza[0][y] == WHITE_PAWN:
            plansza[0][y] = WHITE_QUINN
            #biale += 90
            return True
    else:
        if x == 9 and plansza[9][y] == BLACK_PAWN:
            plansza[9][y] = BLACK_QUINN
            #czarne += 90
            return True
    return False

     #Pionek, który dojdzie do ostatniego rzędu planszy, staje się damką,
    #przy czym jeśli znajdzie się tam w wyniku bicia i będzie mógł wykonać
    #kolejne bicie (do tyłu), to będzie musiał je wykonać i
    # nie staje się wtedy damką (pozostaje pionkiem).

# Stworzyc liste przechowywujaca wszystkie pionki gracza
# Umozliwi sprawdzenie czy ma dostepne bicia