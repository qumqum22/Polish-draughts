from const import *
from board import *
import pygame, sys
from rules import ruchGracza
import time
def runWindow():
    #rozpoczecie programu
    pygame.init()

    #stworzenie ekranu gry
    #size = pygame.display.get_window_size # nie dziala ;(

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    #nazwa gry
    pygame.display.set_caption("szachy stupolowe","szachy stupolowe")

    #ikona gry
    icon = pygame.image.load("assets/icon_32px.png")
    pygame.display.set_icon(icon)

    #plansza
    plansza_img = pygame.image.load("assets/board.jpg")
    planszaX = WIDTH/2 - BOARD/2
    planszaY = HEIGHT/2 - BOARD/2
    #gracz
    white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
    black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")
    white_quenn_img = pygame.image.load("assets/white_quenn_32px.png")
    black_quenn_img = pygame.image.load("assets/black_quenn_32px.png")

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = pygame.mouse.get_pos()
                start_x = int((start_x - planszaX)/32)
                start_y = int((start_y - planszaY)/32)
                print(start_x, start_y)

            if event.type == pygame.MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                end_x = int((end_x - planszaX) / 32)
                end_y = int((end_y - planszaY) / 32)
                print(end_x, end_y)

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

        pygame.display.update() # pokazanie gotowego rysunku gry

