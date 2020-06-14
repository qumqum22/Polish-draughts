"""File with global constants. """

SIZE = 10               #Number of rows and columns in chessboard
WIDTH = 800             #Width of the game window
HEIGHT = 600            #Height of the game window
BOARD = 320             #Size of a chessboard

BUTTON_PROP = (150, 50)

BOARD_X = WIDTH / 2 - BOARD / 2
BOARD_Y = HEIGHT / 2 - BOARD / 2
FIELD = BOARD/SIZE      #Size of single field
LINES_OF_PAWNS = 4
BLACK_PAWN = 'c'
WHITE_PAWN = 'b'
BLACK_QUEEN = 'C'
WHITE_QUEEN = 'B'
EMPTY_FIELD = ' '
POINTS_PAWN = 1
POINTS_QUEEN = 10
PLAYER_ONE = 1
PLAYER_TWO = 0

#Colours
BUTTON_RED = (255, 0, 0)
BUTTON_LIME = (0, 255, 0)
BACKGROUND_COLOR = (128, 128, 128)

if LINES_OF_PAWNS > SIZE / 2:
    LINES_OF_PAWNS = int(SIZE / 2) - 1
