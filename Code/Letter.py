import pygame
import random
import sys
from Wordle_Pygame_Project.Resources.Settings import *
from Wordle_Pygame_Project.Resources.words_eng import *

# -----------------------------------------------

class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((75, 75))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.letter = " "
        self.font = pygame.font.Font(FONT_PATH, 56)
        self.clicked = False

    def update(self):
        if self.clicked:
            pygame.draw.rect(screen, GREEN, self.rect, 3, 5)
        else:
            pygame.draw.rect(screen, WHITE, self.rect, 3, 5)
        text_surface = self.font.render(self.letter, True, GRAY)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def set_letter(self, letter):
        self.letter = letter

    def clear_letter(self):
        self.letter = " "

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
            else:
                self.clicked = False

    def handle_key_event(self, event):
        if self.clicked and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and self.letter != " ":
                self.clear_letter()
            elif event.unicode.isalpha() and len(self.letter) == 0:
                self.set_letter(event.unicode)
