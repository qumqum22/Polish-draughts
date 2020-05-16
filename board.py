from const import *
from punktacja import *

biale_piony = []
biale_damki = []

czarne_piony = []
czarne_damki = []


def wyswietl():
    ''' Funkcja wyswietla aktualny stan gry '''
    for i in range(SIZE):
        print(i, "\t", plansza[i])
        print('-------------------------------------------------------')

    print("\n\t   a    b    c    d    e    f    g    h    i    j \n")

def ukladCzyszczenie():
    for row in range(0, SIZE, 1):
        for column in range(0, SIZE, 1):
            plansza[row][column] = EMPTY_FIELD

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

def czytajFigury():
    global biale_piony
    global biale_damki

    global czarne_piony
    global czarne_damki

    biale_piony.clear()
    biale_damki.clear()

    czarne_piony.clear()
    czarne_damki.clear()
    for row in range(SIZE):
        for column in range(SIZE):
            if plansza[row][column] == WHITE_PAWN:
                biale_piony.append((row, column))
            elif plansza[row][column] == WHITE_QUENN:
                biale_damki.append((row, column))
            elif plansza[row][column] == BLACK_PAWN:
                czarne_piony.append((row, column))
            elif plansza[row][column] == BLACK_QUENN:
                czarne_damki.append((row, column))

def wyniesienie(x, y, gracz):
    global biale
    global czarne
    if gracz == 1:
        if x == 0 and plansza[0][y] == WHITE_PAWN:
            plansza[0][y] = WHITE_QUENN
            punktujBiale(90)
            return True
    else:
        if x == 9 and plansza[9][y] == BLACK_PAWN:
            plansza[9][y] = BLACK_QUENN
            punktujCzarne(90)
            return True
    return False

     #Pionek, który dojdzie do ostatniego rzędu planszy, staje się damką,
    #przy czym jeśli znajdzie się tam w wyniku bicia i będzie mógł wykonać
    #kolejne bicie (do tyłu), to będzie musiał je wykonać i
    # nie staje się wtedy damką (pozostaje pionkiem).
