""" Main module. """
import pygame

import chessboard
import design
import game
import score
import tests

def draughts():
    """ Main function """

    pygame.init()
    _ = design.Look()
    _ = game.Game()
    chessboard.set_game()
    chessboard.show_board()
    score.punktuj()
    score.points_load()
    #score.wyswietl_punktacje()
    tests.multi_hit_test()
    tests.promotion_test()
    tests.win_test()
    design.run_window()


if __name__ == '__main__':
    draughts()
