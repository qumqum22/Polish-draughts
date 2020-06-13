""" Functions which are operating on game board."""
import const as con
import game


def wyswietl():
    """ Funkcja wyswietla aktualny stan gry. """
    for i in range(con.SIZE):
        print(i, "\t", game.Game.board[i])
        print('-------------------------------------------------------')

    print("\n\t   0    1    2    3    4    5    6    7    8    9 \n")


def uklad_czyszczenie():
    """ Czyszczenie planszy z figur. """
    for row in range(0, con.SIZE, 1):
        for column in range(0, con.SIZE, 1):
            game.Game.board[row][column] = con.EMPTY_FIELD


def uklad_poczatkowy():
    """ Funkcja inicjalizuje plansze pionkami """

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

    game.Game.board[6][1] = con.WHITE_QUEEN
    game.Game.board[7][2] = con.WHITE_QUEEN
    game.Game.board[3][8] = con.BLACK_QUEEN

def czytaj_figury():
    """ Tworzenie listy pionkow graczy. """
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

def wyniesienie(x_coord, y_coord):
    """ Zamiana piona na damke, gdy dojdzie do konca planszy. """
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
    """ Test wielokrotnego bicia. """
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
    """ Test wyniesienia. """
    game.Game.attack_from.clear()
    game.Game.board[1][2] = con.WHITE_PAWN
    game.Game.board[8][7] = con.BLACK_PAWN

def test_3():
    """ Test wygranej bialych. """
    game.Game.attack_from.clear()
    game.Game.board[5][6] = con.BLACK_QUEEN
    game.Game.board[6][5] = con.WHITE_PAWN
