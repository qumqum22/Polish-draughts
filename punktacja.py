""" Module with players points logic. """
import const as c



def punktuj():
    """ Initializing the board with points. """
    srodek_l = c.SIZE/2-2
    srodek_p = c.SIZE/2+1
    for x_coord in range(c.SIZE):
        for y_coord in range(c.SIZE):
            #PUNKTOWANIE ZA OKRAG
            if x_coord in (0, c.SIZE - 1) or y_coord in (0, c.SIZE - 1):
                c.punktacja[x_coord][y_coord] += 6
            elif (srodek_l <= x_coord <= srodek_p) and (srodek_l <= y_coord <= srodek_p):
                c.punktacja[x_coord][y_coord] += 2
            else:
                c.punktacja[x_coord][y_coord] += 4
            #PUNKTOWANIE ZA LINIE
            if x_coord < c.SIZE/5:
                c.punktacja[x_coord][y_coord] += 5
            elif x_coord < 2*c.SIZE/5:
                c.punktacja[x_coord][y_coord] += 4
            elif x_coord < 3*c.SIZE/5:
                c.punktacja[x_coord][y_coord] += 3
            elif x_coord < 4*c.SIZE/5:
                c.punktacja[x_coord][y_coord] += 2
            else:
                c.punktacja[x_coord][y_coord] += 1

punktuj()

def wyswietl_punktacje():
    """ Showing x_coord board of points. """
    for i in range(c.SIZE):
        print(i, "\t", c.punktacja[i])
    print()

def punkty_planszy(x_coord, y_coord, gracz, gracz_k):
    """ Returns points of position for player."""
    wynik = c.punktacja[gracz*x_coord+gracz_k][y_coord]    # dla bialego [x][y], # czarny [-x-1][y]
    return wynik

def punkty_start():
    """     Funkcja inicjalizuje punkty poczatkowe graczy   """
    c.biale = 0
    c.czarne = 0
    for i in range(c.SIZE):
        for j in range(c.SIZE):
            if c.plansza[i][j] == c.WHITE_PAWN:
                c.biale += c.POINTS_PAWN
                c.biale += punkty_planszy(i, j, 1, 0)
            elif c.plansza[i][j] == c.WHITE_QUENN:
                c.biale += c.POINTS_QUENN
                c.biale += punkty_planszy(i, j, 1, 0)
            elif c.plansza[i][j] == c.BLACK_PAWN:
                c.czarne += c.POINTS_PAWN
                c.czarne += punkty_planszy(i, j, -1, -1)
            elif c.plansza[i][j] == c.BLACK_QUENN:
                c.czarne += c.POINTS_QUENN
                c.czarne += punkty_planszy(i, j, -1, -1)
    print(f'Punkty bialego: {c.biale}')
    print(f'Punkty czarnego: {c.czarne}')


def punkty_update(row_start, column_start, row_end, column_end, gracz, gracz_k):
    """ Funkcja uaktualnia sume punktow gracza co ruch"""

    nowa_pozycja = punkty_planszy(row_end, column_end, gracz, gracz_k)
    stara_pozycja = punkty_planszy(row_start, column_start, gracz, gracz_k)
    if gracz == 1:
        c.biale += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{c.biale}')
        print(f'Wynik czarnego:{c.czarne}')
    else:
        c.czarne += nowa_pozycja - stara_pozycja
        print(f'Wynik bialego:{c.biale}')
        print(f'Wynik czarnego:{c.czarne}')
