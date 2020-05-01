from const import *
from temp import *
from punktacja import *
from board import wyniesienie
#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.
# Implementacja jakiegoś drzewka(?)

#Podczas bicia nie można przeskakiwać więcej niż jeden raz przez tę samą bierkę.
# Bierki usuwa się z planszy po wykonaniu bicia.

def ruchGracza(od, do, gracz, graczK):
    row_start, column_start = translate(od)
    row_end, column_end = translate(do)
    between_row_points = int((row_start + row_end) / 2)
    between_column_points = int((column_start + column_end) / 2)
    if gracz == 1 and plansza[row_start][column_start] == WHITE_PAWN:
        figure = WHITE_PAWN
        pion = 1
    elif gracz == -1 and plansza[row_start][column_start] == BLACK_PAWN:
        figure = BLACK_PAWN
        pion = 1
    elif gracz == 1 and plansza[row_start][column_start] == WHITE_QUINN:
        figure = WHITE_QUINN
        pion = 0
    elif gracz == -1 and plansza[row_start][column_start] == BLACK_QUINN:
        figure = BLACK_QUINN
        pion = 0
    else:
        print("Ruch niedozwolony")
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
                punktujBiale(-punktyI(between_row_points,between_column_points, -gracz, gracz*graczK - 1))
            elif plansza[between_row_points][between_column_points] == WHITE_QUINN:
                punktujBiale(-POINTS_QUINN)
                punktujBiale(-punktyI(between_row_points,between_column_points, -gracz, gracz*graczK - 1))
            else:
                punktujCzarne(-POINTS_QUINN)
                punktujBiale(-punktyI(between_row_points, between_column_points, -gracz, gracz * graczK - 1))
            plansza[between_row_points][between_column_points] = EMPTY_FIELD
            plansza[row_end][column_end] = figure
        else:
            print("Ruch niedozwolony")
            return False
    else:
        krotka = sprawdzRuchDamki(row_start, column_start, row_end, column_end, gracz)
        if krotka[3]:
            if krotka[0]:
                plansza[row_start][column_start] = EMPTY_FIELD
                plansza[krotka[1]][krotka[2]] = EMPTY_FIELD
                plansza[row_end][column_end] = figure
            else:
                plansza[row_start][column_start] = EMPTY_FIELD
                plansza[row_end][column_end] = figure
        else:
            print(krotka[4])
            return False

    wyniesienie(row_end, column_end, gracz) # jak dodac punkty za wyniesienie
    punktyUpdate(od, do, gracz, graczK)

    return True

def sprawdzRuchPionka(row_start, column_start, row_end, column_end, gracz):
        if ((row_start - row_end)*gracz == 1) and (abs(column_start - column_end) == 1) and plansza[row_end][column_end] == EMPTY_FIELD:
            return True # bialy:  ruch mozliwy o 1 jesli idzie na ukos o 1 i pole przed nim jest puste
        else:
            return False

def sprawdzBiciePionka(row_start, column_start, row_end, column_end, gracz):
    if gracz == -1:
        if row_end - row_start == 2 and abs(column_start - column_end) == 2:
            between_column_points = int((column_start + column_end) / 2)  # współrzędna kolumny pomiedzy skokiem
            if plansza[row_end][column_end] == EMPTY_FIELD:
                if plansza[row_start + 1][between_column_points] == WHITE_PAWN:
                    return True  # ruch mozliwy gdy pionek bialy jest miedzy pionkiem czarnym a miejscem docelowym
                elif plansza[row_start + 1][between_column_points] == WHITE_QUINN:
                    return True  # ruch mozliwy gdy krolowa biala jest miedzy pionkiem czarnym a miejscem docelowym
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        if row_start - row_end == 2 and abs(column_start - column_end) == 2:
            between_column_points = int((column_start + column_end) / 2)
            if plansza[row_end][column_end] == EMPTY_FIELD:
                if plansza[row_start - 1][between_column_points] == BLACK_PAWN:
                    return True
                elif plansza[row_start - 1][between_column_points] == BLACK_QUINN:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def sprawdzRuchDamki(row_start, column_start, row_end, column_end, gracz):
    ''' Sprawdza ruch damki, zwraca liczbe pionków przeciwnika pomiedzy, pozycje x,y pionka przeciwnika oraz czy ruch mozliwy'''
    licznikPionow = 0
    row = row_end - row_start
    column = column_end - column_start
    #row_step
    #column_step
    if row > 0:
        row_step = 1
    else:
        row_step = -1

    if column > 0:
        column_step = 1
    else:
        column_step = -1

    if gracz == -1:
        if plansza[row_end][column_end] == EMPTY_FIELD and abs(row) == abs(column) and row != 0:
            x_pawn = 0
            y_pawn = 0
            for i in range(abs(column_end - column_start)):
                if plansza[row_start+row_step][column_start+column_step] == WHITE_PAWN:
                    licznikPionow += 1
                    x_pawn = row_start+row_step
                    y_pawn = column_start + column_step
                elif plansza[row_start+row_step][column_start+column_step] == WHITE_QUINN:
                    licznikPionow += 1
                    x_pawn = row_start+row_step
                    y_pawn = column_start + column_step
                elif plansza[row_start+row_step][column_start+column_step] == BLACK_PAWN or plansza[row_start+row_step][column_start+column_step] == BLACK_QUINN:
                    return 0, 0, 0, False, "Nie mozesz skakac poprzez swoich"
                if row_step*i > 0:
                    row_step += 1
                else:
                    row_step -= 1
                if column_step*1 > 0:
                    column_step += 1
                else:
                    column_step -= 1
            if licznikPionow < 2:
                return licznikPionow, x_pawn, y_pawn, True
    else:
        if plansza[row_end][column_end] == EMPTY_FIELD and abs(row) == abs(column) and row != 0:
            x_pawn = 0
            y_pawn = 0
            for i in range(abs(column_end - column_start)):
                if plansza[row_start+row_step][column_start+column_step] == BLACK_PAWN:
                    licznikPionow += 1
                    x_pawn = row_start + row_step
                    y_pawn = column_start + column_step
                elif plansza[row_start+row_step][column_start+column_step] == BLACK_QUINN:
                    licznikPionow += 1
                    x_pawn = row_start + row_step
                    y_pawn = column_start + column_step
                elif plansza[row_start+row_step][column_start+column_step] == WHITE_PAWN or plansza[row_start+row_step][column_start+column_step] == WHITE_QUINN:
                    return 0, 0, 0, False, "Nie mozesz skakac poprzez swoich"
                if row_step*i > 0:
                    row_step += 1
                else:
                    row_step -= 1
                if column_step*1 > 0:
                    column_step += 1
                else:
                    column_step -= 1
            if licznikPionow < 2:
                return licznikPionow, x_pawn, y_pawn, True
    return 0, 0, 0, False, "Blad ruchu"