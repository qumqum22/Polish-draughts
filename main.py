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
    pkt.punktuj()
    pkt.punkty_start()
    pkt.wyswietl_punktacje()
    design.run_window()


if __name__ == '__main__':
    rozgrywka()





#funkcja ocen pozycje - liczy laczną pozycje gracza po ruchu pomocnicza do evaluate

#UWAGI
# rekurencyjne sprawdzanie skoku
