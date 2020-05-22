""" Module of design. """
import pygame

import const as c
import gra as g
import board
import rules
import Button as button
import punktacja as pkt


# rozpoczecie programu
pygame.init()

# stworzenie ekranu gry
# size = pygame.display.get_window_size # nie dziala ;(

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT), pygame.RESIZABLE)

# nazwa gry
pygame.display.set_caption("szachy stupolowe", "szachy stupolowe")

# ikona gry
icon = pygame.image.load("assets/icon_32px.png")
pygame.display.set_icon(icon)


# plansza
plansza_img = pygame.image.load("assets/board.jpg")


# gracz
white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")
white_quenn_img = pygame.image.load("assets/white_quenn_32px.png")
black_quenn_img = pygame.image.load("assets/black_quenn_32px.png")

# Tekst ruchu
font = pygame.font.Font('freesansbold.ttf', 32)
textX = c.WIDTH / 2 - c.BOARD / 2
textY = c.HEIGHT / 2 - c.BOARD / 2 - c.FIELD

#Tworzenie przyciskow
restart_button = button.Button(c.LIME, c.PLANSZA_X+c.BOARD + c.BOARD/c.SIZE+2, c.PLANSZA_Y+2,
                               100, 50, "Restart")
test_bicie_button = button.Button(c.LIME, c.WIDTH/100, c.HEIGHT/100,
                                  150, 50, "Test bicia")
test_wyniesienie_button = button.Button(c.LIME, c.WIDTH/100, 2*c.HEIGHT/100+50,
                                        150, 50, "Test wyniesienia")
test_wygrana_button = button.Button(c.LIME, c.WIDTH/100, 3*c.HEIGHT/100+100,
                                    150, 50, "Test wygranej")

def show_move(msg, x_coord, y_coord):
    """ Rendering text at the game window. """
    text_message = font.render(msg, True, (255, 255, 255))
    screen.blit(text_message, (x_coord, y_coord))

def run_window():
    """Game window. """
    running = True

    while running:
        screen.fill(c.GRAY)

        # Obsluga zdarzen
        for event in pygame.event.get():
            #start_x, start_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False


            #KONTROLA MYSZY
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                #ZMIANA KOLOROW PRZYCISKOW
                if restart_button.is_over(pos[0], pos[1]):
                    restart_button.color = c.RED
                else:
                    restart_button.color = c.LIME

                if test_bicie_button.is_over(pos[0], pos[1]):
                    test_bicie_button.color = c.RED
                else:
                    test_bicie_button.color = c.LIME

                if test_wyniesienie_button.is_over(pos[0], pos[1]):
                    test_wyniesienie_button.color = c.RED
                else:
                    test_wyniesienie_button.color = c.LIME

                if test_wygrana_button.is_over(pos[0], pos[1]):
                    test_wygrana_button.color = c.RED
                else:
                    test_wygrana_button.color = c.LIME

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = pygame.mouse.get_pos()

                #PRZYCISK RESTARTU
                if restart_button.is_over(start_x, start_y):
                    board.uklad_czyszczenie()
                    board.uklad_poczatkowy()
                    board.wyswietl()
                    pkt.punkty_start()
                    g.gracz = 1
                    g.gracz_k = 0

                #PRZYCISKI TESTOW
                if test_bicie_button.is_over(start_x, start_y):
                    board.uklad_czyszczenie()
                    board.test_1()
                    board.wyswietl()
                    pkt.punkty_start()
                    g.gracz = 1
                    g.gracz_k = 0

                if test_wyniesienie_button.is_over(start_x, start_y):
                    board.uklad_czyszczenie()
                    board.test_2()
                    board.wyswietl()
                    pkt.punkty_start()
                    g.gracz = 1
                    g.gracz_k = 0

                if test_wygrana_button.is_over(start_x, start_y):
                    board.uklad_czyszczenie()
                    board.test_3()
                    board.wyswietl()
                    pkt.punkty_start()
                    g.gracz = 1
                    g.gracz_k = 0

                #ODCZYT POLOZENIA POCZATKOWEGO MYSZKI
                start_x = int((start_x - c.PLANSZA_X)/c.FIELD)
                start_y = int((start_y - c.PLANSZA_Y)/c.FIELD)

            #ODCZYT POLOZENIA KONCOWEGO MYSZKI
            if event.type == pygame.MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                end_x = int((end_x - c.PLANSZA_X) / c.FIELD)
                end_y = int((end_y - c.PLANSZA_Y) / c.FIELD)


                #OBSŁUGA RUCHÓW
                if g.gracz == 1:
                    print(start_x, start_y, end_x, end_y)
                    if not rules.ruch_gracza(start_y, start_x, end_y, end_x, g.gracz, g.gracz_k):
                        # or krotka[1] (bicie True/False)
                        g.gracz *= -1
                        g.gracz_k = -g.gracz_k - 1
                        board.wyswietl()
                else:
                    if not rules.ruch_gracza(start_y, start_x, end_y, end_x, g.gracz, g.gracz_k):
                        g.gracz *= -1
                        g.gracz_k = -g.gracz_k - 1
                        board.wyswietl()
                g.gracz *= -1
                g.gracz_k = -g.gracz_k - 1
                board.wyswietl()
                print(g.biale)
                print(g.czarne)

        #RYSOWANIE SZACHOWNICY
        screen.blit(plansza_img, (c.PLANSZA_X, c.PLANSZA_Y))

        for i in range(10):
            for j in range(10):
                if g.plansza[i][j] == c.WHITE_PAWN:
                    screen.blit(white_pawn_img, (c.PLANSZA_X + j*c.BOARD/c.SIZE,
                                                 c.PLANSZA_Y + i * c.BOARD/c.SIZE))
                elif g.plansza[i][j] == c.BLACK_PAWN:
                    screen.blit(black_pawn_img, (c.PLANSZA_X + j*c.BOARD/c.SIZE,
                                                 c.PLANSZA_Y + i * c.BOARD/c.SIZE))
                elif g.plansza[i][j] == c.WHITE_QUENN:
                    screen.blit(white_quenn_img, (c.PLANSZA_X + j*c.BOARD/c.SIZE,
                                                  c.PLANSZA_Y + i * c.BOARD/c.SIZE))
                elif g.plansza[i][j] == c.BLACK_QUENN:
                    screen.blit(black_quenn_img, (c.PLANSZA_X + j*c.BOARD/c.SIZE,
                                                  c.PLANSZA_Y + i * c.BOARD/c.SIZE))

        #INFORMACJA CZYJ RUCH / KTO WYGRAL
        if g.biale == 0:
            show_move("WYGRAŁY CZARNE", textX, textY)

        elif g.czarne == 0:
            show_move("WYGRAŁY BIAŁE", textX, textY)

        elif g.gracz == 1:
            show_move("Tura: białe", textX, textY)
        else:
            show_move("Tura: czarne", textX, textY)

        restart_button.draw(screen, (0, 0, 0))
        test_bicie_button.draw(screen, (0, 0, 0))
        test_wyniesienie_button.draw(screen, (0, 0, 0))
        test_wygrana_button.draw(screen, (0, 0, 0))
        pygame.display.update()     # pokazanie gotowego rysunku gry
