import pygame
import os
pygame.init()
class Setup():
    WIDTH = 633 + 110  # 750 - x - 110
    HEIGHT = 900 + 80  # 980  - y -  80
    FPS = 60
    ICON = None
    ALPHABETS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    fonts = pygame.font.get_fonts()
    GUESSED_LETTER_FONT = pygame.font.SysFont(fonts[47], 50)
    AVAILABLE_LETTER_FONT = pygame.font.SysFont(fonts[47], 25)
    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 12
    LETTER_SIZE = 75
    OUTLINE = "#d3d6da"
    FILLED_OUTLINE = "#878a8c"
    CORRECT_WORD = "coder"
    print(CORRECT_WORD)
    BACKGROUND_PATH = os.path.join(os.path.dirname(__file__), "Starting Tiles.png")
    BACKGROUND = pygame.image.load(BACKGROUND_PATH)
    PLAY_AGAIN_FONT = pygame.font.SysFont(fonts[47], 40)


