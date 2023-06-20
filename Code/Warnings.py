import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *

class Warnings:

    def __init__(self, screen):
        self.screen = screen
        pass  # todo define more attributes
    def play_again(self):
        pygame.draw.rect(self.screen, "white", (10, 600, 1000, 600))
        play_again_text = Setup.PLAY_AGAIN_FONT.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(Setup.WIDTH / 2, 700))
        word_was_text = Setup.PLAY_AGAIN_FONT.render(f"The word was {Setup.CORRECT_WORD}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(Setup.WIDTH / 2, 650))
        self.screen.blit(word_was_text, word_was_rect)
        self.screen.blit(play_again_text, play_again_rect)
        pygame.display.update()
