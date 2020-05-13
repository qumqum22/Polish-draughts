
#from design import *

from board import *
from punktacja import *
import design

def rozgrywka():
    #global gracz
    #global graczK

    ukladPoczatkowy()
    wyswietl()
    punktyStart()
    design.runWindow()


rozgrywka()

#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate
#moge zrobic klase ze zmiennych globalnych ( czy jest sens?)
