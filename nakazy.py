""" Functions important for rules file. """
import board
import rules
import const as c


quenn_mozliwe_ruchy_biale = []
quenn_mozliwe_ruchy_czarne = []

quenn_mozliwe_bicia_biale = []
quenn_mozliwe_bicia_czarne = []

def pawn_move(gracz):
    """ Funkcja zwraca liste wszystkich mozliwych ruchow gracza. """
    board.czytaj_figury()
    # zapamietac stan gry trzeba
    # rekurencyjnie robic
    pion_mozliwe_ruchy_biale = []
    pion_mozliwe_ruchy_czarne = []

    pion_mozliwe_ruchy_biale.clear()
    pion_mozliwe_ruchy_czarne.clear()

    if gracz == 1:
        for row_start, column_start in c.biale_piony:
            if rules.sprawdz_pozycje(row_start-1, column_start+1):
                if c.plansza[row_start-1][column_start+1] == c.EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start,
                                                     row_start - 1, column_start + 1))
            if rules.sprawdz_pozycje(row_start - 1, column_start - 1):
                if c.plansza[row_start-1][column_start-1] == c.EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start,
                                                     row_start - 1, column_start - 1))
        return pion_mozliwe_ruchy_biale
    for row_start, column_start in c.czarne_piony:
        if rules.sprawdz_pozycje(row_start + 1, column_start + 1):
            if c.plansza[row_start+1][column_start+1] == c.EMPTY_FIELD:
                pion_mozliwe_ruchy_czarne.append((row_start, column_start,
                                                  row_start + 1, column_start + 1))
        if rules.sprawdz_pozycje(row_start + 1, column_start - 1):
            if c.plansza[row_start+1][column_start-1] == c.EMPTY_FIELD:
                pion_mozliwe_ruchy_czarne.append((row_start, column_start,
                                                  row_start + 1, column_start - 1))
    return pion_mozliwe_ruchy_czarne


def pawn_hit(gracz):
    """ Funkcja wykrywa mozliwe bicia"""
    board.czytaj_figury()

    pion_mozliwe_bicia = []
    pion_mozliwe_bicia.clear()

    if gracz == 1:
        for pionek in c.biale_piony:
            if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                          pionek[0]+2, pionek[1]+2, gracz):
                pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                           pionek[0] + 2, pionek[1] + 2))

            if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                          pionek[0] + 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                           pionek[0] + 2, pionek[1] - 2))

            if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                          pionek[0] - 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                           pionek[0] - 2, pionek[1] - 2))

            if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                          pionek[0] - 2, pionek[1] + 2, gracz):
                pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                           pionek[0] - 2, pionek[1] + 2))

        return pion_mozliwe_bicia

    for pionek in c.czarne_piony:
        if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                      pionek[0] + 2, pionek[1] + 2, gracz):
            pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                       pionek[0] + 2, pionek[1] + 2))

        if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                      pionek[0] + 2, pionek[1] - 2, gracz):
            pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                       pionek[0] + 2, pionek[1] - 2))

        if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                      pionek[0] - 2, pionek[1] - 2, gracz):
            pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                       pionek[0] - 2, pionek[1] - 2))

        if rules.sprawdz_bicie_pionka(pionek[0], pionek[1],
                                      pionek[0] - 2, pionek[1] + 2, gracz):
            pion_mozliwe_bicia.append((pionek[0], pionek[1],
                                       pionek[0] - 2, pionek[1] + 2))

    return pion_mozliwe_bicia


def next_pawn_hit(row_start, column_start, gracz):
    """ Funkcja wykrywa kolejne mozliwe bicia juz posunietego piona """
    board.czytaj_figury()

    pion_mozliwe_bicia = []
    pion_mozliwe_bicia.clear()

    if rules.sprawdz_bicie_pionka(row_start, column_start,
                                  row_start + 2, column_start + 2, gracz):
        pion_mozliwe_bicia.append((row_start, column_start,
                                   row_start + 2, column_start + 2))

    if rules.sprawdz_bicie_pionka(row_start, column_start,
                                  row_start + 2, column_start - 2, gracz):
        pion_mozliwe_bicia.append((row_start, column_start,
                                   row_start + 2, column_start - 2))

    if rules.sprawdz_bicie_pionka(row_start, column_start,
                                  row_start - 2, column_start - 2, gracz):
        pion_mozliwe_bicia.append((row_start, column_start,
                                   row_start - 2, column_start - 2))

    if rules.sprawdz_bicie_pionka(row_start, column_start,
                                  row_start - 2, column_start + 2, gracz):
        pion_mozliwe_bicia.append((row_start, column_start,
                                   row_start - 2, column_start + 2))

    if pion_mozliwe_bicia:
        return pion_mozliwe_bicia, True
    return [], False


def quenn_move(row_start, column_start, gracz):
    """ Funkcja nie dokonczona, sprawdza mozliwe ruchy i bicia krolowa. """
    for i in range(-9, 10, 1):
        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start+i, column_start+i, gracz)
        if move_tuple[3]:
            if move_tuple[0]:
                quenn_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start+i, column_start+i))
            quenn_mozliwe_ruchy_biale.append((row_start, column_start,
                                              row_start+i, column_start+i))

        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start+i, column_start-i, gracz)
        if move_tuple[3]:
            if move_tuple[0]:
                quenn_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start + i, column_start + i))
            quenn_mozliwe_ruchy_biale.append((row_start, column_start,
                                              row_start + i, column_start + i))
