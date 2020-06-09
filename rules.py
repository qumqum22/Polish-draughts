""" Module with rules of game """
import board
import const as con
import gra
import punktacja as pkt


#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.
# Implementacja jakiegoś drzewka(?)

def sprawdz_pozycje(x_coord, y_coord):
    """ Checking if (x, y) coordinates are correct """
    if -1 < x_coord < con.SIZE:
        if -1 < y_coord < con.SIZE:
            return True
    return False


def select_available_moves(path_list):
    """ Selecting the longest available moves. """
    max_len = 0
    for path in path_list:
        if len(path) >= max_len:
            max_len = len(path)

    for i in range(len(path_list) - 1, -1, -1):
        if len(path_list[i]) < max_len:
            path_list.pop(i)


# Czy funkcja minmax zlicza punkty przed ruchem, po ruchu i oblicza roznice : obojetne
# Ma patrzec czasowo, na podstawie wyniku czasu mniejszej glebokosci

def ruch_gracza(row_start, column_start, row_end, column_end):
    """ Moving a figure """
    ruch = (row_start, column_start, row_end, column_end)
    move_from = (row_start, column_start)

    select_available_moves(gra.Gra.path_list)

    if not sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
        return False

    between_row_points = (row_start + row_end) // 2
    between_column_points = (column_start + column_end) // 2
    between = (between_row_points, between_column_points)

    if gra.Gra.attack_from:
        if sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
            for path in gra.Gra.path_list:
                if path[1] == move_from and path[2] == (row_end, column_end):
                    break
            else:
                return False

        for path in gra.Gra.path_list:#in range(len(gra.Gra.path_list) - 1, -1, -1):
            print('sprawdzam {}'.format(path))
            if not path[1] == move_from:
                gra.Gra.path_list.remove(path)
            else:
                path.pop(0)

    print('All max: {}'.format(gra.Gra.path_list))

    if sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
        between_row_points = (row_start + row_end) // 2
        between_column_points = (column_start + column_end) // 2
        between = (between_row_points, between_column_points)
        if gra.Gra.player == con.PLAYER_ONE:
            #Zapisywanie jaką figurą wykonuje ruch
            if gra.Gra.plansza[row_start][column_start] == con.WHITE_PAWN:
                figure = con.WHITE_PAWN
                return service_pawn(ruch, between, figure, gra.Gra.path_list)

            if gra.Gra.plansza[row_start][column_start] == con.WHITE_QUEEN:
                figure = con.WHITE_QUEEN
                return service_queen(ruch, figure, gra.Gra.path_list)
        else:
            if gra.Gra.plansza[row_start][column_start] == con.BLACK_PAWN:
                figure = con.BLACK_PAWN
                return service_pawn(ruch, between, figure, gra.Gra.path_list)

            if gra.Gra.plansza[row_start][column_start] == con.BLACK_QUEEN:
                figure = con.BLACK_QUEEN
                return service_queen(ruch, figure, gra.Gra.path_list)

    print("niepoprawne dane")
    return False


def sprawdz_bicie_pionka(row_start, column_start, row_end, column_end):
    """ Check if hitting enemy figure is possible"""
    if not sprawdz_pozycje(row_end, column_end):
        return False
    if abs(row_end - row_start) == 2 and abs(column_start - column_end) == 2:
        between_row_points = (row_start + row_end) // 2
        between_column_points = (column_start + column_end) // 2

        if gra.Gra.player == con.PLAYER_ONE:
            if gra.Gra.plansza[row_end][column_end] == con.EMPTY_FIELD:
                if gra.Gra.plansza[between_row_points][between_column_points] \
                        in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    return True
        else:
            if gra.Gra.plansza[row_end][column_end] == con.EMPTY_FIELD:
                if gra.Gra.plansza[between_row_points][between_column_points] \
                        in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    return True
    return False



