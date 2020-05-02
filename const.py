SIZE = 10              #Wielkość planszy
WIDTH = 800             #Szerokość okna gry
HEIGHT = 600            #Wysokość okna gry
LINES_OF_PAWNS = 4      #Ilość linii wypełnionych pionkami jednego gracza
BLACK_PAWN = 'c'        #Oznaczenie czarnego pionka
WHITE_PAWN = 'b'        #Oznaczenie białego pionka
BLACK_QUENN = 'C'       #Oznaczenie czarnej królowej
WHITE_QUENN = 'B'       #Oznaczenie białej królowej
EMPTY_FIELD = ' '       #Oznaczenie pustego pola
POINTS_PAWN = 10
POINTS_QUENN = 100
if LINES_OF_PAWNS > SIZE / 2:           #Automatyczna poprawka ilości linii wypełnionych pionkami
    LINES_OF_PAWNS = int(SIZE / 2) - 1  #Na wypadek podania zbyt dużej liczby linii pionków jednego gracza

''' ZMIENNE '''
plansza = [[EMPTY_FIELD for column in range(SIZE)] for row in range(SIZE)]

gracz = 1  # 1 bialy || -1 czarny
figury = [BLACK_QUENN, BLACK_PAWN, WHITE_QUENN, WHITE_PAWN]
graczK = 0 # 0 bialy || -1 czarny

# wtedy funkcje beda moglby byc pasujace do obu dzieki wspolczynnikowi. Mniej ifów.