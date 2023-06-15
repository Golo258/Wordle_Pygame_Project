import pygame
import sys
import random
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import  *



class Letter:
    def __init__(self, row_positon, letter_number):
        self.row_positon = row_positon # row position
        self.letter_number = letter_number
        self.value = " "
        self.rect = pygame.Rect(self.row_positon * 100 + 12, self.letter_number * 100 + 12, 75, 75)

    def set_letter(self, letter):
        if isinstance(letter, str):
            if letter.isalpha():
                self.value = letter
        else: # TODO to implement proper communicate for that
            print("Value should be a letter not int")
    def clear_letter(self):
        self.value = " "

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 3, 5)
        piece_text = HUGE_FONT.render(self.value, True, GRAY)
        screen.blit(piece_text, (self.row_positon * 100 + 30, self.letter_number * 100 + 25))