def sprawdz_ruch_damki(row_start, column_start, row_end, column_end):
    """ Sprawdza ruch damki, zwraca liczbe pionków przeciwnika pomiedzy,
    pozycje x,y pionka przeciwnika oraz czy ruch mozliwy"""
    if not sprawdz_pozycje(row_end, column_end):
        return 0, 0, 0, False, "Niepoprawny cel"

    row = row_end - row_start
    column = column_end - column_start

    if row > 0:
        row_step = 1
    else:
        row_step = -1

    if column > 0:
        column_step = 1
    else:
        column_step = -1

    ruch = (row_start, column_start, row_end, column_end)
    row_column = (row, column)
    return sprawdz_mozliwosci_damki(ruch, row_column, row_step, column_step)


def sprawdz_mozliwosci_damki(ruch, lane, row_step, column_step):
    """ Function checking move for queen. """
    licznik_pionow = 0
    if gra.Gra.plansza[ruch[2]][ruch[3]] == con.EMPTY_FIELD \
            and abs(lane[0]) == abs(lane[1]) and lane[0] != 0:
        x_pawn = 0
        y_pawn = 0
        for _ in range(abs(ruch[3] - ruch[1])):
            r_step = ruch[0] + row_step
            c_step = ruch[1] + column_step
            if gra.Gra.player == con.PLAYER_ONE:
                if gra.Gra.plansza[r_step][c_step] in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    licznik_pionow += 1
                    x_pawn = r_step
                    y_pawn = c_step
                elif gra.Gra.plansza[r_step][c_step] in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    return 0, 0, 0, False, "Nie mozesz skakac poprzez swoich"
            else:
                if gra.Gra.plansza[r_step][c_step] in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    licznik_pionow += 1
                    x_pawn = r_step
                    y_pawn = c_step
                elif gra.Gra.plansza[r_step][c_step] in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    return 0, 0, 0, False, "Nie mozesz skakac poprzez swoich"

            if row_step > 0:
                row_step += 1
            else:
                row_step -= 1
            if column_step > 0:
                column_step += 1
            else:
                column_step -= 1
        if licznik_pionow < 2:
            return licznik_pionow, x_pawn, y_pawn, True, "Poprawny ruch"

    return 0, 0, 0, False, "Blad ruchu"


def service_pawn(move, between, figure, path_list):
    """OBSLUGA PIONKA. """
    row_start, column_start, row_end, column_end = move
    between_row_points, between_column_points = between

    for path_element in path_list:
        if ((row_start, column_start), (row_end, column_end)) == (path_element[0], path_element[1]):

            gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
            gra.Gra.plansza[between_row_points][between_column_points] = con.EMPTY_FIELD
            if abs(row_end - row_start) == 2:
                pkt.punkty_bicie_pionem(move)
            gra.Gra.plansza[row_end][column_end] = figure
            pkt.punkty_update(row_start, column_start, row_end, column_end)

            if len(path_element) > 2:
                gra.Gra.attack_from.clear()
                gra.Gra.attack_from.append(path_element[1])
                print(gra.Gra.attack_from)
                return False
            board.wyniesienie(row_end, column_end)
            gra.Gra.attack_from.clear()
            return True
    print("Ruch niedozwolony")
    return False


def service_queen(move, figure, path_list):
    """OBSLUGA DAMKI. """
    row_start, column_start, row_end, column_end = move

    for path_element in path_list:
        if ((row_start, column_start), (row_end, column_end)) == (path_element[0], path_element[1]):

            krotka = sprawdz_ruch_damki(row_start, column_start, row_end, column_end)

            if krotka[0] == 1:  # Prawda/ fałsz     Bicie / zwykly ruch
                gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD

                pkt.punkty_bicie_damka(krotka)

                gra.Gra.plansza[krotka[1]][krotka[2]] = con.EMPTY_FIELD
                gra.Gra.plansza[row_end][column_end] = figure

                if len(path_element) > 2:
                    gra.Gra.attack_from.clear()
                    gra.Gra.attack_from.append(path_element[1])
                    pkt.punkty_update(row_start, column_start, row_end, column_end)
                    print(gra.Gra.attack_from)
                    return False
            else:
                gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
                gra.Gra.plansza[row_end][column_end] = figure

            pkt.punkty_update(row_start, column_start, row_end, column_end)
            gra.Gra.attack_from.clear()
            return True
    return False
