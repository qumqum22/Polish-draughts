""" Module of design. """
import pygame

import chessboard
import computer
import button
import const as con
import game
import moves
import score
import rules


class Look:
    """ Class initializes Graphical interface"""
    def __init__(self):
        Look.screen = pygame.display.set_mode((con.WIDTH, con.HEIGHT), pygame.RESIZABLE)
        # nazwa gry
        pygame.display.set_caption("szachy stupolowe", "szachy stupolowe")
        # board
        Look.plansza_img = pygame.image.load("assets/board.jpg")
        # gracz
        Look.white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
        Look.black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")
        Look.white_queen_img = pygame.image.load("assets/white_queen_32px.png")
        Look.black_queen_img = pygame.image.load("assets/black_queen_32px.png")

        # Tekst ruchu
        Look.font = pygame.font.Font('freesansbold.ttf', 32)
        Look.textX = con.WIDTH / 2 - con.BOARD / 2
        Look.textY = con.HEIGHT / 2 - con.BOARD / 2 - con.FIELD

        #Tworzenie przyciskow
        Look.restart_button \
            = button.Button(con.BUTTON_LIME, (con.BOARD_X + con.BOARD + con.BOARD / con.SIZE + 2,
                                              con.BOARD_Y + 2), con.BUTTON_PROP, "Restart")
        Look.test_hit_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH/100, con.HEIGHT/100),
                            con.BUTTON_PROP, "Test bicia")
        Look.test_promo_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH / 100, 2 * con.HEIGHT / 100 + 50),
                            con.BUTTON_PROP, "Test wyniesienia")
        Look.test_win_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH/100, 3 * con.HEIGHT/100 + 100),
                            con.BUTTON_PROP, "Test wygranej")

        # ikona gry
        icon = pygame.image.load("assets/icon_32px.png")
        pygame.display.set_icon(icon)

    @staticmethod
    def show_move(msg, x_coord, y_coord):
        """ Rendering text at the game window. """
        text_message = Look.font.render(msg, True, (255, 255, 255))
        Look.screen.blit(text_message, (x_coord, y_coord))

    @staticmethod
    def changing_colours_for_buttons(mouse_pos):
        """ Changing colour of buttons. """
        if Look.restart_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.restart_button.color = con.BUTTON_RED
        else:
            Look.restart_button.color = con.BUTTON_LIME

        if Look.test_hit_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_hit_button.color = con.BUTTON_RED
        else:
            Look.test_hit_button.color = con.BUTTON_LIME

        if Look.test_promo_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_promo_button.color = con.BUTTON_RED
        else:
            Look.test_promo_button.color = con.BUTTON_LIME

        if Look.test_win_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_win_button.color = con.BUTTON_RED
        else:
            Look.test_win_button.color = con.BUTTON_LIME

    @staticmethod
    def service_of_tests(start_x, start_y):
        """ SERVICING TESTS. """
        # PRZYCISK RESTARTU
        if Look.restart_button.is_over(start_x, start_y):
            game.Game.reload_variables()
            chessboard.clear_chessboard()
            chessboard.set_game()
            chessboard.show_board()
            score.points_load()

        # PRZYCISKI TESTOW
        if Look.test_hit_button.is_over(start_x, start_y):
            game.Game.reload_variables()
            chessboard.clear_chessboard()
            chessboard.test_1()
            chessboard.show_board()
            score.points_load()


        if Look.test_promo_button.is_over(start_x, start_y):
            game.Game.reload_variables()
            chessboard.clear_chessboard()
            chessboard.test_2()
            chessboard.show_board()
            score.points_load()


        if Look.test_win_button.is_over(start_x, start_y):
            game.Game.reload_variables()
            chessboard.clear_chessboard()
            chessboard.test_3()
            chessboard.show_board()
            score.points_load()


