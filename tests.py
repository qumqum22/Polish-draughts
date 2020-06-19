""" File with tests. """
import chessboard
import const as con
import game
import moves
import rules
import score


def multi_hit_test():
    """ Testing a multi hit by pawn. """
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.test_1()
    score.points_load()
    moves.check_available_moves(game.Game.path_list, game.Game.path_points)
    rules.player_move(5, 4, 3, 2)
    rules.player_move(3, 2, 1, 0)
    for i in [2, 3, 4, 5]:
        if not game.Game.board[i][i - 1] == con.EMPTY_FIELD:
            print("Test failed.")
            break
    if game.Game.board[1][0] == con.WHITE_PAWN:
        print("Multi-hit test passed.")
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.set_game()
    score.points_load()


def promotion_test():
    """ Testing a promotion. """
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.test_2()
    score.points_load()
    moves.check_available_moves(game.Game.path_list, game.Game.path_points)
    rules.player_move(1, 2, 0, 3)
    if game.Game.board[0][3] == con.WHITE_QUEEN and \
            game.Game.board[1][2] == con.EMPTY_FIELD:
        print("Promotion test passed.")
    else:
        print("Test failed.")
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.set_game()
    score.points_load()


def win_test():
    """ Testing a white player win. """
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.test_3()
    score.points_load()
    moves.check_available_moves(game.Game.path_list, game.Game.path_points)
    rules.player_move(6, 5, 4, 7)
    if not game.Game.black_score:
        print("White wins test passed.")
    else:
        print("Test failed")
    game.Game.reload_variables()
    chessboard.clear_chessboard()
    chessboard.set_game()
    score.points_load()
