from const import *
from board import *
import pygame, sys

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


    running = True
    while running:
        screen.fill((125, 125, 125))

        # Obsluga zdarzen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                mx -= planszaX
                my -= planszaY
                print(int(mx/32), int(my/32))

        screen.blit(plansza_img, (planszaX, planszaY))

        for i in range(10):
            for j in range(10):
                if plansza[i][j] == WHITE_PAWN:
                    screen.blit(white_pawn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))
                elif plansza[i][j] == BLACK_PAWN:
                    screen.blit(black_pawn_img, (planszaX + j*BOARD/SIZE, planszaY + i * BOARD/SIZE))

        pygame.display.update() # pokazanie gotowego rysunku gry

