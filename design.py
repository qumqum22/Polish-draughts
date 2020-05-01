from const import *
from board import *
import pygame


def runWindow():
    #rozpoczecie programu
    pygame.init()

    #stworzenie ekranu gry
    #size = pygame.display.get_window_size # nie dziala ;(

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    #nazwa gry
    pygame.display.set_caption("szachy stupolowe","szachy stupolowe")

    #ikona gry
    icon = pygame.image.load("assets/pawn_32px.png")
    pygame.display.set_icon(icon)

    #plansza
    plansza_img = pygame.image.load("assets/board.jpg")
    planszaX = WIDTH/2 - 320/2
    planszaY = HEIGHT/2 - 320/2
    #gracz
    white_pawn_img = pygame.image.load("assets/white_pawn_32px.png")
    black_pawn_img = pygame.image.load("assets/black_pawn_32px.png")


    running = True
    while running:
        screen.fill((125, 125, 125))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(plansza_img, (planszaX, planszaY))
        for i in range(10):
            for j in range(10):
                if plansza[i][j] == WHITE_PAWN:
                    screen.blit(white_pawn_img,(planszaX + j*32, planszaY + i * 32))
                elif plansza[i][j] == BLACK_PAWN:
                    screen.blit(black_pawn_img,(planszaX + j*32, planszaY + i * 32))

        pygame.display.update()