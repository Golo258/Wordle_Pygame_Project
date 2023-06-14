
from Letter import Letter
import pygame
from Wordle_Pygame_Project.Resources.Settings import *

class Board:
    def __init__(self):
        self.letters = pygame.sprite.Group()
        for row in range(6):
            for col in range(5):
                x = col * 100 + 12
                y = row * 100 + 12
                letter = Letter(x, y)
                self.letters.add(letter)

    def draw(self, screen):
        self.letters.draw(screen)

    def update(self, screen):
        self.letters.update(screen)

    def get_word(self):
        word = ""
        for col in range(5):
            for letter in self.letters:
                if letter.rect.collidepoint((col * 100 + 50, letter.rect.centery)):
                    word += letter.letter
        return word
