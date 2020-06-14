""" Functions responsible for checking available moves. """
import chessboard
import const as con
import game
import rules
import score


def check_available_moves(path_list, path_points):
    """ Making list of possible moves."""
    game.Game.available_moves.clear()
    game.Game.path_list.clear()
    game.Game.path_points.clear()
    chessboard.read_figures()

    pawn_multi_hit(path_list, path_points)
    queen_multi_hit(path_list, path_points)

    if not path_list:
        pawn_move(path_list)
        queen_move(path_list)


def pawn_move(path_list):
    """ Function is creating list of all possible player moves . """
    if game.Game.player == con.PLAYER_ONE:
        for row_start, column_start in game.Game.white_pawns:
            for d_column in [-1, 1]:
                path = []
                if rules.check_position(row_start - 1, column_start + d_column):
                    if game.Game.board[row_start - 1][column_start + d_column] == con.EMPTY_FIELD:
                        path.append((row_start, column_start))
                        path.append((row_start-1, column_start+d_column))
                        path_list.append(path)
                        score.update_points(row_start, column_start, row_start - 1,
                                          column_start + d_column)
                        game.Game.path_points.append(game.Game.white_score - game.Game.black_score)
                        score.cancel_update_points(row_start - 1, column_start + d_column,
                                                 row_start, column_start)
    else:
        for row_start, column_start in game.Game.black_pawns:
            for d_column in [-1, 1]:
                path = []
                if rules.check_position(row_start + 1, column_start + d_column):
                    if game.Game.board[row_start + 1][column_start + d_column] == con.EMPTY_FIELD:
                        path.append((row_start, column_start))
                        path.append((row_start + 1, column_start + d_column))
                        path_list.append(path)
                        score.update_points(row_start, column_start, row_start + 1,
                                          column_start + d_column)
                        game.Game.path_points.append(game.Game.white_score - game.Game.black_score)
                        score.cancel_update_points(row_start + 1, column_start + d_column,
                                                 row_start, column_start)



def pawn_multi_hit(path_list, path_points):
    """ Function returing the longest available hits. """
    if game.Game.player == con.PLAYER_ONE:
        for row_start, column_start in game.Game.white_pawns:
            path = [(row_start, column_start)]
            pawn_single_hit(path, path_list, path_points)
    else:
        for row_start, column_start in game.Game.black_pawns:
            path = [(row_start, column_start)]
            pawn_single_hit(path, path_list, path_points)


def pawn_single_hit(path, path_list, path_points):
    """ Making path of long hitting. """
    row_start, column_start = path[-1]
    for d_row in (-2, +2):
        for d_column in (-2, +2):
            new_row = row_start + d_row
            new_column = column_start + d_column

            if rules.check_if_pawn_hits(row_start, column_start, new_row, new_column):
                path_copy = path[:]
                path_copy.append((new_row, new_column))
                path_list.append(path_copy)
                move = (row_start, column_start, new_row, new_column)
                remember_figure, jumper = simulate_pawn_hit(move)   # executing a hit
                path_points.append(game.Game.white_score - game.Game.black_score)

                pawn_single_hit(path_copy, path_list, path_points)
                back_simulated_pawn_hit(move, remember_figure, jumper)  # back executed hit


def simulate_pawn_hit(move):
    """ Simulating a pawn hit. """
    row_start, column_start, row_end, column_end = move
    between_row_points = (row_start + row_end) // 2
    between_column_points = (column_start + column_end) // 2

    score.points_for_pawn_hit(move)
    score.update_points(row_start, column_start, row_end, column_end)

    remember_figure = game.Game.board[between_row_points][between_column_points]
    jumper = game.Game.board[row_start][column_start]

    game.Game.board[row_start][column_start] = con.EMPTY_FIELD
    game.Game.board[between_row_points][between_column_points] = con.EMPTY_FIELD
    game.Game.board[row_end][column_end] = jumper

    return remember_figure, jumper


def back_simulated_pawn_hit(move, remember_figure, jumper):
    """ Revoke changes done by simulate_pawn_hit. """
    row_start, column_start, row_end, column_end = move
    between_row = (row_start + row_end) // 2
    between_column = (column_start + column_end) // 2

    if game.Game.player == con.PLAYER_ONE:
        if remember_figure == con.BLACK_PAWN:
            game.Game.black_score += con.POINTS_PAWN
            game.Game.black_score += score.board_points_black(between_row, between_column)

        elif remember_figure == con.BLACK_QUEEN:
            game.Game.black_score += con.POINTS_QUEEN
            game.Game.black_score += score.board_points_black(between_row, between_column)
    else:
        if remember_figure == con.WHITE_PAWN:
            game.Game.white_score += con.POINTS_PAWN
            game.Game.white_score += score.board_points_white(between_row, between_column)

        elif remember_figure == con.WHITE_QUEEN:
            game.Game.white_score += con.POINTS_QUEEN
            game.Game.white_score += score.board_points_white(between_row, between_column)

    game.Game.board[row_end][column_end] = con.EMPTY_FIELD
    game.Game.board[between_row][between_column] = remember_figure
    game.Game.board[row_start][column_start] = jumper

    score.cancel_update_points(row_end, column_end, row_start, column_start)



