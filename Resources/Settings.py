import pygame

WIDTH = 500
HEIGHT = 700
FPS = 60
FONT_PATH = "freesansbold.ttf"
EMPTY = " "
pygame.init()
HUGE_FONT = pygame.font.Font('freesansbold.ttf', 56)

EMPTY_BOARD = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (64, 64, 64)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
GOLD = (255, 215, 0)
GREY = (100, 100, 100)
DARK_GREY = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 108, 108)

COLOR_INCORRECT = (50, 50, 50)
COLOR_MISPLACED = (255, 193, 53)
COLOR_CORRECT = (0, 185, 6)

TEXT_TIMER = 2
NUM_ROWS = 6
NUM_COLS = 5
LETTER_LENGTH = NUM_COLS
RECT_WIDTH = 50
RECT_HEIGHT = 50
# Pixels between each Rect
DX = 10
DY = 10
X_PADDING = 5
Y_PADDING = 5
BASE_OFFSET_X = (WIDTH / 2) - ((NUM_COLS / 2) * DX) - ((NUM_COLS / 2) * RECT_WIDTH) + (((NUM_COLS + 1) % 2) * (DX / 2))
BASE_OFFSET_Y = (HEIGHT / 2) - ((NUM_ROWS / 2) * DY) - ((NUM_ROWS / 2) * RECT_HEIGHT) + (
            ((NUM_ROWS + 1) % 2) * (DY / 2))
