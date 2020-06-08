""" Functions important for rules file. """
import board
import const as con
import gra
import rules

def check_available_moves():
    """ Making list of possible moves."""
    gra.Gra.available_moves.clear()
    board.czytaj_figury()

    hits_pawn = pawn_hit()
    hits_queen = queen_hit()
    moves_pawn = pawn_move()
    moves_queen = queen_move()

    if hits_pawn:
    #for ruch in hits_pawn:
        gra.Gra.available_moves.append(hits_pawn)
    #for ruch in hits_queen:
        if hits_queen:
            gra.Gra.available_moves.append(hits_queen)
    elif hits_queen:
        gra.Gra.available_moves.append(hits_queen)
    elif moves_pawn:
    #for ruch in moves_pawn:
        gra.Gra.available_moves.append(moves_pawn)
    elif moves_queen:
    #for ruch in moves_queen:
        gra.Gra.available_moves.append(moves_queen)

    #ruch jako współ. poczatku, srodka i konca
    # lista współrzędnych która odwiedza wszystkie bicia pośrednie i konczy ostatnim
    #jesli zwykly ruch- dwie pary wpsółrzędnych, bicie, wiecej par

def pawn_move():
    """ Funkcja zwraca liste wszystkich mozliwych ruchow gracza. """
    board.czytaj_figury()

    pion_mozliwe_ruchy_biale = []
    pion_mozliwe_ruchy_czarne = []

    if gra.Gra.player == con.PLAYER_ONE:
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


def pawn_hit():
    """ Funkcja wykrywa mozliwe bicia"""
    board.czytaj_figury()

    pion_mozliwe_bicia = []

    if gra.Gra.player == con.PLAYER_ONE:
        for row_start, column_start in gra.Gra.biale_piony:
            for d_row in (-2, +2):
                for d_column in (-2, +2):
                    new_row = row_start + d_row
                    new_column = column_start + d_column
                    if rules.sprawdz_bicie_pionka(row_start, column_start,
                                                  new_row, new_column):
                        pion_mozliwe_bicia.append((row_start, column_start,
                                                   new_row, new_column))
        return pion_mozliwe_bicia

    for row_start, column_start in gra.Gra.czarne_piony:
        for d_row in (-2, +2):
            for d_column in (-2, +2):
                new_row = row_start + d_row
                new_column = column_start + d_column
                if rules.sprawdz_bicie_pionka(row_start, column_start,
                                              new_row, new_column):
                    pion_mozliwe_bicia.append((row_start, column_start,
                                               new_row, new_column))
    return pion_mozliwe_bicia


def pawn_multi_hit(path_list):
    """ Function returing the longest available hits. """
    if gra.Gra.player == con.PLAYER_ONE:
        for row_start, column_start in gra.Gra.biale_piony:
            path = [(row_start, column_start)]
            pawn_single_hit(path, path_list)
    else:
        for row_start, column_start in gra.Gra.czarne_piony:
            path = [(row_start, column_start)]
            pawn_single_hit(path, path_list)

    print(path_list)
    max_len = 0
    for path in path_list:
        if len(path) >= max_len:
            max_len = len(path)

    for i in range(len(path_list) - 1, -1, -1):
        if len(path_list[i]) < max_len:
            path_list.pop(i)

    return path_list


def pawn_single_hit(path, path_list):
    """ Making path of long hitting. """
    row_start, column_start = path[-1]
    for d_row in (-2, +2):
        for d_column in (-2, +2):
            new_row = row_start + d_row
            new_column = column_start + d_column

            if rules.sprawdz_bicie_pionka(row_start, column_start, new_row, new_column):
                path_copy = path[:]
                path_copy.append((new_row, new_column))
                path_list.append(path_copy)
                board.wyswietl()
                move = (row_start, column_start, new_row, new_column)
                remember_figure, jumper = simulate_pawn_hit(move)   # executing a hit
                pawn_single_hit(path_copy, path_list)
                back_simulated_pawn_hit(move, remember_figure, jumper)  # back executed hit



def simulate_pawn_hit(move):
    """ Simulating a pawn hit. """
    row_start, column_start, row_end, column_end = move
    between_row_points = (row_start + row_end) // 2
    between_column_points = (column_start + column_end) // 2

    remember_figure = gra.Gra.plansza[between_row_points][between_column_points]
    jumper = gra.Gra.plansza[row_start][column_start]

    gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
    gra.Gra.plansza[between_row_points][between_column_points] = con.EMPTY_FIELD
    gra.Gra.plansza[row_end][column_end] = jumper
    return remember_figure, jumper