def run_window():
    """Game window. """
    running = True

    while running:
        Look.screen.fill(con.BACKGROUND_COLOR)

        # Obsluga zdarzen
        for event in pygame.event.get():
            #start_x, start_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            #KONTROLA MYSZY
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                # ZMIANA KOLOROW PRZYCISKOW
                Look.changing_colours_for_buttons(pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = pygame.mouse.get_pos()
                #OBSLUGA PRZYCISKOW
                Look.service_of_tests(start_x, start_y)
                #ODCZYT POLOZENIA POCZATKOWEGO MYSZKI
                start_x = int((start_x - con.BOARD_X) / con.FIELD)
                start_y = int((start_y - con.BOARD_Y) / con.FIELD)

            #ODCZYT POLOZENIA KONCOWEGO MYSZKI
            if event.type == pygame.MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                end_x = int((end_x - con.BOARD_X) / con.FIELD)
                end_y = int((end_y - con.BOARD_Y) / con.FIELD)


                #OBSŁUGA RUCHÓW
                if game.Game.player == con.PLAYER_ONE:

                    if game.Game.attack_from:
                        if not rules.player_move(game.Game.attack_from[0][0],
                                                 game.Game.attack_from[0][1], end_y, end_x):
                            game.Game.player = con.PLAYER_ONE
                        else:
                            game.Game.player = con.PLAYER_TWO

                    else:
                        game.Game.attack_from.clear()
                        moves.check_available_moves(game.Game.path_list, game.Game.path_points)

                        if not rules.player_move(start_y, start_x, end_y, end_x):
                            game.Game.player = con.PLAYER_ONE
                        else:
                            game.Game.player = con.PLAYER_TWO
                else:
                    if game.Game.attack_from:
                        if not rules.player_move(game.Game.attack_from[0][0],
                                                 game.Game.attack_from[0][1], end_y, end_x):
                            game.Game.player = con.PLAYER_TWO
                        else:
                            game.Game.player = con.PLAYER_ONE
                    else:
                        game.Game.attack_from.clear()
                        moves.check_available_moves(game.Game.path_list, game.Game.path_points)

                        if not rules.player_move(start_y, start_x, end_y, end_x):
                            game.Game.player = con.PLAYER_TWO
                        else:
                            game.Game.player = con.PLAYER_ONE


        #RYSOWANIE SZACHOWNICY
        Look.screen.blit(Look.plansza_img, (con.BOARD_X, con.BOARD_Y))

        for i in range(10):
            for j in range(10):
                if game.Game.board[i][j] == con.WHITE_PAWN:
                    Look.screen.blit(Look.white_pawn_img, (con.BOARD_X + j * con.BOARD / con.SIZE,
                                                           con.BOARD_Y + i * con.BOARD / con.SIZE))
                elif game.Game.board[i][j] == con.BLACK_PAWN:
                    Look.screen.blit(Look.black_pawn_img, (con.BOARD_X + j * con.BOARD / con.SIZE,
                                                           con.BOARD_Y + i * con.BOARD / con.SIZE))
                elif game.Game.board[i][j] == con.WHITE_QUEEN:
                    Look.screen.blit(Look.white_queen_img, (con.BOARD_X + j * con.BOARD / con.SIZE,
                                                            con.BOARD_Y + i * con.BOARD / con.SIZE))
                elif game.Game.board[i][j] == con.BLACK_QUEEN:
                    Look.screen.blit(Look.black_queen_img, (con.BOARD_X + j * con.BOARD / con.SIZE,
                                                            con.BOARD_Y + i * con.BOARD / con.SIZE))

        # Text above a chessboard
        if game.Game.white_score == 0:
            Look.show_move("BLACK WON", Look.textX, Look.textY)

        elif game.Game.black_score == 0:
            Look.show_move("WHITE WON", Look.textX, Look.textY)

        elif game.Game.player == con.PLAYER_ONE:
            Look.show_move("Round: White", Look.textX, Look.textY)
        else:
            Look.show_move("Round: Black", Look.textX, Look.textY)

        Look.restart_button.draw(Look.screen, (0, 0, 0))
        Look.test_hit_button.draw(Look.screen, (0, 0, 0))
        Look.test_promo_button.draw(Look.screen, (0, 0, 0))
        Look.test_win_button.draw(Look.screen, (0, 0, 0))
        pygame.display.update()
