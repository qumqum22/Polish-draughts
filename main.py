""" Main module. """
import pygame

import chessboard
import design
import game
import score as pkt

def draughts():
    """ Main function """

    pygame.init()
    _ = design.Look() #poradnik
    _ = game.Game()
    chessboard.uklad_poczatkowy()
    chessboard.wyswietl()
    pkt.punktuj()
    pkt.points_load()
    #pkt.wyswietl_punktacje()
    design.run_window()


if __name__ == '__main__':
    draughts()
