""" Functions which are operating on game board."""
import const as con
import gra
def wyswietl():
    """ Funkcja wyswietla aktualny stan gry. """
    for i in range(con.SIZE):
        print(i, "\t", gra.Gra.plansza[i])
        print('-------------------------------------------------------')

    print("\n\t   a    b    c    d    e    f    g    h    i    j \n")

def uklad_czyszczenie():
    """ Czyszczenie planszy z figur. """
    for row in range(0, con.SIZE, 1):
        for column in range(0, con.SIZE, 1):
            gra.Gra.plansza[row][column] = con.EMPTY_FIELD

def uklad_poczatkowy():
    """ Funkcja inicjalizuje plansze pionkami """

    for row in range(0, con.LINES_OF_PAWNS, 1):
        if row % 2:
            for column in range(0, con.SIZE, 2):
                gra.Gra.plansza[row][column] = con.BLACK_PAWN
        else:
            for column in range(1, con.SIZE, 2):
                gra.Gra.plansza[row][column] = con.BLACK_PAWN

    for row in range(con.SIZE - con.LINES_OF_PAWNS, con.SIZE, 1):
        if row % 2:
            for column in range(0, con.SIZE, 2):
                gra.Gra.plansza[row][column] = con.WHITE_PAWN
        else:
            for column in range(1, con.SIZE, 2):
                gra.Gra.plansza[row][column] = con.WHITE_PAWN
    gra.Gra.plansza[6][1] = con.WHITE_QUENN

def czytaj_figury():
    """ Tworzenie listy pionkow graczy. """
    gra.Gra.biale_piony.clear()
    gra.Gra.biale_damki.clear()

    gra.Gra.czarne_piony.clear()
    gra.Gra.czarne_damki.clear()
    for row in range(con.SIZE):
        for column in range(con.SIZE):
            if gra.Gra.plansza[row][column] == con.WHITE_PAWN:
                gra.Gra.biale_piony.append((row, column))
            elif gra.Gra.plansza[row][column] == con.WHITE_QUENN:
                gra.Gra.biale_damki.append((row, column))
            elif gra.Gra.plansza[row][column] == con.BLACK_PAWN:
                gra.Gra.czarne_piony.append((row, column))
            elif gra.Gra.plansza[row][column] == con.BLACK_QUENN:
                gra.Gra.czarne_damki.append((row, column))

def wyniesienie(x_coord, y_coord, gracz):
    """ Zamiana piona na damke, gdy dojdzie do konca planszy. """
    if gracz == 1:
        if x_coord == 0 and gra.Gra.plansza[0][y_coord] == con.WHITE_PAWN:
            gra.Gra.plansza[0][y_coord] = con.WHITE_QUENN
            gra.Gra.biale += con.POINTS_QUENN - con.POINTS_PAWN
            return True
    else:
        if x_coord == 9 and gra.Gra.plansza[9][y_coord] == con.BLACK_PAWN:
            gra.Gra.plansza[9][y_coord] = con.BLACK_QUENN
            gra.Gra.czarne += con.POINTS_QUENN - con.POINTS_PAWN
            return True
    return False

def test_1():
    """ Test wielokrotnego bicia. """
    gra.Gra.attack_from.clear()
    gra.Gra.plansza[6][3] = con.BLACK_PAWN
    gra.Gra.plansza[5][4] = con.WHITE_PAWN
    gra.Gra.plansza[5][6] = con.WHITE_PAWN
    gra.Gra.plansza[7][4] = con.WHITE_PAWN
    gra.Gra.plansza[7][6] = con.WHITE_PAWN

    gra.Gra.plansza[5][2] = con.WHITE_PAWN
    gra.Gra.plansza[2][1] = con.BLACK_PAWN
    gra.Gra.plansza[2][3] = con.BLACK_PAWN
    gra.Gra.plansza[4][3] = con.BLACK_PAWN
    gra.Gra.plansza[4][1] = con.BLACK_PAWN

def test_2():
    """ Test wyniesienia. """
    gra.Gra.attack_from.clear()
    gra.Gra.plansza[1][2] = con.WHITE_PAWN
    gra.Gra.plansza[8][7] = con.BLACK_PAWN

def test_3():
    """ Test wygranej bialych. """
    gra.Gra.attack_from.clear()
    gra.Gra.plansza[5][6] = con.BLACK_QUENN
    gra.Gra.plansza[6][5] = con.WHITE_PAWN
