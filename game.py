"""Variables."""
import const

class Game:
    """ Class for global variables. """
    def __init__(self):
        """ Class initializes variables"""
        Game.board = [[const.EMPTY_FIELD for _ in range(const.SIZE)]
                      for _ in range(const.SIZE)]

        Game.white_pawns = []
        Game.white_queens = []
        Game.black_pawns = []
        Game.black_queens = []

        Game.path_list = []
        Game.path_points = []

        Game.attack_from = []
        Game.available_moves = []
        Game.player = const.PLAYER_ONE

        Game.white_score = 0
        Game.black_score = 0
        Game.score = [[0 for _ in range(const.SIZE)] for _ in range(const.SIZE)]

    @staticmethod
    def reload_variables():
        """ Function is clearing variables."""
        Game.white_pawns.clear()
        Game.white_queens.clear()
        Game.black_pawns.clear()
        Game.black_queens.clear()

        Game.path_list.clear()
        Game.path_points.clear()

        Game.attack_from.clear()
        Game.available_moves.clear()
        Game.player = const.PLAYER_ONE

        Game.white_score = 0
        Game.black_score = 0
