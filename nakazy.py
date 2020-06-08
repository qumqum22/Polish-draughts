""" Functions important for rules file. """
import board
import const as con
import gra
import rules


def check_available_moves(path_list):
    """ Making list of possible moves."""
    gra.Gra.available_moves.clear()
    board.czytaj_figury()

    pawn_multi_hit(path_list)
    queen_multi_hit(path_list)

    if not path_list:
        pawn_move(path_list)
        queen_move(path_list)


def pawn_move(path_list):
    """ Funkcja zwraca liste wszystkich mozliwych ruchow gracza. """
    board.czytaj_figury()

    if gra.Gra.player == con.PLAYER_ONE:
        for row_start, column_start in gra.Gra.biale_piony:
            path = []
            if rules.sprawdz_pozycje(row_start-1, column_start+1):
                if gra.Gra.plansza[row_start - 1][column_start + 1] == con.EMPTY_FIELD:
                    path.append((row_start, column_start))
                    path.append((row_start-1, column_start+1))
                    path_list.append(path)
            path = []

            if rules.sprawdz_pozycje(row_start - 1, column_start - 1):
                if gra.Gra.plansza[row_start-1][column_start-1] == con.EMPTY_FIELD:
                    path.append((row_start, column_start))
                    path.append((row_start - 1, column_start - 1))
                    path_list.append(path)
    else:
        for row_start, column_start in gra.Gra.czarne_piony:
            path = []
            if rules.sprawdz_pozycje(row_start + 1, column_start + 1):
                if gra.Gra.plansza[row_start + 1][column_start + 1] == con.EMPTY_FIELD:
                    path.append((row_start, column_start))
                    path.append((row_start + 1, column_start + 1))
                    path_list.append(path)

            path = []
            if rules.sprawdz_pozycje(row_start + 1, column_start - 1):
                if gra.Gra.plansza[row_start + 1][column_start - 1] == con.EMPTY_FIELD:
                    path.append((row_start, column_start))
                    path.append((row_start + 1, column_start - 1))
                    path_list.append(path)


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


def queen_move(path_list):
    """ Funkcja sprawdza mozliwe ruchy krolowa. """
    board.czytaj_figury()

    if gra.Gra.player == con.PLAYER_ONE:
        for skad in gra.Gra.biale_damki:
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] + i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] + i))
                    path_list.append(path)

                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] - i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] - i))
                    path_list.append(path)

    else:
        for skad in gra.Gra.czarne_damki:
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] + i)
                path = []
                if move_tuple[3]:
                    if not move_tuple[0]:
                        path.append((skad[0], skad[1]))
                        path.append((skad[0] + i, skad[1] + i))
                        path_list.append(path)
                        path.clear()

                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] - i)
                path = []
                if move_tuple[3]:
                    if not move_tuple[0]:
                        path.append((skad[0], skad[1]))
                        path.append((skad[0] + i, skad[1] - i))
                        path_list.append(path)
                        path.clear()


def queen_multi_hit(path_list):
    """ Function returning the longest available hits. """
    if gra.Gra.player == con.PLAYER_ONE:
        for row_start, column_start in gra.Gra.biale_damki:
            path = [(row_start, column_start)]
            queen_single_hit(path, path_list)
    else:
        for row_start, column_start in gra.Gra.czarne_damki:
            path = [(row_start, column_start)]
            queen_single_hit(path, path_list)


def queen_single_hit(path, path_list):
    """ Making path of queen hitting. """
    row_start, column_start = path[-1]
    for i_row in range(-9, 10, 1):
        for i_column in range(-9, 10, 1):
            new_row = row_start + i_row
            new_column = column_start + i_column
            move_queen = rules.sprawdz_ruch_damki(row_start, column_start, new_row, new_column)
            if move_queen[3]:
                if move_queen[0]:
                    path_copy = path[:]
                    path_copy.append((new_row, new_column))
                    path_list.append(path_copy)
                    move = (row_start, column_start, new_row, new_column)
                    enemy_pawn = (move_queen[1], move_queen[2])
                    remember_figure, jumper = simulate_queen_hit(move, enemy_pawn)
                    queen_single_hit(path_copy, path_list)
                    back_simulated_queen_hit(move, enemy_pawn, remember_figure, jumper)


def simulate_queen_hit(move, hit):
    """ Moving a pawns during creating available moves. """
    row_start, column_start, row_end, column_end = move
    row_enemy, column_enemy = hit

    remember_figure = gra.Gra.plansza[row_enemy][column_enemy]
    jumper = gra.Gra.plansza[row_start][column_start]

    gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
    gra.Gra.plansza[row_enemy][column_enemy] = con.EMPTY_FIELD
    gra.Gra.plansza[row_end][column_end] = jumper
    return remember_figure, jumper


def back_simulated_queen_hit(move, enemy_pawn, remember_figure, jumper):
    """ Moving a pawns back during creating available moves. """
    row_start, column_start, row_end, column_end = move
    row_enemy, column_enemy = enemy_pawn

    gra.Gra.plansza[row_start][column_start] = jumper
    gra.Gra.plansza[row_enemy][column_enemy] = remember_figure
    gra.Gra.plansza[row_end][column_end] = con.EMPTY_FIELD


def back_simulated_queen_move(move, jumper):
    """ Moving a pawns back during creating available moves. """
    row_start, column_start, row_end, column_end = move

    gra.Gra.plansza[row_start][column_start] = jumper
    gra.Gra.plansza[row_end][column_end] = con.EMPTY_FIELD


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


def next_queen_hit(row_start, column_start):
    """ Funkcja sprawdza mozliwe ruchy i bicia krolowa. """

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()


    if gra.Gra.player == con.PLAYER_ONE:
        for sign in (-1, 1):
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                      row_start + i, column_start + sign * i)
                if move_tuple[0]:
                    queen_mozliwe_bicia_biale.append((row_start, column_start,
                                                      row_start + i, column_start + sign * i))
        return queen_mozliwe_bicia_biale
    for sign in (-1, 1):
        for i in range(-9, 10, 1):
            move_tuple = rules.sprawdz_ruch_damki(row_start, column_start,
                                                  row_start + i, column_start + sign * i)
            if move_tuple[0] == 1:
                queen_mozliwe_bicia_czarne.append((row_start, column_start,
                                                   row_start + i, column_start + sign * i))
    return queen_mozliwe_bicia_czarne


def queen_hit():
    """ Funkcja sprawdza mozliwe bicia krolowa. """
    board.czytaj_figury()

    queen_mozliwe_bicia_biale = []
    queen_mozliwe_bicia_czarne = []

    queen_mozliwe_bicia_biale.clear()
    queen_mozliwe_bicia_czarne.clear()

    if gra.Gra.player == con.PLAYER_ONE:
        for skad in gra.Gra.biale_damki:
            for sign in (-1, 1):
                for i in range(-9, 10, 1):
                    move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                          skad[0] + i, skad[1] + sign * i)
                    if move_tuple[0]:
                        queen_mozliwe_bicia_biale.append((skad[0], skad[1],
                                                          skad[0]+i, skad[1] + sign * i))

        return queen_mozliwe_bicia_biale
    for skad in gra.Gra.czarne_damki:
        for sign in (-1, 1):
            for i in range(-9, 10, 1):
                move_tuple = rules.sprawdz_ruch_damki(skad[0], skad[1],
                                                      skad[0] + i, skad[1] + sign * i)
                if move_tuple[0]:
                    queen_mozliwe_bicia_czarne.append((skad[0], skad[1],
                                                       skad[0] + i, skad[1] + sign * i))
    return queen_mozliwe_bicia_czarne
