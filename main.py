import time
#from const import *
from design import *
from board import *
from rules import *
from punktacja import *

def rozgrywka():
    #global gracz
    #global graczK

    ukladPoczatkowy()
    wyswietl()
    punktyStart()
    runWindow()


rozgrywka()

#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate
#moge zrobic klase ze zmiennych globalnych ( czy jest sens?)
