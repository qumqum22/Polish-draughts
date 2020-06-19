""" File with tests. """
import unittest

import chessboard
import const as con
import game
import moves
import rules
import score


def test_1():
    """ Preparing chessboard for multi-hit test. """
    game.Game.attack_from.clear()
    game.Game.board[5][4] = con.WHITE_PAWN
    game.Game.board[5][6] = con.WHITE_PAWN
    game.Game.board[7][6] = con.WHITE_PAWN

    game.Game.board[6][3] = con.BLACK_PAWN
    game.Game.board[2][1] = con.BLACK_PAWN
    game.Game.board[2][3] = con.BLACK_PAWN
    game.Game.board[4][3] = con.BLACK_PAWN
    game.Game.board[4][1] = con.BLACK_PAWN

def test_2():
    """ Preparing chessboard for promotion test. """
    game.Game.attack_from.clear()
    game.Game.board[1][2] = con.WHITE_PAWN
    game.Game.board[8][7] = con.BLACK_PAWN

def test_3():
    """ Preparing chessboard for win test. """
    game.Game.attack_from.clear()
    game.Game.board[5][6] = con.BLACK_QUEEN
    game.Game.board[6][5] = con.WHITE_PAWN


class BoardTest(unittest.TestCase):

    def multi_hit_test(self):
        """ Testing a multi hit by pawn. """
        game.Game.reload_variables()
        chessboard.clear_chessboard()
        test_1()
        score.points_load()
        moves.check_available_moves(game.Game.path_list, game.Game.path_points)
        rules.player_move(5, 4, 3, 2)
        rules.player_move(3, 2, 1, 0)
        for i in [2, 3, 4, 5]:
            if not game.Game.board[i][i - 1] == con.EMPTY_FIELD:
                break
        if game.Game.board[1][0] == con.WHITE_PAWN:
            print("Multi-hit test passed.")

    def promotion_test(self):
        """ Testing a promotion. """
        game.Game.reload_variables()
        chessboard.clear_chessboard()
        test_2()
        score.points_load()
        moves.check_available_moves(game.Game.path_list, game.Game.path_points)
        rules.player_move(1, 2, 0, 3)
        if game.Game.board[0][3] == con.WHITE_QUEEN and \
                game.Game.board[1][2] == con.EMPTY_FIELD:
            print("Promotion test passed.")

    def win_test(self):
        """ Testing a white player win. """
        game.Game.reload_variables()
        chessboard.clear_chessboard()
        test_3()
        score.points_load()
        moves.check_available_moves(game.Game.path_list, game.Game.path_points)
        rules.player_move(6, 5, 4, 7)
        if not game.Game.black_score:
            print("White wins test passed.")

    def reset_game(self):
        game.Game.reload_variables()
        chessboard.clear_chessboard()
        chessboard.set_game()
        score.points_load()

    def test_multi_hit(self):
        BoardTest.multi_hit_test(self)
        self.assertEqual(game.Game.board[2][1], con.EMPTY_FIELD)
        self.assertEqual(game.Game.board[3][2], con.EMPTY_FIELD)
        self.assertEqual(game.Game.board[4][3], con.EMPTY_FIELD)
        self.assertEqual(game.Game.board[5][4], con.EMPTY_FIELD)
        self.assertEqual(game.Game.board[1][0], con.WHITE_PAWN)
        BoardTest.reset_game(self)

    def test_promotion(self):
        BoardTest.promotion_test(self)
        self.assertEqual(game.Game.board[1][2], con.EMPTY_FIELD)
        BoardTest.reset_game(self)

    def test_win(self):
        BoardTest.win_test(self)
        self.assertEqual(game.Game.black_score, 0)
        BoardTest.reset_game(self)
