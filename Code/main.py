import pygame
import random
import sys
from Wordle_Pygame_Project.Resources.Settings import *

# -----------------------------------------------

timer = pygame.time.Clock()
pygame.display.set_caption("Wordle Game GG")
screen = pygame.display.set_mode(
    [WIDTH, HEIGHT]
)
is_running = True
turn = 0
board[
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]


def draw_board():
    global turn
    global board
    for column in range (0, len(board[0])):
        for row in range(0, 6):
            pygame.draw.rect(screen, white, )



draw_board()

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            sys.exit()

    timer.tick(FPS)
    screen.fill("black")
    pygame.display.flip()

pygame.quit()
