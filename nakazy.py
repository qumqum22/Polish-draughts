""" Functions important for rules file. """
import board
import const as con
import gra
import rules


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
        for row_start, column_start in gra.Gra.biale_piony:
            if rules.sprawdz_pozycje(row_start-1, column_start+1):
                if gra.Gra.plansza[row_start-1][column_start+1] == con.EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start,
                                                     row_start - 1, column_start + 1))
            if rules.sprawdz_pozycje(row_start - 1, column_start - 1):
                if gra.Gra.plansza[row_start-1][column_start-1] == con.EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start,
                                                     row_start - 1, column_start - 1))
        return pion_mozliwe_ruchy_biale
    for row_start, column_start in gra.Gra.czarne_piony:
        if rules.sprawdz_pozycje(row_start + 1, column_start + 1):
            if gra.Gra.plansza[row_start+1][column_start+1] == con.EMPTY_FIELD:
                pion_mozliwe_ruchy_czarne.append((row_start, column_start,
                                                  row_start + 1, column_start + 1))
        if rules.sprawdz_pozycje(row_start + 1, column_start - 1):
            if gra.Gra.plansza[row_start+1][column_start-1] == con.EMPTY_FIELD:
                pion_mozliwe_ruchy_czarne.append((row_start, column_start,
                                                  row_start + 1, column_start - 1))
    return pion_mozliwe_ruchy_czarne


def pawn_hit(gracz):
    """ Funkcja wykrywa mozliwe bicia"""
    board.czytaj_figury()

    pion_mozliwe_bicia = []
    pion_mozliwe_bicia.clear()

    if gracz == 1:
        for pionek in gra.Gra.biale_piony:
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

    for pionek in gra.Gra.czarne_piony:
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


def queen_move(gracz):
    """ Funkcja sprawdza mozliwe ruchy i bicia krolowa. """
    board.czytaj_figury()

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()


    if gracz == 1:
        for skad in gra.Gra.biale_damki:
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0]+i, skad[1]+i, gracz)
                if move_tuple[3]:
                    if move_tuple[0]:
                        queen_mozliwe_bicia_biale.append((skad[0], skad[1]))

                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0]+i, skad[1] - i, gracz)
                if move_tuple[3]:
                    if move_tuple[0]:
                        queen_mozliwe_bicia_biale.append((skad[0], skad[1]))

        return queen_mozliwe_bicia_biale
    for skad in gra.Gra.czarne_damki:
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] + i, gracz)
            if move_tuple[3]:
                if move_tuple[0]:
                    queen_mozliwe_bicia_czarne.append((skad[0], skad[1]))

            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] - i, gracz)

            if move_tuple[3]:
                if move_tuple[0]:
                    queen_mozliwe_bicia_czarne.append((skad[0], skad[1]))
    return queen_mozliwe_bicia_czarne


def next_queen_hit(row_start, column_start, gracz):
    """ Funkcja sprawdza mozliwe ruchy i bicia krolowa. """

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()


    if gracz == 1:
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                  row_start + i, column_start + i, gracz)
            if move_tuple[0]:
                queen_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start + i, column_start + i))

            move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                  row_start + i, column_start - i, gracz)
            if move_tuple[0]:
                queen_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start + i, column_start - i))

        return queen_mozliwe_bicia_biale
    for i in range(-9, 10, 1):
        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start + i, column_start + i, gracz)
        if move_tuple[0] == 1:
            queen_mozliwe_bicia_czarne.append((row_start, column_start,
                                               row_start + i, column_start + i))

        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start + i, column_start - i, gracz)
        if move_tuple[0] == 1:
            queen_mozliwe_bicia_czarne.append((row_start, column_start,
                                               row_start + i, column_start - i))
    return queen_mozliwe_bicia_czarne
