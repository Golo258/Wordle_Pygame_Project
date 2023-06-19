import pygame
from pygame.sprite import Sprite
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import *

class Letter(Sprite):
    class Letter(Sprite):
        class Letter(pygame.sprite.Sprite):
            def __init__(self, col, row):
                super().__init__()
                self.value = " "
                self.col = col
                self.row = row
                self.rect = pygame.Rect(col * 100 + 12, row * 100 + 12, 75, 75)

            def set_letter(self, letter):
                self.value = letter

            def clear_letter(self):
                self.value = " "

            def draw(self, screen):
                pygame.draw.rect(screen, WHITE, self.rect, 3, 5)
                piece_text = HUGE_FONT.render(self.value, True, GRAY)
                screen.blit(piece_text, (self.rect.x + 18, self.rect.y + 13))
