""" Functions which are operating on game board."""
import const as con
import game


def show_board():
    """ Function displays actual game state in console. """
    for i in range(con.SIZE):
        print(i, "\t", game.Game.board[i])
        print('-------------------------------------------------------')

    print("\n\t   0    1    2    3    4    5    6    7    8    9 \n")


def clear_chessboard():
    """ Clearing chessboard. """
    for row in range(0, con.SIZE, 1):
        for column in range(0, con.SIZE, 1):
            game.Game.board[row][column] = con.EMPTY_FIELD


def set_game():
    """ Initialization chessboard by figures. """

    for row in range(0, con.LINES_OF_PAWNS, 1):
        if row % 2:
            for column in range(0, con.SIZE, 2):
                game.Game.board[row][column] = con.BLACK_PAWN
        else:
            for column in range(1, con.SIZE, 2):
                game.Game.board[row][column] = con.BLACK_PAWN

    for row in range(con.SIZE - con.LINES_OF_PAWNS, con.SIZE, 1):
        if row % 2:
            for column in range(0, con.SIZE, 2):
                game.Game.board[row][column] = con.WHITE_PAWN
        else:
            for column in range(1, con.SIZE, 2):
                game.Game.board[row][column] = con.WHITE_PAWN


def read_figures():
    """ Creating a list of players figures. """
    game.Game.white_pawns.clear()
    game.Game.white_queens.clear()

    game.Game.black_pawns.clear()
    game.Game.black_queens.clear()
    for row in range(con.SIZE):
        for column in range(con.SIZE):
            if game.Game.board[row][column] == con.WHITE_PAWN:
                game.Game.white_pawns.append((row, column))
            elif game.Game.board[row][column] == con.WHITE_QUEEN:
                game.Game.white_queens.append((row, column))
            elif game.Game.board[row][column] == con.BLACK_PAWN:
                game.Game.black_pawns.append((row, column))
            elif game.Game.board[row][column] == con.BLACK_QUEEN:
                game.Game.black_queens.append((row, column))


def promotion(x_coord, y_coord):
    """ Making a promotion. Pawn becomes a queen. """
    if game.Game.player == con.PLAYER_ONE:
        if x_coord == 0 and game.Game.board[0][y_coord] == con.WHITE_PAWN:
            game.Game.board[0][y_coord] = con.WHITE_QUEEN
            game.Game.white_score += con.POINTS_QUEEN - con.POINTS_PAWN
            return True
    else:
        if x_coord == 9 and game.Game.board[9][y_coord] == con.BLACK_PAWN:
            game.Game.board[9][y_coord] = con.BLACK_QUEEN
            game.Game.black_score += con.POINTS_QUEEN - con.POINTS_PAWN
            return True
    return False


def test_1():
    """ Preparing chessboard for multi-hit test. """
    game.Game.attack_from.clear()
    game.Game.board[6][3] = con.BLACK_PAWN
    game.Game.board[5][4] = con.WHITE_PAWN
    game.Game.board[5][6] = con.WHITE_PAWN
    game.Game.board[7][6] = con.WHITE_PAWN


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