def back_simulated_pawn_hit(move, remember_figure, jumper):
    """ Revoke changes done by simulate_pawn_hit. """
    row_start, column_start, row_end, column_end = move
    between_row_points = (row_start + row_end) // 2
    between_column_points = (column_start + column_end) // 2
    gra.Gra.plansza[row_end][column_end] = con.EMPTY_FIELD
    gra.Gra.plansza[between_row_points][between_column_points] = remember_figure

    gra.Gra.plansza[row_start][column_start] = jumper


def next_pawn_hit(row_start, column_start):
    """ Funkcja wykrywa kolejne mozliwe bicia juz posunietego piona """
    board.czytaj_figury()

    pion_mozliwe_bicia = []

    gra.Gra.dlugi_skok.clear()
    for d_row in (-2, +2):
        for d_column in (-2, +2):
            new_row = row_start + d_row
            new_column = column_start + d_column
            if rules.sprawdz_bicie_pionka(row_start, column_start,
                                          new_row, new_column):
                pion_mozliwe_bicia.append((row_start, column_start,
                                           new_row, new_column))

    if pion_mozliwe_bicia:
        return pion_mozliwe_bicia, True
    return [], False

def queen_move():
    """ Funkcja sprawdza mozliwe ruchy krolowa. """
    board.czytaj_figury()
    queen_mozliwe_ruchy_biale = []
    queen_mozliwe_ruchy_czarne = []

    if gra.Gra.player == con.PLAYER_ONE:
        for skad in gra.Gra.biale_damki:
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] + i)
                if move_tuple[3]:
                    if not move_tuple[0]:
                        queen_mozliwe_ruchy_biale.append((skad[0], skad[1]))

                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] - i)
                if move_tuple[3]:
                    if not move_tuple[0]:
                        queen_mozliwe_ruchy_biale.append((skad[0], skad[1]))

        return queen_mozliwe_ruchy_biale
    for skad in gra.Gra.czarne_damki:
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] + i)
            if move_tuple[3]:
                if not move_tuple[0]:
                    queen_mozliwe_ruchy_czarne.append((skad[0], skad[1]))

            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] - i)

            if move_tuple[3]:
                if not move_tuple[0]:
                    queen_mozliwe_ruchy_czarne.append((skad[0], skad[1]))
    return queen_mozliwe_ruchy_czarne

def queen_hit():
    """ Funkcja sprawdza mozliwe bicia krolowa. """
    board.czytaj_figury()

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()

    if gra.Gra.player == con.PLAYER_ONE:
        for skad in gra.Gra.biale_damki:
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1]+i)
                if move_tuple[3]:
                    if move_tuple[0]:
                        queen_mozliwe_bicia_biale.append((skad[0], skad[1],
                                                          skad[0]+i, skad[1]+i))

                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] - i)
                if move_tuple[3]:
                    if move_tuple[0]:
                        queen_mozliwe_bicia_biale.append((skad[0], skad[1],
                                                          skad[0] + i, skad[1] - i))

        return queen_mozliwe_bicia_biale
    for skad in gra.Gra.czarne_damki:
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] + i)
            if move_tuple[3]:
                if move_tuple[0]:
                    queen_mozliwe_bicia_czarne.append((skad[0], skad[1],
                                                       skad[0] + i, skad[1] + i))

            move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                  skad[0] + i, skad[1] - i)

            if move_tuple[3]:
                if move_tuple[0]:
                    queen_mozliwe_bicia_czarne.append((skad[0], skad[1],
                                                       skad[0] + i, skad[1] - i))
    return queen_mozliwe_bicia_czarne


def next_queen_hit(row_start, column_start):
    """ Funkcja sprawdza mozliwe ruchy i bicia krolowa. """

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()


    if gra.Gra.player == con.PLAYER_ONE:
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                  row_start + i, column_start + i)
            if move_tuple[0]:
                queen_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start + i, column_start + i))

            move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                  row_start + i, column_start - i)
            if move_tuple[0]:
                queen_mozliwe_bicia_biale.append((row_start, column_start,
                                                  row_start + i, column_start - i))

        return queen_mozliwe_bicia_biale
    for i in range(-9, 10, 1):
        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start + i, column_start + i)
        if move_tuple[0] == 1:
            queen_mozliwe_bicia_czarne.append((row_start, column_start,
                                               row_start + i, column_start + i))

        move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                              row_start + i, column_start - i)
        if move_tuple[0] == 1:
            queen_mozliwe_bicia_czarne.append((row_start, column_start,
                                               row_start + i, column_start - i))
    return queen_mozliwe_bicia_czarne
