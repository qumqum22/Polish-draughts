import pygame
from const import *

def runWindow():
    #rozpoczecie programu
    pygame.init()

    #stworzenie ekranu gry
    #size = pygame.display.get_window_size # nie dziala ;(

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    #nazwa gry
    pygame.display.set_caption("szachy stupolowe","szachy stupolowe")

    icon = pygame.image.load("assets/pawn_32px.png")
    pygame.display.set_icon(icon)

    running = True
    while running:
        screen.fill((255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()