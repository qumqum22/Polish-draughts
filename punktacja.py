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


def punkty_planszy(x_coord, y_coord, gracz, gracz_k):
    """ Returns points of position for player."""
    wynik = gra.Gra.punktacja[gracz*x_coord+gracz_k][y_coord]    # dla bialego [x][y], # czarny [-x-1][y]
    return wynik


def punkty_start():
    """     Funkcja inicjalizuje punkty poczatkowe graczy   """
    gra.Gra.biale = 0
    gra.Gra.czarne = 0
    for i in range(con.SIZE):
        for j in range(con.SIZE):
            if gra.Gra.plansza[i][j] == con.WHITE_PAWN:
                gra.Gra.biale += con.POINTS_PAWN
                gra.Gra.biale += punkty_planszy(i, j, 1, 0)
            elif gra.Gra.plansza[i][j] == con.WHITE_QUENN:
                gra.Gra.biale += con.POINTS_QUENN
                gra.Gra.biale += punkty_planszy(i, j, 1, 0)
            elif gra.Gra.plansza[i][j] == con.BLACK_PAWN:
                gra.Gra.czarne += con.POINTS_PAWN
                gra.Gra.czarne += punkty_planszy(i, j, -1, -1)
            elif gra.Gra.plansza[i][j] == con.BLACK_QUENN:
                gra.Gra.czarne += con.POINTS_QUENN
                gra.Gra.czarne += punkty_planszy(i, j, -1, -1)
    print(f'Punkty bialego: {gra.Gra.biale}')
    print(f'Punkty czarnego: {gra.Gra.czarne}')


def punkty_update(row_start, column_start, row_end, column_end, gracz, gracz_k):
    """ Funkcja uaktualnia sume punktow gracza co ruch"""

    nowa_pozycja = punkty_planszy(row_end, column_end, gracz, gracz_k)
    stara_pozycja = punkty_planszy(row_start, column_start, gracz, gracz_k)
    if gracz == 1:
        gra.Gra.biale += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{gra.Gra.biale}')
        print(f'Wynik czarnego:{gra.Gra.czarne}')
    else:
        gra.Gra.czarne += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{gra.Gra.biale}')
        print(f'Wynik czarnego:{gra.Gra.czarne}')


def punkty_bicie_pionem(ruch, gracz, gracz_k):
    """ Function substracts points for deleting figure. """
    between_row_points = int((ruch[0] + ruch[2]) / 2)   # Working for pawn only
    between_column_points = int((ruch[1] + ruch[3]) / 2)    # Working for pawn only

    if gracz == 1:
        if gra.Gra.plansza[between_row_points][between_column_points] == con.BLACK_PAWN:
            gra.Gra.czarne += -con.POINTS_PAWN
            gra.Gra.czarne += -punkty_planszy(between_row_points, between_column_points,
                                            -gracz, gracz * gracz_k - 1)
        elif gra.Gra.plansza[between_row_points][between_column_points] == con.BLACK_QUENN:
            gra.Gra.czarne += -con.POINTS_QUENN
            gra.Gra.czarne += -punkty_planszy(between_row_points, between_column_points,
                                            -gracz, gracz * gracz_k - 1)
    else:
        if gra.Gra.plansza[between_row_points][between_column_points] == con.WHITE_PAWN:
            gra.Gra.biale += -con.POINTS_PAWN
            gra.Gra.biale += -punkty_planszy(between_row_points, between_column_points,
                                           -gracz, gracz * gracz_k - 1)
        elif gra.Gra.plansza[between_row_points][between_column_points] == con.WHITE_QUENN:
            gra.Gra.biale += -con.POINTS_QUENN
            gra.Gra.biale += -punkty_planszy(between_row_points, between_column_points,
                                           -gracz, gracz * gracz_k - 1)

def punkty_bicie_damka(krotka, gracz, gracz_k):
    """ Function substracts points for deleting figure. """
    if gracz == 1:
        if gra.Gra.plansza[krotka[1]][krotka[2]] == con.BLACK_PAWN:
            gra.Gra.czarne += -con.POINTS_PAWN
            gra.Gra.czarne += -punkty_planszy(krotka[1], krotka[2],
                                        -gracz, gracz * gracz_k - 1)
        elif gra.Gra.plansza[krotka[1]][krotka[2]] == con.BLACK_QUENN:
            gra.Gra.czarne += -con.POINTS_QUENN
            gra.Gra.czarne += -punkty_planszy(krotka[1], krotka[2],
                                        -gracz, gracz * gracz_k - 1)
    else:
        if gra.Gra.plansza[krotka[1]][krotka[2]] == con.WHITE_PAWN:
            gra.Gra.biale += -con.POINTS_PAWN
            gra.Gra.biale += -punkty_planszy(krotka[1], krotka[2],
                                       -gracz, gracz * gracz_k - 1)
        elif gra.Gra.plansza[krotka[1]][krotka[2]] == con.WHITE_QUENN:
            gra.Gra.biale += -con.POINTS_QUENN
            gra.Gra.biale += -punkty_planszy(krotka[1], krotka[2],
                                       -gracz, gracz * gracz_k - 1)