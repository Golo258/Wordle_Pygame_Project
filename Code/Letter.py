import pygame
import sys
import random
from Wordle_Pygame_Project.Resources.Settings import *


class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((75, 75))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.letter = " "

    def update(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 3, 5)
        piece_text = HUGE_FONT.render(self.letter, True, GRAY)
        screen.blit(piece_text, (self.rect.x + 18, self.rect.y + 13))

    def set_letter(self, letter):
        self.letter = letter

    def clear_letter(self):
        self.letter = " "