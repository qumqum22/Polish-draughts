"""Module with const values. """

SIZE = 10              #Wielkość planszy
WIDTH = 800             #Szerokość okna gry
HEIGHT = 600            #Wysokość okna gry
BOARD = 320             #Wielkosc planszy

BUTTON_PROP = (150, 50)

BOARD_X = WIDTH / 2 - BOARD / 2
BOARD_Y = HEIGHT / 2 - BOARD / 2
FIELD = BOARD/SIZE      #Wielkosc pola planszy
LINES_OF_PAWNS = 4      #Ilość linii wypełnionych pionkami jednego gracza
BLACK_PAWN = 'c'        #Oznaczenie czarnego pionka
WHITE_PAWN = 'b'        #Oznaczenie białego pionka
BLACK_QUEEN = 'C'       #Oznaczenie czarnej królowej
WHITE_QUEEN = 'B'       #Oznaczenie białej królowej
EMPTY_FIELD = ' '       #Oznaczenie pustego pola
POINTS_PAWN = 1
POINTS_QUEEN = 10
PLAYER_ONE = 1
PLAYER_TWO = 0

#Kolory
BUTTON_RED = (255, 0, 0)
BUTTON_LIME = (0, 255, 0)
BACKGROUND_COLOR = (128, 128, 128)

if LINES_OF_PAWNS > SIZE / 2:           #Automatyczna poprawka ilości linii wypełnionych pionkami
    LINES_OF_PAWNS = int(SIZE / 2) - 1  #Na wypadek przepelnienia linii pionków jednego gracza
