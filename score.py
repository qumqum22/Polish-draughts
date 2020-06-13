""" Module with players points logicon. """
import const as con
import game


def punktuj():
    """ Initializing the board with points. """
    left_of_middle = con.SIZE/2-2
    right_of_middle = con.SIZE/2+1
    for x_coord in range(con.SIZE):
        for y_coord in range(con.SIZE):
            #PUNKTOWANIE ZA OKRAG
            if x_coord in (0, con.SIZE - 1) or y_coord in (0, con.SIZE - 1):
                game.Game.score[x_coord][y_coord] += 6
            elif (left_of_middle <= x_coord <= right_of_middle) and \
                    (left_of_middle <= y_coord <= right_of_middle):
                game.Game.score[x_coord][y_coord] += 2
            else:
                game.Game.score[x_coord][y_coord] += 4
            #PUNKTOWANIE ZA LINIE
            if x_coord < con.SIZE/5:
                game.Game.score[x_coord][y_coord] += 5
            elif x_coord < 2*con.SIZE/5:
                game.Game.score[x_coord][y_coord] += 4
            elif x_coord < 3*con.SIZE/5:
                game.Game.score[x_coord][y_coord] += 3
            elif x_coord < 4*con.SIZE/5:
                game.Game.score[x_coord][y_coord] += 2
            else:
                game.Game.score[x_coord][y_coord] += 1


def wyswietl_punktacje():
    """ Showing x_coord board of points. """
    for i in range(con.SIZE):
        print(i, "\t", game.Game.score[i])
    print()


def board_points_black(x_coord, y_coord):
    """ Returns points of position for player."""

    wynik = game.Game.score[-x_coord - 1][-y_coord]
    return wynik

def board_points_white(x_coord, y_coord):
    """ Returns points of position for player."""

    wynik = game.Game.score[x_coord][y_coord]
    return wynik

def points_load():
    """     Funkcja inicjalizuje punkty poczatkowe graczy   """
    game.Game.white_score = 0
    game.Game.black_score = 0
    for i in range(con.SIZE):
        for j in range(con.SIZE):
            if game.Game.board[i][j] == con.WHITE_PAWN:
                game.Game.white_score += con.POINTS_PAWN
                game.Game.white_score += board_points_white(i, j)
            elif game.Game.board[i][j] == con.WHITE_QUEEN:
                game.Game.white_score += con.POINTS_QUEEN
                game.Game.white_score += board_points_white(i, j)
            elif game.Game.board[i][j] == con.BLACK_PAWN:
                game.Game.black_score += con.POINTS_PAWN
                game.Game.black_score += board_points_black(i, j)
            elif game.Game.board[i][j] == con.BLACK_QUEEN:
                game.Game.black_score += con.POINTS_QUEEN
                game.Game.black_score += board_points_black(i, j)


def update_points(row_start, column_start, row_end, column_end):
    """ Funkcja uaktualnia sume punktow gracza co ruch"""

    if game.Game.player == con.PLAYER_ONE:
        new_coords = board_points_white(row_end, column_end)
        old_coords = board_points_white(row_start, column_start)
        game.Game.white_score += new_coords - old_coords
    else:
        new_coords = board_points_black(row_end, column_end)
        old_coords = board_points_black(row_start, column_start)
        game.Game.black_score += new_coords - old_coords


def cancel_update_points(row_start, column_start, row_end, column_end):
    """ Funkcja cofa uaktualnianie sumy punktow gracza co ruch"""

    if game.Game.player == con.PLAYER_ONE:
        new_coords = board_points_white(row_end, column_end)
        old_coords = board_points_white(row_start, column_start)
        game.Game.white_score += new_coords - old_coords
    else:
        new_coords = board_points_black(row_end, column_end)
        old_coords = board_points_black(row_start, column_start)
        game.Game.black_score += new_coords - old_coords

def points_for_pawn_hit(ruch):
    """ Function substracts points for deleting figure. """
    between_row = (ruch[0] + ruch[2]) // 2
    between_column = (ruch[1] + ruch[3]) // 2

    if game.Game.player == con.PLAYER_ONE:
        if game.Game.board[between_row][between_column] == con.BLACK_PAWN:
            game.Game.black_score += -con.POINTS_PAWN
            game.Game.black_score += -board_points_black(between_row, between_column)

        elif game.Game.board[between_row][between_column] == con.BLACK_QUEEN:
            game.Game.black_score += -con.POINTS_QUEEN
            game.Game.black_score += -board_points_black(between_row, between_column)
    else:
        if game.Game.board[between_row][between_column] == con.WHITE_PAWN:
            game.Game.white_score += -con.POINTS_PAWN
            game.Game.white_score += -board_points_white(between_row, between_column)

        elif game.Game.board[between_row][between_column] == con.WHITE_QUEEN:
            game.Game.white_score += -con.POINTS_QUEEN
            game.Game.white_score += -board_points_white(between_row, between_column)


def points_for_queen_hit(enemy_figure):
    """ Function substracts points for deleting figure. """
    if game.Game.player == con.PLAYER_ONE:
        if game.Game.board[enemy_figure[1]][enemy_figure[2]] == con.BLACK_PAWN:
            game.Game.black_score += -con.POINTS_PAWN
            game.Game.black_score += -board_points_black(enemy_figure[1], enemy_figure[2])
        elif game.Game.board[enemy_figure[1]][enemy_figure[2]] == con.BLACK_QUEEN:
            game.Game.black_score += -con.POINTS_QUEEN
            game.Game.black_score += -board_points_black(enemy_figure[1], enemy_figure[2])
    else:
        if game.Game.board[enemy_figure[1]][enemy_figure[2]] == con.WHITE_PAWN:
            game.Game.white_score += -con.POINTS_PAWN
            game.Game.white_score += -board_points_white(enemy_figure[1], enemy_figure[2])
        elif game.Game.board[enemy_figure[1]][enemy_figure[2]] == con.WHITE_QUEEN:
            game.Game.white_score += -con.POINTS_QUEEN
            game.Game.white_score += -board_points_white(enemy_figure[1], enemy_figure[2])
