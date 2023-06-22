import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *

class Letter_Key:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = Setup.OUTLINE

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = Setup.AVAILABLE_LETTER_FONT.render(self.text, True, Colors.GRAY.value)
        self.text_rect = self.text_surface.get_rect(center=(self.x + 20, self.y + 23))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()
