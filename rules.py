""" Module with rules of game """
import chessboard
import const as con
import game
import score


def check_position(x_coord, y_coord):
    """ Checking if (x, y) coordinates are correct """
    if -1 < x_coord < con.SIZE:
        if -1 < y_coord < con.SIZE:
            return True
    return False


def select_available_moves(path_list, path_points):
    """ Selecting the longest available moves. """
    max_len = 0
    for path in path_list:
        if len(path) >= max_len:
            max_len = len(path)

    for i in range(len(path_list) - 1, -1, -1):
        if len(path_list[i]) < max_len:
            path_list.pop(i)
            path_points.pop(i)


def player_move(row_start, column_start, row_end, column_end):
    """ Moving a figure """
    move = (row_start, column_start, row_end, column_end)
    move_from = (row_start, column_start)

    select_available_moves(game.Game.path_list, game.Game.path_points)

    if not (check_position(row_start, column_start) and check_position(row_end, column_end)):
        return False

    if game.Game.attack_from:
        if check_position(row_start, column_start) and check_position(row_end, column_end):
            for path in game.Game.path_list:
                if path[1] == move_from and path[2] == (row_end, column_end):
                    break
            else:
                return False
            for path in game.Game.path_list:
                if not path[1] == move_from:
                    index = game.Game.path_list.index(path)
                    game.Game.path_list.remove(path)
                    game.Game.path_points.pop(index)
                else:
                    path.pop(0)


    if check_position(row_start, column_start) and check_position(row_end, column_end):
        return make_move(move)
    return False


def make_move(move):
    """ Makes a move. """
    row_start = move[0]
    column_start = move[1]
    if game.Game.player == con.PLAYER_ONE:
        if not game.Game.path_list:
            game.Game.white_score = 0
            return False

        if game.Game.board[row_start][column_start] == con.WHITE_PAWN:
            figure = con.WHITE_PAWN
            return service_pawn(move, figure, game.Game.path_list)

        if game.Game.board[row_start][column_start] == con.WHITE_QUEEN:
            figure = con.WHITE_QUEEN
            return service_queen(move, figure, game.Game.path_list)
    else:
        if not game.Game.path_list:
            game.Game.black_score = 0
            return False

        if game.Game.board[row_start][column_start] == con.BLACK_PAWN:
            figure = con.BLACK_PAWN
            return service_pawn(move, figure, game.Game.path_list)

        if game.Game.board[row_start][column_start] == con.BLACK_QUEEN:
            figure = con.BLACK_QUEEN
            return service_queen(move, figure, game.Game.path_list)


def check_if_pawn_hits(row_start, column_start, row_end, column_end):
    """ Check if hitting enemy figure is possible"""
    if not check_position(row_end, column_end):
        return False
    if abs(row_end - row_start) == 2 and abs(column_start - column_end) == 2:
        between_row = (row_start + row_end) // 2
        between_column = (column_start + column_end) // 2

        if game.Game.player == con.PLAYER_ONE:
            if game.Game.board[row_end][column_end] == con.EMPTY_FIELD:
                if game.Game.board[between_row][between_column] \
                        in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    return True
        else:
            if game.Game.board[row_end][column_end] == con.EMPTY_FIELD:
                if game.Game.board[between_row][between_column] \
                        in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    return True
    return False



def check_if_queen_hits(row_start, column_start, row_end, column_end):
    """ Checking possible queen's hits, returns: number of enemy pawns between start and end, coordinates
    of enemy figure , is_move_possible and information."""
    if not check_position(row_end, column_end):
        return 0, 0, 0, False, "Invalid destiny"

    row = row_end - row_start
    column = column_end - column_start

    if row > 0:
        row_step = 1
    else:
        row_step = -1

    if column > 0:
        column_step = 1
    else:
        column_step = -1

    ruch = (row_start, column_start, row_end, column_end)
    row_column = (row, column)
    return check_if_queen_moves(ruch, row_column, row_step, column_step)


def check_if_queen_moves(move, lane, row_step, column_step):
    """ Function checking move for queen. """
    figures_counter = 0
    if game.Game.board[move[2]][move[3]] == con.EMPTY_FIELD \
            and abs(lane[0]) == abs(lane[1]) and lane[0] != 0:
        x_pawn = 0
        y_pawn = 0
        for _ in range(abs(move[3] - move[1])):
            r_step = move[0] + row_step
            c_step = move[1] + column_step
            if game.Game.player == con.PLAYER_ONE:
                if game.Game.board[r_step][c_step] in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    figures_counter += 1
                    x_pawn = r_step
                    y_pawn = c_step
                elif game.Game.board[r_step][c_step] in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    return 0, 0, 0, False, "You cannot jumps through your figures"
            else:
                if game.Game.board[r_step][c_step] in [con.WHITE_PAWN, con.WHITE_QUEEN]:
                    figures_counter += 1
                    x_pawn = r_step
                    y_pawn = c_step
                elif game.Game.board[r_step][c_step] in [con.BLACK_PAWN, con.BLACK_QUEEN]:
                    return 0, 0, 0, False, "You cannot jumps through your figures"

            if row_step > 0:
                row_step += 1
            else:
                row_step -= 1
            if column_step > 0:
                column_step += 1
            else:
                column_step -= 1
        if figures_counter < 2:
            return figures_counter, x_pawn, y_pawn, True, "Correct move"

    return 0, 0, 0, False, "Blad ruchu"


def service_pawn(move, figure, path_list):
    """Pawn service. """
    row_start, column_start, row_end, column_end = move

    between_row = (row_start + row_end) // 2
    between_column = (column_start + column_end) // 2

    for path_element in path_list:
        if ((row_start, column_start), (row_end, column_end)) == (path_element[0], path_element[1]):

            game.Game.board[row_start][column_start] = con.EMPTY_FIELD
            if abs(row_end - row_start) == 2:
                score.points_for_pawn_hit(move)

            game.Game.board[between_row][between_column] = con.EMPTY_FIELD
            game.Game.board[row_end][column_end] = figure
            score.update_points(row_start, column_start, row_end, column_end)

            if len(path_element) > 2:
                game.Game.attack_from.clear()
                game.Game.attack_from.append(path_element[1])
                #print(game.Game.attack_from)
                return False
            chessboard.promotion(row_end, column_end)
            game.Game.attack_from.clear()
            return True
    print("Illegal move")
    return False


def service_queen(move, figure, path_list):
    """Queen service. """
    row_start, column_start, row_end, column_end = move

    for path_element in path_list:
        if ((row_start, column_start), (row_end, column_end)) == (path_element[0], path_element[1]):

            temp_list = check_if_queen_hits(row_start, column_start, row_end, column_end)

            if temp_list[0] == 1:  # Prawda/ fałsz     Bicie / zwykly ruch
                game.Game.board[row_start][column_start] = con.EMPTY_FIELD

                score.points_for_queen_hit(temp_list)

                game.Game.board[temp_list[1]][temp_list[2]] = con.EMPTY_FIELD
                game.Game.board[row_end][column_end] = figure

                if len(path_element) > 2:
                    game.Game.attack_from.clear()
                    game.Game.attack_from.append(path_element[1])
                    score.update_points(row_start, column_start, row_end, column_end)
                    print(game.Game.attack_from)
                    return False
            else:
                game.Game.board[row_start][column_start] = con.EMPTY_FIELD
                game.Game.board[row_end][column_end] = figure

            score.update_points(row_start, column_start, row_end, column_end)
            game.Game.attack_from.clear()
            return True
    return False
