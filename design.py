from const import *
from board import *
import pygame, sys
from rules import ruchGracza
import time
from Button import *
import punktacja as pkt
# rozpoczecie programu
pygame.init()

# stworzenie ekranu gry
# size = pygame.display.get_window_size # nie dziala ;(

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# nazwa gry
pygame.display.set_caption("szachy stupolowe", "szachy stupolowe")

# ikona gry
icon = pygame.image.load("assets/icon_32px.png")
pygame.display.set_icon(icon)

# plansza
plansza_img = pygame.image.load("assets/board.jpg")
planszaX = WIDTH / 2 - BOARD / 2
planszaY = HEIGHT / 2 - BOARD / 2

# gracz
white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")
white_quenn_img = pygame.image.load("assets/white_quenn_32px.png")
black_quenn_img = pygame.image.load("assets/black_quenn_32px.png")

# Tekst ruchu
font = pygame.font.Font('freesansbold.ttf', 32)
textX = WIDTH / 2 - BOARD / 2
textY = HEIGHT / 2 - BOARD / 2 - 32

restartButton = Button((0, 255, 0), planszaX + BOARD + BOARD / SIZE + 2, planszaY + 2, 100, 50, "Restart")
test_bicieButton = Button((255, 0, 0), WIDTH / 100, HEIGHT / 100, 150, 50, "Test bicia")
test_wyniesienieButton = Button((255, 0, 0), WIDTH / 100, 2 * HEIGHT / 100 + 50, 150, 50, "Test wyniesienia")
test_wygranaButton = Button((255, 0, 0), WIDTH / 100, 3 * HEIGHT / 100 + 100, 150, 50, "Test wygranej")

def show_move(msg, x, y):
    textMessage = font.render(msg, True, (255, 255, 255))
    screen.blit(textMessage, (x, y))

def runWindow():

    global gracz
    global graczK

    running = True

    while running:
        screen.fill((125, 125, 125))

        # Obsluga zdarzen
        for event in pygame.event.get():
            #start_x, start_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                #sys.exit(0)


            '''           KONTROLA MYSZY              '''
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                '''         ZMIANA KOLOROW PRZYCISKOW       '''
                if restartButton.isOver(pos[0], pos[1]):
                    restartButton.color = (255, 0, 0)
                else:
                    restartButton.color = (0, 255, 0)

                if test_bicieButton.isOver(pos[0], pos[1]):
                    test_bicieButton.color = (255, 0, 0)
                else:
                    test_bicieButton.color = (0, 255, 0)

                if test_wyniesienieButton.isOver(pos[0], pos[1]):
                    test_wyniesienieButton.color = (255, 0, 0)
                else:
                    test_wyniesienieButton.color = (0, 255, 0)

                if test_wygranaButton.isOver(pos[0], pos[1]):
                    test_wygranaButton.color = (255, 0, 0)
                else:
                    test_wygranaButton.color = (0, 255, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = pygame.mouse.get_pos()

                '''           PRZYCISK RESTARTU              '''
                if restartButton.isOver(start_x, start_y):
                    ukladCzyszczenie()
                    ukladPoczatkowy()
                    wyswietl()
                    punktyStart()
                    gracz = 1
                    graczK = 0

                '''             PRZYCISKI TESTOW             '''
                if test_bicieButton.isOver(start_x, start_y):
                    ukladCzyszczenie()
                    test_1()
                    wyswietl()
                    punktyStart()
                    gracz = 1
                    graczK = 0

                if test_wyniesienieButton.isOver(start_x, start_y):
                    ukladCzyszczenie()
                    test_2()
                    wyswietl()
                    punktyStart()
                    gracz = 1
                    graczK = 0

                if test_wygranaButton.isOver(start_x, start_y):
                    ukladCzyszczenie()
                    test_3()
                    wyswietl()
                    punktyStart()
                    gracz = 1
                    graczK = 0
                '''           ODCZYT POLOZENIA POCZATKOWEGO MYSZKI             '''
                start_x = int((start_x - planszaX)/32)
                start_y = int((start_y - planszaY)/32)

                '''           ODCZYT POLOZENIA KONCOWEGO MYSZKI             '''
            if event.type == pygame.MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                end_x = int((end_x - planszaX) / 32)
                end_y = int((end_y - planszaY) / 32)


                '''           OBSŁUGA RUCHÓW             '''
                if gracz == 1:
                    print(start_x, start_y, end_x, end_y)
                    if not ruchGracza(start_y, start_x, end_y, end_x, gracz, graczK):  # or krotka[1] (bicie True/False)
                        gracz *= -1
                        graczK = -graczK - 1
                        wyswietl()
                else:
                    if not ruchGracza(start_y, start_x, end_y, end_x, gracz, graczK):
                        gracz *= -1
                        graczK = -graczK - 1
                        wyswietl()
                gracz *= -1
                graczK = -graczK - 1
                wyswietl()
                print(pkt.biale)
                print(pkt.czarne)

        '''           RYSOWANIE SZACHOWNICY            '''
        screen.blit(plansza_img, (planszaX, planszaY))

        for i in range(10):
            for j in range(10):
                if plansza[i][j] == WHITE_PAWN:
                    screen.blit(white_pawn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))
                elif plansza[i][j] == BLACK_PAWN:
                    screen.blit(black_pawn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))
                elif plansza[i][j] == WHITE_QUENN:
                    screen.blit(white_quenn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))
                elif plansza[i][j] == BLACK_QUENN:
                    screen.blit(black_quenn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))

        '''           INFORMACJA CZYJ RUCH             '''
        if pkt.biale == 0:
            show_move("WYGRAŁY CZARNE", textX, textY)

        elif pkt.czarne == 0:
            show_move("WYGRAŁY BIAŁE", textX, textY)

        elif gracz == 1:
            show_move("Tura: białe", textX, textY)
        else:
            show_move("Tura: czarne", textX, textY)

        restartButton.draw(screen, (0, 0, 0))
        test_bicieButton.draw(screen, (0, 0, 0))
        test_wyniesienieButton.draw(screen, (0, 0, 0))
        test_wygranaButton.draw(screen, (0, 0, 0))
        pygame.display.update() # pokazanie gotowego rysunku gry

