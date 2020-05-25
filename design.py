""" Module of design. """
import pygame

import const as con
import gra
import board
import rules
import button
import punktacja as pkt

class Look:
    """ Class initializes Graphical interface"""
    def __init__(self):
        Look.screen = pygame.display.set_mode((con.WIDTH, con.HEIGHT), pygame.RESIZABLE)
        # nazwa gry
        pygame.display.set_caption("szachy stupolowe", "szachy stupolowe")
        # plansza
        Look.plansza_img = pygame.image.load("assets/board.jpg")
        # gracz
        Look.white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
        Look.black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")
        Look.white_quenn_img = pygame.image.load("assets/white_quenn_32px.png")
        Look.black_quenn_img = pygame.image.load("assets/black_quenn_32px.png")

        # Tekst ruchu
        Look.font = pygame.font.Font('freesansbold.ttf', 32)
        Look.textX = con.WIDTH / 2 - con.BOARD / 2
        Look.textY = con.HEIGHT / 2 - con.BOARD / 2 - con.FIELD

        #Tworzenie przyciskow
        Look.restart_button \
            = button.Button(con.BUTTON_LIME, (con.PLANSZA_X+con.BOARD + con.BOARD/con.SIZE+2,
                                                            con.PLANSZA_Y+2), (100, 50), "Restart")
        Look.test_bicie_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH/100, con.HEIGHT/100),
                                               (150, 50), "Test bicia")
        Look.test_promo_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH / 100, 2 * con.HEIGHT / 100 +
                                                               50), (150, 50), "Test wyniesienia")
        Look.test_wygrana_button \
            = button.Button(con.BUTTON_LIME, (con.WIDTH/100, 3*con.HEIGHT/100+100),
                                                 (150, 50), "Test wygranej")
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

        if Look.test_bicie_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_bicie_button.color = con.BUTTON_RED
        else:
            Look.test_bicie_button.color = con.BUTTON_LIME

        if Look.test_promo_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_promo_button.color = con.BUTTON_RED
        else:
            Look.test_promo_button.color = con.BUTTON_LIME

        if Look.test_wygrana_button.is_over(mouse_pos[0], mouse_pos[1]):
            Look.test_wygrana_button.color = con.BUTTON_RED
        else:
            Look.test_wygrana_button.color = con.BUTTON_LIME

    @staticmethod
    def service_of_tests(start_x, start_y):
        """ SERVICING TESTS. """
        # PRZYCISK RESTARTU
        if Look.restart_button.is_over(start_x, start_y):
            board.uklad_czyszczenie()
            board.uklad_poczatkowy()
            board.wyswietl()
            pkt.punkty_start()
            gra.Gra.gracz = 1
            gra.Gra.gracz_k = 0

        # PRZYCISKI TESTOW
        if Look.test_bicie_button.is_over(start_x, start_y):
            board.uklad_czyszczenie()
            board.test_1()
            board.wyswietl()
            pkt.punkty_start()
            gra.Gra.gracz = 1
            gra.Gra.gracz_k = 0

        if Look.test_promo_button.is_over(start_x, start_y):
            board.uklad_czyszczenie()
            board.test_2()
            board.wyswietl()
            pkt.punkty_start()
            gra.Gra.gracz = 1
            gra.Gra.gracz_k = 0

        if Look.test_wygrana_button.is_over(start_x, start_y):
            board.uklad_czyszczenie()
            board.test_3()
            board.wyswietl()
            pkt.punkty_start()
            gra.Gra.gracz = 1
            gra.Gra.gracz_k = 0




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
                start_x = int((start_x - con.PLANSZA_X)/con.FIELD)
                start_y = int((start_y - con.PLANSZA_Y)/con.FIELD)

            #ODCZYT POLOZENIA KONCOWEGO MYSZKI
            if event.type == pygame.MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                end_x = int((end_x - con.PLANSZA_X) / con.FIELD)
                end_y = int((end_y - con.PLANSZA_Y) / con.FIELD)

                #OBSŁUGA RUCHÓW
                if gra.Gra.gracz == 1:
                    print(start_x, start_y, end_x, end_y)
                    if gra.Gra.attack_from:
                        if not rules.ruch_gracza(gra.Gra.attack_from[0], gra.Gra.attack_from[1],
                                                 end_y, end_x, gra.Gra.gracz, gra.Gra.gracz_k):
                            gra.Gra.gracz *= -1
                            gra.Gra.gracz_k = -gra.Gra.gracz_k - 1
                            board.wyswietl()

                    else:
                        if not rules.ruch_gracza(start_y, start_x, end_y, end_x,
                                                 gra.Gra.gracz, gra.Gra.gracz_k):
                            # or krotka[1] (bicie True/False)
                            gra.Gra.gracz *= -1
                            gra.Gra.gracz_k = -gra.Gra.gracz_k - 1
                            board.wyswietl()
                else:
                    if gra.Gra.attack_from:
                        if not rules.ruch_gracza(gra.Gra.attack_from[0], gra.Gra.attack_from[1],
                                                 end_y, end_x, gra.Gra.gracz, gra.Gra.gracz_k):
                            gra.Gra.gracz *= -1
                            gra.Gra.gracz_k = -gra.Gra.gracz_k - 1
                            board.wyswietl()

                    else:
                        if not rules.ruch_gracza(start_y, start_x, end_y, end_x,
                                                 gra.Gra.gracz, gra.Gra.gracz_k):
                            # or krotka[1] (bicie True/False)
                            gra.Gra.gracz *= -1
                            gra.Gra.gracz_k = -gra.Gra.gracz_k - 1
                            board.wyswietl()
                gra.Gra.gracz *= -1
                gra.Gra.gracz_k = -gra.Gra.gracz_k - 1
                board.wyswietl()
                print(gra.Gra.biale)
                print(gra.Gra.czarne)

        #RYSOWANIE SZACHOWNICY
        Look.screen.blit(Look.plansza_img, (con.PLANSZA_X, con.PLANSZA_Y))

        for i in range(10):
            for j in range(10):
                if gra.Gra.plansza[i][j] == con.WHITE_PAWN:
                    Look.screen.blit(Look.white_pawn_img, (con.PLANSZA_X + j*con.BOARD/con.SIZE,
                                                           con.PLANSZA_Y + i * con.BOARD/con.SIZE))
                elif gra.Gra.plansza[i][j] == con.BLACK_PAWN:
                    Look.screen.blit(Look.black_pawn_img, (con.PLANSZA_X + j*con.BOARD/con.SIZE,
                                                           con.PLANSZA_Y + i * con.BOARD/con.SIZE))
                elif gra.Gra.plansza[i][j] == con.WHITE_QUENN:
                    Look.screen.blit(Look.white_quenn_img, (con.PLANSZA_X + j*con.BOARD/con.SIZE,
                                                            con.PLANSZA_Y + i * con.BOARD/con.SIZE))
                elif gra.Gra.plansza[i][j] == con.BLACK_QUENN:
                    Look.screen.blit(Look.black_quenn_img, (con.PLANSZA_X + j*con.BOARD/con.SIZE,
                                                            con.PLANSZA_Y + i * con.BOARD/con.SIZE))

        #INFORMACJA CZYJ RUCH / KTO WYGRAL
        if gra.Gra.biale == 0:
            Look.show_move("WYGRAŁY CZARNE", Look.textX, Look.textY)

        elif gra.Gra.czarne == 0:
            Look.show_move("WYGRAŁY BIAŁE", Look.textX, Look.textY)

        elif gra.Gra.gracz == 1:
            Look.show_move("Tura: białe", Look.textX, Look.textY)
        else:
            Look.show_move("Tura: czarne", Look.textX, Look.textY)

        Look.restart_button.draw(Look.screen, (0, 0, 0))
        Look.test_bicie_button.draw(Look.screen, (0, 0, 0))
        Look.test_promo_button.draw(Look.screen, (0, 0, 0))
        Look.test_wygrana_button.draw(Look.screen, (0, 0, 0))
        pygame.display.update()     # pokazanie gotowego rysunku gry
