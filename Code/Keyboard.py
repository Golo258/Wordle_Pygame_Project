import pygame

from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import  *
#TODO to implement it more
class Keyboard:
    def __init__(self):
        self.key_width = 45
        self.key_height = 45
        self.margin = 5
        self.keys = []

        for row in range(0, 2):
            for col in range(0, 13):
                x = col * (self.key_width + self.margin) + 28
                y = row * (self.key_height + self.margin) + 550
                self.keys.append(pygame.Rect(x, y, self.key_width, self.key_height))

    def draw(self, screen):
        for key in self.keys:
            pygame.draw.rect(screen, WHITE, key)