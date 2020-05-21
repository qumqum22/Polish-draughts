""" Module with rules of game """
import pygame

import punktacja as pkt
import nakazy
import board
import const as c
#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.
# Implementacja jakiegoś drzewka(?)

#Podczas bicia nie można przeskakiwać więcej niż jeden raz przez tę samą bierkę.
# Bierki usuwa się z planszy po wykonaniu bicia.

def sprawdz_pozycje(x_coord, y_coord):
    """ Checking if (x, y) coordinates are correct """
    if -1 < x_coord < c.SIZE:
        if -1 < y_coord < c.SIZE:
            return True
    return False

def ruch_gracza(row_start, column_start, row_end, column_end, gracz, gracz_k):
    """ Moving a figure """
    ruch = (row_start, column_start, row_end, column_end)
    if sprawdz_pozycje(row_start, column_start) and sprawdz_pozycje(row_end, column_end):
        between_row_points = int((row_start + row_end) / 2)
        between_column_points = int((column_start + column_end) / 2)

        #Zapisywanie jaką figurą wykonuje ruch
        if c.plansza[row_start][column_start] == c.figury[-gracz]:
            figure = c.figury[-gracz]
            pion = 1

        elif c.plansza[row_start][column_start] == c.figury[-gracz - 1]:
            figure = c.figury[-gracz - 1]
            pion = 0

        else:
            print("Ruch niedozwolonyyy")
            return False

        if pion:                        # Prawda gdy figura to pionek
            #OBSLUGA PIONKA
            if nakazy.pawn_hit(gracz):         # jesli istnieja bicia, musze je wykonac
                if ruch in nakazy.pawn_hit(gracz):

                    #Zamienic to na funkcje
                    c.plansza[row_start][column_start] = c.EMPTY_FIELD
                    #Odejmowanie punktow przeciwnikowi od piona i od pozycji piona
                    if c.plansza[between_row_points][between_column_points] == c.WHITE_PAWN:
                        c.biale += -c.POINTS_PAWN
                        c.biale += -pkt.punkty_planszy(between_row_points, between_column_points,
                                                       -gracz, gracz * gracz_k - 1)
                    elif c.plansza[between_row_points][between_column_points] == c.BLACK_PAWN:
                        c.czarne += -c.POINTS_PAWN
                        c.czarne += -pkt.punkty_planszy(between_row_points, between_column_points,
                                                        -gracz, gracz * gracz_k - 1)
                    elif c.plansza[between_row_points][between_column_points] == c.WHITE_QUENN:
                        c.biale += -c.POINTS_QUENN
                        c.biale += -pkt.punkty_planszy(between_row_points, between_column_points,
                                                       -gracz, gracz * gracz_k - 1)
                    else:
                        c.czarne += -c.POINTS_QUENN
                        c.czarne += -pkt.punkty_planszy(between_row_points, between_column_points,
                                                        -gracz, gracz * gracz_k - 1)
                    c.plansza[between_row_points][between_column_points] = c.EMPTY_FIELD
                    c.plansza[row_end][column_end] = figure
                    pkt.punkty_update(row_start, column_start, row_end, column_end, gracz, gracz_k)
                    ### Wynonanie fnkcji podobnej do ruch_gracza,
                    # ale parametr row/column_end staje sie poczatkowym,
                    # jesli nie ma takiego bicia, fałsz
                    if nakazy.next_pawn_hit(row_end, column_end, gracz)[1]:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                start_x, start_y = pygame.mouse.get_pos()
                                start_x = int((start_x - c.PLANSZA_X) / c.FIELD)
                                start_y = int((start_y - c.PLANSZA_Y) / c.FIELD)

                            #  ODCZYT POLOZENIA KONCOWEGO MYSZKI
                            if event.type == pygame.MOUSEBUTTONUP:
                                end_x, end_y = pygame.mouse.get_pos()
                                end_x = int((end_x - c.PLANSZA_X) / c.FIELD)
                                end_y = int((end_y - c.PLANSZA_Y) / c.FIELD)
                                if (row_end, column_end, end_x, end_y) in \
                                        nakazy.next_pawn_hit(row_end, column_end, gracz):
                                    ruch_gracza(row_end, column_end, end_x, end_y, gracz, gracz_k)
                                else:
                                    print("Blad")
                    board.wyniesienie(row_end, column_end, gracz)
                    return True
                return False

            if ruch in nakazy.pawn_move(gracz):
                c.plansza[row_start][column_start] = c.EMPTY_FIELD
                c.plansza[row_end][column_end] = figure
            else:
                print("Ruch niedozwolony")
                return False
        else:
            #OBSLUGA DAMKI
            krotka = sprawdz_ruch_damki(row_start, column_start, row_end, column_end, gracz)

            if krotka[3]:   # Prawda/fałsz  ruch prawidłowy / ruch nieprawidłowy
                if krotka[0] == 1:   # Prawda/ fałsz     Bicie / zwykly ruch
                    c.plansza[row_start][column_start] = c.EMPTY_FIELD
                    #Odejmowanie punktow przeciwnikowi od piona i od pozycji piona
                    if c.plansza[krotka[1]][krotka[2]] == c.WHITE_PAWN:
                        c.biale += -c.POINTS_PAWN
                        c.biale += -pkt.punkty_planszy(krotka[1], krotka[2],
                                                       -gracz, gracz * gracz_k - 1)
                    elif c.plansza[krotka[1]][krotka[2]] == c.BLACK_PAWN:
                        c.czarne += -c.POINTS_PAWN
                        c.czarne += -pkt.punkty_planszy(krotka[1], krotka[2],
                                                        -gracz, gracz * gracz_k - 1)
                    elif c.plansza[krotka[1]][krotka[2]] == c.WHITE_QUENN:
                        c.biale += -c.POINTS_QUENN
                        c.biale += -pkt.punkty_planszy(krotka[1], krotka[2],
                                                       -gracz, gracz * gracz_k - 1)
                    else:
                        c.czarne += -c.POINTS_QUENN
                        c.czarne += -pkt.punkty_planszy(krotka[1], krotka[2],
                                                        -gracz, gracz * gracz_k - 1)
                    c.plansza[krotka[1]][krotka[2]] = c.EMPTY_FIELD
                    c.plansza[row_end][column_end] = figure
                else:
                    c.plansza[row_start][column_start] = c.EMPTY_FIELD
                    c.plansza[row_end][column_end] = figure
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
        if c.plansza[row_end][column_end] == c.EMPTY_FIELD:
            if c.plansza[between_row_points][between_column_points] == c.figury[gracz]:
                return True
            if c.plansza[between_row_points][between_column_points] == c.figury[gracz-1]:
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

    if c.plansza[row_end][column_end] == c.EMPTY_FIELD and abs(row) == abs(column) and row != 0:
        x_pawn = 0
        y_pawn = 0
        for i in range(abs(column_end - column_start)):
            r_step = row_start + row_step
            c_step = column_start + column_step
            if c.plansza[r_step][c_step] == c.figury[gracz] \
                    or c.plansza[r_step][c_step] == c.figury[gracz-1]:
                licznik_pionow += 1
                x_pawn = r_step
                y_pawn = c_step
            elif c.plansza[r_step][c_step] == c.figury[-gracz] \
                    or c.plansza[r_step][c_step] == c.figury[gracz+1]:
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
