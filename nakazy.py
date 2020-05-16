from const import *
import board
import rules

quenn_mozliwe_ruchy_biale = []
quenn_mozliwe_ruchy_czarne = []

quenn_mozliwe_bicia_biale = []
quenn_mozliwe_bicia_czarne = []

def pawnMove(gracz):
    board.czytajFigury()

    pion_mozliwe_ruchy_biale = []
    pion_mozliwe_ruchy_czarne = []

    pion_mozliwe_ruchy_biale.clear()
    pion_mozliwe_ruchy_czarne.clear()

    if gracz == 1:
        for row_start, column_start in board.biale_piony:
            if rules.sprawdzPozycje(row_start-1, column_start+1):
                if plansza[row_start-1][column_start+1] == EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start, row_start - 1, column_start + 1))
            if rules.sprawdzPozycje(row_start - 1, column_start - 1):
                if plansza[row_start-1][column_start-1] == EMPTY_FIELD:
                    pion_mozliwe_ruchy_biale.append((row_start, column_start, row_start - 1, column_start - 1))
        return pion_mozliwe_ruchy_biale
    else:
        for row_start, column_start in board.czarne_piony:
            if rules.sprawdzPozycje(row_start + 1, column_start + 1):
                if plansza[row_start+1][column_start+1] == EMPTY_FIELD:
                    pion_mozliwe_ruchy_czarne.append((row_start, column_start, row_start + 1, column_start + 1))
            if rules.sprawdzPozycje(row_start + 1, column_start - 1):
                if plansza[row_start+1][column_start-1] == EMPTY_FIELD:
                    pion_mozliwe_ruchy_czarne.append((row_start, column_start, row_start + 1, column_start - 1))
        return pion_mozliwe_ruchy_czarne


def pawnHit(gracz):
    ''' Funkcja wykrywa mozliwe bicia'''
    board.czytajFigury()

    pion_mozliwe_bicia_biale = []
    pion_mozliwe_bicia_czarne = []

    pion_mozliwe_bicia_biale.clear()
    pion_mozliwe_bicia_czarne.clear()

    if gracz == 1:
        for pionek in board.biale_piony:
            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0]+2, pionek[1]+2, gracz):
                pion_mozliwe_bicia_biale.append((pionek[0], pionek[1], pionek[0] + 2, pionek[1] + 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] + 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia_biale.append((pionek[0], pionek[1], pionek[0] + 2, pionek[1] - 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] - 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia_biale.append((pionek[0], pionek[1], pionek[0] - 2, pionek[1] - 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] - 2, pionek[1] + 2, gracz):
                pion_mozliwe_bicia_biale.append((pionek[0], pionek[1], pionek[0] - 2, pionek[1] + 2))
        return pion_mozliwe_bicia_biale

    else:
        for pionek in board.czarne_piony:
            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] + 2, pionek[1] + 2, gracz):
                pion_mozliwe_bicia_czarne.append((pionek[0], pionek[1], pionek[0] + 2, pionek[1] + 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] + 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia_czarne.append((pionek[0], pionek[1], pionek[0] + 2, pionek[1] - 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] - 2, pionek[1] - 2, gracz):
                pion_mozliwe_bicia_czarne.append((pionek[0], pionek[1], pionek[0] - 2, pionek[1] - 2))

            if rules.sprawdzBiciePionka(pionek[0], pionek[1], pionek[0] - 2, pionek[1] + 2, gracz):
                pion_mozliwe_bicia_czarne.append((pionek[0], pionek[1], pionek[0] - 2, pionek[1] + 2))

        return pion_mozliwe_bicia_czarne


def quennMove(row_start, column_start, gracz):
    for i in range(-9, 10, 1):
        move_tuple = rules.sprawdzRuchDamki(row_start, column_start, row_start+i, column_start+i, gracz)
        if move_tuple[3]:
            if move_tuple[0]:
                quenn_mozliwe_bicia_biale.append((row_start, column_start, row_start+i, column_start+i))
            quenn_mozliwe_ruchy_biale.append((row_start, column_start, row_start+i, column_start+i))

        move_tuple = rules.sprawdzRuchDamki(row_start, column_start, row_start+i, column_start-i, gracz)
        if move_tuple[3]:
            if move_tuple[0]:
                quenn_mozliwe_bicia_biale.append((row_start, column_start, row_start + i, column_start + i))
            quenn_mozliwe_ruchy_biale.append((row_start, column_start, row_start + i, column_start + i))