""" Functions which are operating on game board."""
import const as c
import gra as g
def wyswietl():
    """ Funkcja wyswietla aktualny stan gry. """
    for i in range(c.SIZE):
        print(i, "\t", g.plansza[i])
        print('-------------------------------------------------------')

    print("\n\t   a    b    c    d    e    f    g    h    i    j \n")

def uklad_czyszczenie():
    """ Czyszczenie planszy z figur. """
    for row in range(0, c.SIZE, 1):
        for column in range(0, c.SIZE, 1):
            g.plansza[row][column] = c.EMPTY_FIELD

def uklad_poczatkowy():
    """ Funkcja inicjalizuje plansze pionkami """

    for row in range(0, c.LINES_OF_PAWNS, 1):
        if row % 2:
            for column in range(0, c.SIZE, 2):
                g.plansza[row][column] = c.BLACK_PAWN
        else:
            for column in range(1, c.SIZE, 2):
                g.plansza[row][column] = c.BLACK_PAWN

    for row in range(c.SIZE - c.LINES_OF_PAWNS, c.SIZE, 1):
        if row % 2:
            for column in range(0, c.SIZE, 2):
                g.plansza[row][column] = c.WHITE_PAWN
        else:
            for column in range(1, c.SIZE, 2):
                g.plansza[row][column] = c.WHITE_PAWN

def czytaj_figury():
    """ Tworzenie listy pionkow graczy. """
    g.biale_piony.clear()
    g.biale_damki.clear()

    g.czarne_piony.clear()
    g.czarne_damki.clear()
    for row in range(c.SIZE):
        for column in range(c.SIZE):
            if g.plansza[row][column] == c.WHITE_PAWN:
                g.biale_piony.append((row, column))
            elif g.plansza[row][column] == c.WHITE_QUENN:
                g.biale_damki.append((row, column))
            elif g.plansza[row][column] == c.BLACK_PAWN:
                g.czarne_piony.append((row, column))
            elif g.plansza[row][column] == c.BLACK_QUENN:
                g.czarne_damki.append((row, column))

def wyniesienie(x_coord, y_coord, gracz):
    """ Zamiana piona na damke, gdy dojdzie do konca planszy. """
    if gracz == 1:
        if x_coord == 0 and g.plansza[0][y_coord] == c.WHITE_PAWN:
            g.plansza[0][y_coord] = c.WHITE_QUENN
            g.biale += c.POINTS_QUENN - c.POINTS_PAWN
            return True
    else:
        if x_coord == 9 and g.plansza[9][y_coord] == c.BLACK_PAWN:
            g.plansza[9][y_coord] = c.BLACK_QUENN
            g.czarne += c.POINTS_QUENN - c.POINTS_PAWN
            return True
    return False

def test_1():
    """ Test wielokrotnego bicia. """
    g.plansza[6][3] = c.BLACK_PAWN
    g.plansza[5][4] = c.WHITE_PAWN
    g.plansza[5][6] = c.WHITE_PAWN
    g.plansza[7][4] = c.WHITE_PAWN
    g.plansza[7][6] = c.WHITE_PAWN

    g.plansza[5][2] = c.WHITE_PAWN
    g.plansza[2][1] = c.BLACK_PAWN
    g.plansza[2][3] = c.BLACK_PAWN
    g.plansza[4][3] = c.BLACK_PAWN
    g.plansza[4][1] = c.BLACK_PAWN

def test_2():
    """ Test wyniesienia. """
    g.plansza[1][2] = c.WHITE_PAWN
    g.plansza[8][7] = c.BLACK_PAWN

def test_3():
    """ Test wygranej bialych. """
    g.plansza[5][6] = c.BLACK_QUENN
    g.plansza[6][5] = c.WHITE_PAWN
