""" Module with players points logicon. """
import const as con
import gra


def punktuj():
    """ Initializing the board with points. """
    srodek_l = con.SIZE/2-2
    srodek_p = con.SIZE/2+1
    for x_coord in range(con.SIZE):
        for y_coord in range(con.SIZE):
            #PUNKTOWANIE ZA OKRAG
            if x_coord in (0, con.SIZE - 1) or y_coord in (0, con.SIZE - 1):
                gra.Gra.punktacja[x_coord][y_coord] += 6
            elif (srodek_l <= x_coord <= srodek_p) and (srodek_l <= y_coord <= srodek_p):
                gra.Gra.punktacja[x_coord][y_coord] += 2
            else:
                gra.Gra.punktacja[x_coord][y_coord] += 4
            #PUNKTOWANIE ZA LINIE
            if x_coord < con.SIZE/5:
                gra.Gra.punktacja[x_coord][y_coord] += 5
            elif x_coord < 2*con.SIZE/5:
                gra.Gra.punktacja[x_coord][y_coord] += 4
            elif x_coord < 3*con.SIZE/5:
                gra.Gra.punktacja[x_coord][y_coord] += 3
            elif x_coord < 4*con.SIZE/5:
                gra.Gra.punktacja[x_coord][y_coord] += 2
            else:
                gra.Gra.punktacja[x_coord][y_coord] += 1


punktuj()


def wyswietl_punktacje():
    """ Showing x_coord board of points. """
    for i in range(con.SIZE):
        print(i, "\t", gra.Gra.punktacja[i])
    print()


def punkty_planszy(x_coord, y_coord):
    """ Returns points of position for player."""

    if gra.Gra.player == con.PLAYER_ONE:
        wynik = gra.Gra.punktacja[x_coord][y_coord]
    else:
        wynik = gra.Gra.punktacja[-x_coord-1][-y_coord]
    return wynik

def punkty_planszy_czarne(x_coord, y_coord):
    """ Returns points of position for player."""

    wynik = gra.Gra.punktacja[-x_coord-1][-y_coord]
    return wynik

def punkty_planszy_biale(x_coord, y_coord):
    """ Returns points of position for player."""

    wynik = gra.Gra.punktacja[x_coord][y_coord]
    return wynik

def punkty_start():
    """     Funkcja inicjalizuje punkty poczatkowe graczy   """
    gra.Gra.biale = 0
    gra.Gra.czarne = 0
    for i in range(con.SIZE):
        for j in range(con.SIZE):
            if gra.Gra.plansza[i][j] == con.WHITE_PAWN:
                gra.Gra.biale += con.POINTS_PAWN
                gra.Gra.biale += punkty_planszy_biale(i, j)
            elif gra.Gra.plansza[i][j] == con.WHITE_QUEEN:
                gra.Gra.biale += con.POINTS_QUEEN
                gra.Gra.biale += punkty_planszy_biale(i, j)
            elif gra.Gra.plansza[i][j] == con.BLACK_PAWN:
                gra.Gra.czarne += con.POINTS_PAWN
                gra.Gra.czarne += punkty_planszy_czarne(i, j)
            elif gra.Gra.plansza[i][j] == con.BLACK_QUEEN:
                gra.Gra.czarne += con.POINTS_QUEEN
                gra.Gra.czarne += punkty_planszy_czarne(i, j)
    print(f'Punkty bialego: {gra.Gra.biale}')
    print(f'Punkty czarnego: {gra.Gra.czarne}')


def punkty_update(row_start, column_start, row_end, column_end):
    """ Funkcja uaktualnia sume punktow gracza co ruch"""


    if gra.Gra.player == con.PLAYER_ONE:
        nowa_pozycja = punkty_planszy_biale(row_end, column_end)
        stara_pozycja = punkty_planszy_biale(row_start, column_start)
        gra.Gra.biale += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{gra.Gra.biale}')
        print(f'Wynik czarnego:{gra.Gra.czarne}')
    else:
        nowa_pozycja = punkty_planszy_czarne(row_end, column_end)
        stara_pozycja = punkty_planszy_czarne(row_start, column_start)
        gra.Gra.czarne += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{gra.Gra.biale}')
        print(f'Wynik czarnego:{gra.Gra.czarne}')


def punkty_bicie_pionem(ruch):
    """ Function substracts points for deleting figure. """
    between_row = (ruch[0] + ruch[2]) // 2
    between_column = (ruch[1] + ruch[3]) // 2

    if gra.Gra.player == con.PLAYER_ONE:
        if gra.Gra.plansza[between_row][between_column] == con.BLACK_PAWN:
            gra.Gra.czarne += -con.POINTS_PAWN
            gra.Gra.czarne += -punkty_planszy_czarne(between_row, between_column)

        elif gra.Gra.plansza[between_row][between_column] == con.BLACK_QUEEN:
            gra.Gra.czarne += -con.POINTS_QUEEN
            gra.Gra.czarne += -punkty_planszy_czarne(between_row, between_column)
    else:
        if gra.Gra.plansza[between_row][between_column] == con.WHITE_PAWN:
            gra.Gra.biale += -con.POINTS_PAWN
            gra.Gra.biale += -punkty_planszy_biale(between_row, between_column)

        elif gra.Gra.plansza[between_row][between_column] == con.WHITE_QUEEN:
            gra.Gra.biale += -con.POINTS_QUEEN
            gra.Gra.biale += -punkty_planszy_biale(between_row, between_column)

def punkty_bicie_damka(krotka):
    """ Function substracts points for deleting figure. """
    if gra.Gra.player == con.PLAYER_ONE:
        if gra.Gra.plansza[krotka[1]][krotka[2]] == con.BLACK_PAWN:
            gra.Gra.czarne += -con.POINTS_PAWN
            gra.Gra.czarne += -punkty_planszy_czarne(krotka[1], krotka[2])
        elif gra.Gra.plansza[krotka[1]][krotka[2]] == con.BLACK_QUEEN:
            gra.Gra.czarne += -con.POINTS_QUEEN
            gra.Gra.czarne += -punkty_planszy_czarne(krotka[1], krotka[2])
    else:
        if gra.Gra.plansza[krotka[1]][krotka[2]] == con.WHITE_PAWN:
            gra.Gra.biale += -con.POINTS_PAWN
            gra.Gra.biale += -punkty_planszy_biale(krotka[1], krotka[2])
        elif gra.Gra.plansza[krotka[1]][krotka[2]] == con.WHITE_QUEEN:
            gra.Gra.biale += -con.POINTS_QUEEN
            gra.Gra.biale += -punkty_planszy_biale(krotka[1], krotka[2])
