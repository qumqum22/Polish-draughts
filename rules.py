""" Module with rules of game """
import board
import const as con
import gra
import nakazy
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

def ruch_gracza(row_start, column_start, row_end, column_end):
    """ Moving a figure """
    ruch = (row_start, column_start, row_end, column_end)
    nakazy.check_available_moves()
    print(gra.Gra.available_moves)

    if sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
        between_row_points = (row_start + row_end) // 2
        between_column_points = (column_start + column_end) // 2
        between = (between_row_points, between_column_points)

        if gra.Gra.player == con.PLAYER_ONE:
            #Zapisywanie jaką figurą wykonuje ruch
            if gra.Gra.plansza[row_start][column_start] == con.WHITE_PAWN:
                figure = con.WHITE_PAWN
                pion = 1

            elif gra.Gra.plansza[row_start][column_start] == con.WHITE_QUEEN:
                figure = con.WHITE_QUEEN
                pion = 0

            else:
                print("Ruch niedozwolonyyy")
                return False
        else:
            if gra.Gra.plansza[row_start][column_start] == con.BLACK_PAWN:
                figure = con.BLACK_PAWN
                pion = 1

            elif gra.Gra.plansza[row_start][column_start] == con.BLACK_QUEEN:
                figure = con.BLACK_QUEEN
                pion = 0
            else:
                print("Ruch niedozwolonyyy")
                return False

        if pion:  # Prawda gdy figura to pionek
            return service_pawn(ruch, between, figure)
        return service_queen(ruch, figure)
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
                if gra.Gra.plansza[between_row_points][between_column_points] in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    return True
        else:
            if gra.Gra.plansza[row_end][column_end] == con.EMPTY_FIELD:
                if gra.Gra.plansza[between_row_points][between_column_points] in [con.WHITE_PAWN, con.WHITE_QUEEN]:
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

def service_pawn(move, between, figure):
    """OBSLUGA PIONKA. """
    row_start, column_start, row_end, column_end = move
    between_row_points, between_column_points = between
    if nakazy.pawn_hit():  # jesli istnieja bicia, musze je wykonac
        if move in nakazy.pawn_hit():

            gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD

            pkt.punkty_bicie_pionem(move)

            gra.Gra.plansza[between_row_points][between_column_points] = con.EMPTY_FIELD
            gra.Gra.plansza[row_end][column_end] = figure

            pkt.punkty_update(row_start, column_start, row_end, column_end)
            ### Wynonanie fnkcji podobnej do ruch_gracza,
            # ale parametr row/column_end staje sie poczatkowym,
            # jesli nie ma takiego bicia, fałsz

            if nakazy.next_pawn_hit(row_end, column_end)[1]:
                gra.Gra.attack_from.clear()
                gra.Gra.attack_from.append(row_end)
                gra.Gra.attack_from.append(column_end)
                return False
            board.wyniesienie(row_end, column_end)
            gra.Gra.attack_from.clear()
            return True
        return False

    if nakazy.queen_hit():
        print("Krolowa moze bic")
        return False

    if move in nakazy.pawn_move():
        gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
        gra.Gra.plansza[row_end][column_end] = figure
        pkt.punkty_update(row_start, column_start, row_end, column_end)
        board.wyniesienie(row_end, column_end)
        gra.Gra.attack_from.clear()
        return True
    print("Ruch niedozwolony")
    return False

def service_queen(move, figure):
    """OBSLUGA DAMKI. """
    row_start, column_start, row_end, column_end = move
    if not (row_start, column_start, row_end, column_end) in nakazy.queen_hit():
        if nakazy.pawn_hit():
            print("Musisz bic pionem")
            return False
        if nakazy.queen_hit():
            print("Musisz bic krolowa")
            return False

    krotka = sprawdz_ruch_damki(row_start, column_start, row_end, column_end)

    if krotka[3]:  # Prawda/fałsz  ruch prawidłowy / ruch nieprawidłowy
        if krotka[0] == 1:  # Prawda/ fałsz     Bicie / zwykly ruch
            gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD

            pkt.punkty_bicie_damka(krotka)

            gra.Gra.plansza[krotka[1]][krotka[2]] = con.EMPTY_FIELD
            gra.Gra.plansza[row_end][column_end] = figure

            if nakazy.next_queen_hit(row_end, column_end):
                gra.Gra.attack_from.clear()
                pkt.punkty_update(row_start, column_start, row_end, column_end)
                gra.Gra.attack_from.append(row_end)
                gra.Gra.attack_from.append(column_end)
                return False

        elif (row_start, column_start, row_end, column_end) in nakazy.queen_hit():
            print("Musisz bic")
            return False
        else:
            gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
            gra.Gra.plansza[row_end][column_end] = figure
    else:
        print(krotka[4])
        return False
    board.wyniesienie(row_end, column_end)
    pkt.punkty_update(row_start, column_start, row_end, column_end)
    gra.Gra.attack_from.clear()
    return True
