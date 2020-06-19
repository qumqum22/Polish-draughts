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
    test = tests.BoardTest()
    chessboard.set_game()
    chessboard.show_board()
    score.punktuj()
    score.points_load()
    #score.wyswietl_punktacje()
    test.multi_hit_test()
    test.promotion_test()
    test.test_win()
    design.run_window()


if __name__ == '__main__':
    draughts()