def queen_move(path_list):
    """ Checking all available queen's moves. """
    chessboard.read_figures()

    if game.Game.player == con.PLAYER_ONE:
        for skad in game.Game.white_queens:
            for i in range(-9, 10, 1):
                move_tuple = rules.check_if_queen_hits(skad[0], skad[1],
                                                       skad[0] + i, skad[1] + i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] + i))
                    path_list.append(path)
                    score.update_points(skad[0], skad[1], skad[0] + i, skad[1] + i)
                    score_difference = game.Game.white_score - game.Game.black_score
                    game.Game.path_points.append(score_difference)
                    score.cancel_update_points(skad[0] + i, skad[1] + i, skad[0], skad[1])

                move_tuple = rules.check_if_queen_hits(skad[0], skad[1],
                                                       skad[0] + i, skad[1] - i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] - i))
                    path_list.append(path)
                    score.update_points(skad[0], skad[1], skad[0] + i, skad[1] - i)
                    score_difference = game.Game.white_score - game.Game.black_score
                    game.Game.path_points.append(score_difference)
                    score.cancel_update_points(skad[0] + i, skad[1] - i, skad[0], skad[1])

    else:
        for skad in game.Game.black_queens:
            for i in range(-9, 10, 1):
                move_tuple = rules.check_if_queen_hits(skad[0], skad[1],
                                                       skad[0] + i, skad[1] + i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] + i))
                    path_list.append(path)
                    score.update_points(skad[0], skad[1], skad[0] + i, skad[1] + i)
                    score_difference = game.Game.white_score - game.Game.black_score
                    game.Game.path_points.append(score_difference)
                    score.cancel_update_points(skad[0] + i, skad[1] + i, skad[0], skad[1])

                move_tuple = rules.check_if_queen_hits(skad[0], skad[1],
                                                       skad[0] + i, skad[1] - i)
                path = []
                if move_tuple[3] and not move_tuple[0]:
                    path.append((skad[0], skad[1]))
                    path.append((skad[0] + i, skad[1] - i))
                    path_list.append(path)
                    score.update_points(skad[0], skad[1], skad[0] + i, skad[1] - i)
                    score_difference = game.Game.white_score - game.Game.black_score
                    game.Game.path_points.append(score_difference)
                    score.cancel_update_points(skad[0] + i, skad[1] - i, skad[0], skad[1])



def queen_multi_hit(path_list, path_points):
    """ Function returning the longest available hits. """
    if game.Game.player == con.PLAYER_ONE:
        for row_start, column_start in game.Game.white_queens:
            path = [(row_start, column_start)]
            queen_single_hit(path, path_list, path_points)
    else:
        for row_start, column_start in game.Game.black_queens:
            path = [(row_start, column_start)]
            queen_single_hit(path, path_list, path_points)


def queen_single_hit(path, path_list, path_points):
    """ Making path of queen hitting. """
    row_start, column_start = path[-1]
    for i_row in range(-9, 10, 1):
        for i_column in range(-9, 10, 1):
            new_row = row_start + i_row
            new_column = column_start + i_column
            move_queen = rules.check_if_queen_hits(row_start, column_start, new_row, new_column)
            if move_queen[3]:
                if move_queen[0]:
                    path_copy = path[:]
                    path_copy.append((new_row, new_column))
                    path_list.append(path_copy)
                    move = (row_start, column_start, new_row, new_column)
                    enemy_pawn = (move_queen[1], move_queen[2])
                    remember_figure, jumper = simulate_queen_hit(move, enemy_pawn)
                    path_points.append(game.Game.white_score - game.Game.black_score)
                    queen_single_hit(path_copy, path_list, path_points)
                    back_simulated_queen_hit(move, enemy_pawn, remember_figure, jumper)


def simulate_queen_hit(move, hit):
    """ Moving a pawns during creating available moves. """
    row_start, column_start, row_end, column_end = move
    row_enemy, column_enemy = hit

    remember_figure = game.Game.board[row_enemy][column_enemy]
    jumper = game.Game.board[row_start][column_start]

    score.points_for_queen_hit((0, row_enemy, column_enemy))
    score.update_points(row_start, column_start, row_end, column_end)

    game.Game.board[row_start][column_start] = con.EMPTY_FIELD
    game.Game.board[row_enemy][column_enemy] = con.EMPTY_FIELD
    game.Game.board[row_end][column_end] = jumper
    return remember_figure, jumper


def back_simulated_queen_hit(move, enemy_pawn, remember_figure, jumper):
    """ Moving a pawns back during creating available moves. """
    row_start, column_start, row_end, column_end = move
    row_enemy, column_enemy = enemy_pawn

    if game.Game.player == con.PLAYER_ONE:
        if remember_figure == con.BLACK_PAWN:
            game.Game.black_score += con.POINTS_PAWN
            game.Game.black_score += score.board_points_black(row_enemy, column_enemy)
        elif remember_figure == con.BLACK_QUEEN:
            game.Game.black_score += con.POINTS_QUEEN
            game.Game.black_score += score.board_points_black(row_enemy, column_enemy)
    else:
        if remember_figure == con.WHITE_PAWN:
            game.Game.white_score += con.POINTS_PAWN
            game.Game.white_score += score.board_points_white(row_enemy, column_enemy)
        elif remember_figure == con.WHITE_QUEEN:
            game.Game.white_score += con.POINTS_QUEEN
            game.Game.white_score += score.board_points_white(row_enemy, column_enemy)

    game.Game.board[row_start][column_start] = jumper
    game.Game.board[row_enemy][column_enemy] = remember_figure
    game.Game.board[row_end][column_end] = con.EMPTY_FIELD
    score.cancel_update_points(row_end, column_end, row_start, column_start)
