import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import *

class Warning:
    def __init__(self):
        self.message = ""
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def set_message(self, message):
        self.message = message

    def draw(self, screen):
        text = self.font.render(self.message, True, WHITE)
        screen.blit(text, (30, 640))
