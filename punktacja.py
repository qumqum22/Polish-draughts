from temp import *
from const import *

biale = 0
czarne = 0
punktacja = [[0 for column in range(SIZE)] for row in range(SIZE)]

def punktuj():
    srodek_l = SIZE/2-2
    srodek_p = SIZE/2+1
    for a in range(SIZE):
        for b in range(SIZE):
            ''' PUNKTOWANIE ZA OKRAG'''
            if (a == 0 or a == SIZE-1) or (b == 0 or b == SIZE-1):
                punktacja[a][b] += 60
            elif (srodek_l <= a <= srodek_p) and (srodek_l <= b <= srodek_p):
                punktacja[a][b] += 20
            else:
                punktacja[a][b] += 40
            ''' PUNKTOWANIE ZA LINIE'''
            if a < SIZE/5:
                punktacja[a][b] += 50
            elif a < 2*SIZE/5:
                punktacja[a][b] += 40
            elif a < 3*SIZE/5:
                punktacja[a][b] += 30
            elif a < 4*SIZE/5:
                punktacja[a][b] += 20
            else:
                punktacja[a][b] += 10

punktuj()

def wyswietlpunktacje():
    for i in range(SIZE):
        print(i, "\t", punktacja[i])
    print()

def punktujBiale(ile):
    global biale
    biale += ile


def punktujCzarne(ile):
    global czarne
    czarne += ile


def punkty(pozycja, gracz, graczK):
    x, y = translate(pozycja)
    wynik = punktacja[gracz*x+graczK][gracz*y+graczK] # dla bialego [x][y], # czarny [-x-1][y]
    return wynik

def punktyI(x, y, gracz, graczK):
    wynik = punktacja[gracz*x+graczK][y] # dla bialego [x][y], # czarny [-x-1][y]
    return wynik

def punktyStart():
    global biale
    global czarne
    for i in range(SIZE):
        for j in range(SIZE):
            if plansza[i][j] == WHITE_PAWN:
                biale += POINTS_PAWN
                biale += punktyI(i,j, 1, 0)
            elif plansza[i][j] == WHITE_QUINN:
                biale += POINTS_QUINN
                biale += punktyI(i,j, 1, 0)
            elif plansza[i][j] == BLACK_PAWN:
                czarne += POINTS_PAWN
                czarne += punktyI(i, j, -1, -1)
            elif plansza[i][j] == BLACK_QUINN:
                czarne += POINTS_QUINN
                czarne += punktyI(i, j, -1, -1)
    print(f'Punkty bialego: {biale}')
    print(f'Punkty czarnego: {czarne}')


def punktyUpdate(od, do, gracz, graczK):
    ''' Funkcja uaktualnia sume punktow gracza co ruch'''
    global biale
    global czarne
    if gracz == 1:
        biale = biale + punkty(do, gracz, graczK) - punkty(od, gracz, graczK)
        print(f'Wynik bialego:{biale}')
        print(f'Wynik czarnego:{czarne}')
    else:
        czarne = czarne + punkty(do, gracz, graczK) - punkty(od, gracz, graczK)
        print(f'Wynik bialego:{biale}')
        print(f'Wynik czarnego:{czarne}')
