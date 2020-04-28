from const import *
from temp import *
from punktacja import *
from board import wyniesienie
#Bicia są obowiązkowe. Kiedy istnieje kilka możliwych bić, gracz musi wykonać maksymalne
# (tzn. takie, w którym zbije największą liczbę pionów lub damek przeciwnika).
# Jeżeli gracz ma dwie lub więcej możliwości bicia takiej samej ilości bierek
# (pionków, damek lub pionków i damek) przeciwnika, to może wybrać jedną z nich.

#Podczas bicia nie można przeskakiwać więcej niż jeden raz przez tę samą bierkę.
# Bierki usuwa się z planszy po wykonaniu bicia.

def ruchGracza(od, do, gracz, graczK):
    row_start, column_start = translate(od)
    row_end, column_end = translate(do)
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
            plansza[row_start - 1][between_column_points] = EMPTY_FIELD
            plansza[row_end][column_end] = figure
        else:
            print("Ruch niedozwolony")
            return False
    else:
        pass


    wyniesienie(row_end, column_end, gracz)
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
            between_column_points = int((column_start + column_end) / 2)  # współrzędna kolumny pomiedzy skokiem
            if plansza[row_end][column_end] == EMPTY_FIELD:
                if plansza[row_start - 1][between_column_points] == BLACK_PAWN:
                    return True  # ruch mozliwy gdy pionek bialy jest miedzy pionkiem czarnym a miejscem docelowym
                elif plansza[row_start - 1][between_column_points] == BLACK_QUINN:
                    return True  # ruch mozliwy gdy krolowa biala jest miedzy pionkiem czarnym a miejscem docelowym
                else:
                    return False
            else:
                return False
        else:
            return False

# Czy dodawac jeszcze 1 zmienna graczK w ktorej jest 0 -dla bialych i -1 dla czarnych. Wtedy moge zrobić:
# Dodatkową tablice przechowywujacą rodzaje pionkow. figury =[WHITE_PAWN, WHITE_QUINN, BLACK_QUINN, BLACK_PAWN]