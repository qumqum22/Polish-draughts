""" Functions which are operating on game board."""
import const as c

def wyswietl():
    """ Funkcja wyswietla aktualny stan gry. """
    for i in range(c.SIZE):
        print(i, "\t", c.plansza[i])
        print('-------------------------------------------------------')

    print("\n\t   a    b    c    d    e    f    g    h    i    j \n")

def uklad_czyszczenie():
    """ Czyszczenie planszy z figur. """
    for row in range(0, c.SIZE, 1):
        for column in range(0, c.SIZE, 1):
            c.plansza[row][column] = c.EMPTY_FIELD

def uklad_poczatkowy():
    """ Funkcja inicjalizuje plansze pionkami """

    for row in range(0, c.LINES_OF_PAWNS, 1):
        if row % 2:
            for column in range(0, c.SIZE, 2):
                c.plansza[row][column] = c.BLACK_PAWN
        else:
            for column in range(1, c.SIZE, 2):
                c.plansza[row][column] = c.BLACK_PAWN

    for row in range(c.SIZE - c.LINES_OF_PAWNS, c.SIZE, 1):
        if row % 2:
            for column in range(0, c.SIZE, 2):
                c.plansza[row][column] = c.WHITE_PAWN
        else:
            for column in range(1, c.SIZE, 2):
                c.plansza[row][column] = c.WHITE_PAWN

def czytaj_figury():
    """ Tworzenie listy pionkow graczy. """
    c.biale_piony.clear()
    c.biale_damki.clear()

    c.czarne_piony.clear()
    c.czarne_damki.clear()
    for row in range(c.SIZE):
        for column in range(c.SIZE):
            if c.plansza[row][column] == c.WHITE_PAWN:
                c.biale_piony.append((row, column))
            elif c.plansza[row][column] == c.WHITE_QUENN:
                c.biale_damki.append((row, column))
            elif c.plansza[row][column] == c.BLACK_PAWN:
                c.czarne_piony.append((row, column))
            elif c.plansza[row][column] == c.BLACK_QUENN:
                c.czarne_damki.append((row, column))

def wyniesienie(x_coord, y_coord, gracz):
    """ Zamiana piona na damke, gdy dojdzie do konca planszy. """
    if gracz == 1:
        if x_coord == 0 and c.plansza[0][y_coord] == c.WHITE_PAWN:
            c.plansza[0][y_coord] = c.WHITE_QUENN
            c.biale += c.POINTS_QUENN - c.POINTS_PAWN
            return True
    else:
        if x_coord == 9 and c.plansza[9][y_coord] == c.BLACK_PAWN:
            c.plansza[9][y_coord] = c.BLACK_QUENN
            c.czarne += c.POINTS_QUENN - c.POINTS_PAWN
            return True
    return False

def test_1():
    """ Test wielokrotnego bicia. """
    c.plansza[6][3] = c.BLACK_PAWN
    c.plansza[5][4] = c.WHITE_PAWN
    c.plansza[5][6] = c.WHITE_PAWN
    c.plansza[7][4] = c.WHITE_PAWN
    c.plansza[7][6] = c.WHITE_PAWN

    c.plansza[5][2] = c.WHITE_PAWN
    c.plansza[2][1] = c.BLACK_PAWN
    c.plansza[2][3] = c.BLACK_PAWN
    c.plansza[4][3] = c.BLACK_PAWN
    c.plansza[4][1] = c.BLACK_PAWN

def test_2():
    """ Test wyniesienia. """
    c.plansza[1][2] = c.WHITE_PAWN
    c.plansza[8][7] = c.BLACK_PAWN

def test_3():
    """ Test wygranej bialych. """
    c.plansza[5][6] = c.BLACK_QUENN
    c.plansza[6][5] = c.WHITE_PAWN
