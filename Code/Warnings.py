import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *

class Warnings:
    def __init__(self, screen):
        self.screen = screen

    def get_warning_bottom(self, end_behaviour):
        is_not_clicked = True
        while is_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    is_not_clicked = False
                else:
                    pygame.draw.rect(self.screen, Colors.BACKGROUND.value, (10 + 55, 600 + 60, 1000, 600))
                    if end_behaviour == "winner":
                        text, rect = self.win_game_warning()
                    elif end_behaviour == "loser":
                        text, rect = self.lose_game_warning()
                    again_text, again_rect = self.play_again_warn()
                    press_enter = Setup.PLAY_AGAIN_FONT.render(f"Press Enter To Try Again", True, "black")
                    press_rect = press_enter.get_rect(center=(Setup.WIDTH / 2, 750 + 60))
                    self.screen.blit(text, rect)
                    self.screen.blit(again_text, again_rect)
                    self.screen.blit(press_enter, press_rect)
                    pygame.display.update()

    def get_warning_top(self, end_behaviour):
        if end_behaviour == "letter_nr":
            text, rect = self.word_has_to_have_5_letter_warning()
        elif end_behaviour == "base_error":
            text, rect = self.word_not_in_base_warning()
        self.screen.blit(text, rect)
        pygame.display.update()

    def play_again_warn(self):
        again_text = Setup.PLAY_AGAIN_FONT.render(f"The word was {Setup.CORRECT_WORD}!", True, "black")
        again_rect = again_text.get_rect(center=(Setup.WIDTH / 2, 650 + 60))
        return again_text, again_rect

    def win_game_warning(self):
        winner_text = Setup.PLAY_AGAIN_FONT.render("Congrats, You win the game!", True, "black")
        winner_rect = winner_text.get_rect(center=(Setup.WIDTH / 2, 700 + 60))
        return winner_text, winner_rect

    def lose_game_warning(self):
        loser_text = Setup.PLAY_AGAIN_FONT.render("You lose. Unlucky!", True, "black")
        loser_rect = loser_text.get_rect(center=(Setup.WIDTH / 2, 700 + 60))
        return loser_text, loser_rect

    def word_not_in_base_warning(self):
        unknown_word_text = Setup.PLAY_AGAIN_FONT.render("No such word in base!", True, "black")
        unknown_word_rect = unknown_word_text.get_rect(center=(Setup.WIDTH / 2, 33))
        return unknown_word_text, unknown_word_rect

    def word_has_to_have_5_letter_warning(self):
        wrong_letter_number_text = Setup.PLAY_AGAIN_FONT.render("Word has to have 5 letter!", True, "black")
        wrong_letter_number_rect = wrong_letter_number_text.get_rect(center=(Setup.WIDTH / 2, 33))
        return wrong_letter_number_text, wrong_letter_number_rect
