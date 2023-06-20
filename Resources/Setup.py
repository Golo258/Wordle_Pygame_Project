import pygame

pygame.init()
class Setup():
    WIDTH = 633
    HEIGHT = 900
    FPS = 60
    ICON = None
    ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
    AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)
    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 12
    LETTER_SIZE = 75
    OUTLINE = "#d3d6da"
    FILLED_OUTLINE = "#878a8c"
    CORRECT_WORD = "coder"
    print(CORRECT_WORD)
    BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
    PLAY_AGAIN_FONT = pygame.font.Font("assets/FreeSansBold.otf", 40)
    # TODO render font from resource

