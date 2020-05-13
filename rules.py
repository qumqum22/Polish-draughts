from const import *
from temp import *
from punktacja import *
import board
#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.
# Implementacja jakiegoś drzewka(?)

#Podczas bicia nie można przeskakiwać więcej niż jeden raz przez tę samą bierkę.
# Bierki usuwa się z planszy po wykonaniu bicia.

mozliwe_ruchy_biale = []
mozliwe_ruchy_czarne = []

mozliwe_bicia_biale = []
mozliwe_bicia_czarne = []


def pionRuch(row_start, column_start, gracz, graczK):
    pass    # czy pion moze sie ruszyc. Biale w gore, czarne w dół

def pionBicie(row_start, column_start, gracz, graczK):
    pass


def ruchGracza(row_start, column_start, row_end, column_end, gracz, graczK):
    #row_start, column_start = translate(od)
    #row_end, column_end = translate(do)
    if sprawdzPozycje(row_start, column_start) and sprawdzPozycje(row_end, column_end):
        between_row_points = int((row_start + row_end) / 2)
        between_column_points = int((column_start + column_end) / 2)
        if gracz == 1 and plansza[row_start][column_start] == WHITE_PAWN:
            figure = WHITE_PAWN
            pion = 1
        elif gracz == -1 and plansza[row_start][column_start] == BLACK_PAWN:
            figure = BLACK_PAWN
            pion = 1
        elif gracz == 1 and plansza[row_start][column_start] == WHITE_QUENN:
            figure = WHITE_QUENN
            pion = 0
        elif gracz == -1 and plansza[row_start][column_start] == BLACK_QUENN:
            figure = BLACK_QUENN
            pion = 0
        else:
            print("Ruch niedozwolonyyy")
            return False
        if pion:
            if sprawdzRuchPionka(row_start, column_start, row_end, column_end, gracz):
                plansza[row_start][column_start] = EMPTY_FIELD
                plansza[row_end][column_end] = figure
            elif sprawdzBiciePionka(row_start, column_start, row_end, column_end, gracz):
                plansza[row_start][column_start] = EMPTY_FIELD
                ''' Odejmowanie punktow przeciwnikowi od piona i od pozycji piona'''
                if plansza[between_row_points][between_column_points] == WHITE_PAWN:
                    punktujBiale(-POINTS_PAWN)
                    punktujBiale(-punktyI(between_row_points,between_column_points, -gracz, gracz*graczK - 1))
                elif plansza[between_row_points][between_column_points] == BLACK_PAWN:
                    punktujCzarne(-POINTS_PAWN)
                    punktujCzarne(-punktyI(between_row_points,between_column_points, -gracz, gracz*graczK - 1))
                elif plansza[between_row_points][between_column_points] == WHITE_QUENN:
                    punktujBiale(-POINTS_QUENN)
                    punktujBiale(-punktyI(between_row_points,between_column_points, -gracz, gracz*graczK - 1))
                else:
                    punktujCzarne(-POINTS_QUENN)
                    punktujCzarne(-punktyI(between_row_points, between_column_points, -gracz, gracz * graczK - 1))
                plansza[between_row_points][between_column_points] = EMPTY_FIELD
                plansza[row_end][column_end] = figure
            else:
                print("Ruch niedozwolony")
                return False
        else:
            krotka = sprawdzRuchDamki(row_start, column_start, row_end, column_end, gracz)

            if krotka[3]:
                if krotka[0] == 1:
                    plansza[row_start][column_start] = EMPTY_FIELD
                    ''' Odejmowanie punktow przeciwnikowi od piona i od pozycji piona'''
                    if plansza[krotka[1]][krotka[2]] == WHITE_PAWN:
                        punktujBiale(-POINTS_PAWN)
                        punktujBiale(-punktyI(krotka[1], krotka[2], -gracz, gracz * graczK - 1))
                    elif plansza[krotka[1]][krotka[2]] == BLACK_PAWN:
                        punktujCzarne(-POINTS_PAWN)
                        punktujCzarne(-punktyI(krotka[1], krotka[2], -gracz, gracz * graczK - 1))
                    elif plansza[krotka[1]][krotka[2]] == WHITE_QUENN:
                        punktujBiale(-POINTS_QUENN)
                        punktujBiale(-punktyI(krotka[1], krotka[2], -gracz, gracz * graczK - 1))
                    else:
                        punktujCzarne(-POINTS_QUENN)
                        punktujCzarne(-punktyI(krotka[1], krotka[2], -gracz, gracz * graczK - 1))
                    plansza[krotka[1]][krotka[2]] = EMPTY_FIELD
                    plansza[row_end][column_end] = figure
                else:
                    plansza[row_start][column_start] = EMPTY_FIELD
                    plansza[row_end][column_end] = figure
            else:
                print(krotka[4])
                return False

        board.wyniesienie(row_end, column_end, gracz)
        punktyUpdate(row_start, column_start, row_end, column_end, gracz, graczK)
        return True
    else:
        print("niepoprawne dane")
        return False

def sprawdzRuchPionka(row_start, column_start, row_end, column_end, gracz):
        if ((row_start - row_end)*gracz == 1) and (abs(column_start - column_end) == 1) and plansza[row_end][column_end] == EMPTY_FIELD:
            return True # bialy:  ruch mozliwy o 1 jesli idzie na ukos o 1 i pole przed nim jest puste
        else:
            return False

def sprawdzBiciePionka(row_start, column_start, row_end, column_end, gracz):
    between_row_points = int((row_start + row_end) / 2)
    between_column_points = int((column_start + column_end) / 2)
    if abs(row_end - row_start) == 2 and abs(column_start - column_end) == 2:
        if plansza[row_end][column_end] == EMPTY_FIELD:
            if plansza[between_row_points][between_column_points] == figury[gracz]:
                return True  # ruch mozliwy gdy pionek bialy jest miedzy pionkiem czarnym a miejscem docelowym
            elif plansza[between_row_points][between_column_points] == figury[gracz-1]:
                return True  # ruch mozliwy gdy krolowa biala jest miedzy pionkiem czarnym a miejscem docelowym
            else:
                return False
        else:
            return False
    else:
        return False


def sprawdzRuchDamki(row_start, column_start, row_end, column_end, gracz):
    ''' Sprawdza ruch damki, zwraca liczbe pionków przeciwnika pomiedzy,
    pozycje x,y pionka przeciwnika oraz czy ruch mozliwy'''
    licznikPionow = 0
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

    if plansza[row_end][column_end] == EMPTY_FIELD and abs(row) == abs(column) and row != 0:
        x_pawn = 0
        y_pawn = 0
        for i in range(abs(column_end - column_start)):
            r_step = row_start + row_step
            c_step = column_start + column_step
            if plansza[r_step][c_step] == figury[gracz] or plansza[r_step][c_step] == figury[gracz-1]:
                licznikPionow += 1
                x_pawn = r_step
                y_pawn = c_step
            elif plansza[r_step][c_step] == figury[-gracz] or plansza[r_step][c_step] == figury[gracz+1]:
                return 0, 0, 0, False, "Nie mozesz skakac poprzez swoich"
            if row_step > 0:
                row_step += 1
            else:
                row_step -= 1
            if column_step > 0:
                column_step += 1
            else:
                column_step -= 1
        if licznikPionow < 2:
            return licznikPionow, x_pawn, y_pawn, True

    return 0, 0, 0, False, "Blad ruchu"