""" Main module. """
import pygame

import board
import design
import gra
import punktacja as pkt

def rozgrywka():
    """ Main function """

    pygame.init()
    _ = design.Look() #poradnik
    _ = gra.Gra()
    board.uklad_poczatkowy()
    board.wyswietl()
    pkt.punkty_start()
    pkt.wyswietl_punktacje()
    design.run_window()

rozgrywka()
#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate


#UWAGI
# pygame.kdasdas do maina wrzucic :!, stałe duzymi napisac
# nie musze robic klas
# rekurencyjne sprawdzanie skoku
# tekst w sposob inny
