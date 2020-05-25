""" Module with rules of game """
import pygame

import punktacja as pkt
import nakazy
import board
import const as con
import gra
#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.
# Implementacja jakiegoś drzewka(?)

#Podczas bicia nie można przeskakiwać więcej niż jeden raz przez tę samą bierkę.
# Bierki usuwa się z planszy po wykonaniu bicia.

def sprawdz_pozycje(x_coord, y_coord):
    """ Checking if (x, y) coordinates are correct """
    if -1 < x_coord < con.SIZE:
        if -1 < y_coord < con.SIZE:
            return True
    return False


def ruch_gracza(row_start, column_start, row_end, column_end, gracz, gracz_k):
    """ Moving a figure """
    ruch = (row_start, column_start, row_end, column_end)
    if sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
        between_row_points = int((row_start + row_end) / 2)
        between_column_points = int((column_start + column_end) / 2)

        #Zapisywanie jaką figurą wykonuje ruch
        if gra.Gra.plansza[row_start][column_start] == gra.Gra.figury[-gracz]:
            figure = gra.Gra.figury[-gracz]
            pion = 1

        elif gra.Gra.plansza[row_start][column_start] == gra.Gra.figury[-gracz - 1]:
            figure = gra.Gra.figury[-gracz - 1]
            pion = 0

        else:
            print("Ruch niedozwolonyyy")
            return False

        if pion:                        # Prawda gdy figura to pionek
            #OBSLUGA PIONKA
            if nakazy.pawn_hit(gracz):         # jesli istnieja bicia, musze je wykonac
                if ruch in nakazy.pawn_hit(gracz):

                    gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD

                    pkt.punkty_bicie_pionem(ruch, gracz, gracz_k)     # tylko dla pionow

                    gra.Gra.plansza[between_row_points][between_column_points] = con.EMPTY_FIELD
                    gra.Gra.plansza[row_end][column_end] = figure



                    pkt.punkty_update(row_start, column_start, row_end, column_end, gracz, gracz_k)
                    ### Wynonanie fnkcji podobnej do ruch_gracza,
                    # ale parametr row/column_end staje sie poczatkowym,
                    # jesli nie ma takiego bicia, fałsz

                    if nakazy.next_pawn_hit(row_end, column_end, gracz)[1]:
                        gra.Gra.attack_from.clear()
                        gra.Gra.attack_from.append(row_end)
                        gra.Gra.attack_from.append(column_end)
                        return False
                    else:
                        gra.Gra.attack_from.clear()
                    board.wyniesienie(row_end, column_end, gracz)
                    return True
                return False

            if nakazy.quenn_move(gracz):
                print("Krolowa moze bic")
                return False

            if ruch in nakazy.pawn_move(gracz):
                gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
                gra.Gra.plansza[row_end][column_end] = figure
            else:
                print("Ruch niedozwolony")
                return False
        else:
            #OBSLUGA DAMKI
            if not (row_start, column_start) in nakazy.quenn_move(gracz):
                if nakazy.pawn_hit(gracz):
                    print("Musisz bic pionem")
                    return False

            krotka = sprawdz_ruch_damki(row_start, column_start, row_end, column_end, gracz)

            if krotka[3]:   # Prawda/fałsz  ruch prawidłowy / ruch nieprawidłowy
                if krotka[0] == 1:   # Prawda/ fałsz     Bicie / zwykly ruch
                    gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD

                    pkt.punkty_bicie_damka(krotka, gracz, gracz_k)

                    gra.Gra.plansza[krotka[1]][krotka[2]] = con.EMPTY_FIELD
                    gra.Gra.plansza[row_end][column_end] = figure
                elif (row_start, column_start) in nakazy.quenn_move(gracz):
                    print("Musisz bic")
                    return False
                else:
                    gra.Gra.plansza[row_start][column_start] = con.EMPTY_FIELD
                    gra.Gra.plansza[row_end][column_end] = figure

            else:
                print(krotka[4])
                return False

        board.wyniesienie(row_end, column_end, gracz)
        pkt.punkty_update(row_start, column_start, row_end, column_end, gracz, gracz_k)
        return True
    print("niepoprawne dane")
    return False


def sprawdz_bicie_pionka(row_start, column_start, row_end, column_end, gracz):
    """ Check if hitting enemy figure is possible"""

    if not sprawdz_pozycje(row_end, column_end):
        return False
    between_row_points = int((row_start + row_end) / 2)
    between_column_points = int((column_start + column_end) / 2)
    if abs(row_end - row_start) == 2 and abs(column_start - column_end) == 2:
        if gra.Gra.plansza[row_end][column_end] == con.EMPTY_FIELD:
            if gra.Gra.plansza[between_row_points][between_column_points] == gra.Gra.figury[gracz]:
                return True
            if gra.Gra.plansza[between_row_points][between_column_points] == gra.Gra.figury[gracz-1]:
                return True
            return False
        return False
    return False


def sprawdz_ruch_damki(row_start, column_start, row_end, column_end, gracz):
    """ Sprawdza ruch damki, zwraca liczbe pionków przeciwnika pomiedzy,
    pozycje x,y pionka przeciwnika oraz czy ruch mozliwy"""
    if not sprawdz_pozycje(row_end, column_end):
        return 0, 0, 0, False, "Niepoprawny cel"

    licznik_pionow = 0
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

    #r_step = row_start + row_step
    #c_step = column_start + column_step

    if gra.Gra.plansza[row_end][column_end] == con.EMPTY_FIELD and abs(row) == abs(column) and row != 0:
        x_pawn = 0
        y_pawn = 0
        for _ in range(abs(column_end - column_start)):
            r_step = row_start + row_step
            c_step = column_start + column_step
            if gra.Gra.plansza[r_step][c_step] == gra.Gra.figury[gracz] \
                    or gra.Gra.plansza[r_step][c_step] == gra.Gra.figury[gracz-1]:
                licznik_pionow += 1
                x_pawn = r_step
                y_pawn = c_step
            elif gra.Gra.plansza[r_step][c_step] == gra.Gra.figury[-gracz] \
                    or gra.Gra.plansza[r_step][c_step] == gra.Gra.figury[gracz+1]:
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
            return licznik_pionow, x_pawn, y_pawn, True

    return 0, 0, 0, False, "Blad ruchu"
