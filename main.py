import time
#from const import *
from design import *
from board import *
from rules import *
from punktacja import *

def rozgrywka():
    global gracz
    global graczK
    ukladPoczatkowy()
    wyswietl()
    punktyStart()

    runWindow()
    while(1):
        #Petla nie uwzglednia bicia, wystarczy zwracac procz True, drugie True, informacja czy bylo bicie
        if gracz == 1:
            graczK = 0
            ruch, ruch2 = input('Biale: Wskaz pionka i cel: ').split()
            if ruch == 'z':
                break
            if not ruchGracza(ruch, ruch2, gracz, graczK): # or krotka[1] (bicie True/False)
                gracz *= -1
                graczK = -graczK - 1
        else:
            graczK = -1
            ruch, ruch2 = input('Czarne: Wskaz pionka i cel: ').split()
            if ruch == 'z':
                break
            if not ruchGracza(ruch, ruch2, gracz, graczK):
                gracz *= -1
                graczK = -graczK - 1

        gracz *= -1
        wyswietl()

    #wyswietlpunktacje() #wyswietla szachownice punktow

rozgrywka()

#spr. zasady gry stupolowych pod wzgl. maksymalnego bicia. Zrobic musowe bicie.
#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate
#Dodanie oceny ruchu królowej // krolowa wiecej punkt, pion mniej
#Dodanie sprawdzania ruchów królowej
#moge zrobic klase ze zmiennych globalnych
