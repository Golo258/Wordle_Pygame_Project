import random
import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *
from Letter_Key import Letter_Key
from Letter import Letter
from Warnings import Warnings
class Keyboard:
    def __init__(self, screen, game_result):
        self.guesses = [[]] * 6  # todo change name to guesses_list
        self.guesses_count = 0
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110
        self.keys = []  # todo change name to letter_key
        self.key_x = 20 + 55
        self.key_y = 600 + 80
        self.game_result = game_result
        self.screen = screen
        self.background_rect = Setup.BACKGROUND.get_rect(center=(317 + 55, 300 + 60))
        self.warning = Warnings(self.screen)

    def draw_keyboard(self):
        for i in range(3):
            for letter in Setup.ALPHABETS[i]:
                new_key = Letter_Key(self.key_x, self.key_y, letter)
                self.keys.append(new_key)
                new_key.draw(self.screen)
                self.key_x += 60
            self.key_y += 100
            if i == 0:
                self.key_x = 50 + 55
            elif i == 1:
                self.key_x = 105 + 55

    def check_guess_correctness(self):
        game_decided = False
        for i in range(5):
            letter = self.current_guess[i].text.lower()
            if letter in Setup.CORRECT_WORD:
                if letter in Setup.CORRECT_WORD[i]:
                    self.current_guess[i].bg_color = Colors.CORRECT_CHOOSE.value
                    for key in self.keys:
                        if key.text == letter.upper():
                            key.bg_color = Colors.GREEN.value
                            key.draw(self.screen)
                    self.current_guess[i].text_color = Colors.GREEN.value
                    if not game_decided:
                        self.game_result = "Win"
                else:
                    self.current_guess[i].bg_color = Colors.YELLOW.value
                    for key in self.keys:
                        if key.text == letter.upper():
                            key.bg_color = Colors.GOLD.value
                            key.draw(self.screen)
                    self.current_guess[i].text_color = Colors.GOLD.value
                    self.game_result = ""
                    game_decided = True
            else:
                self.current_guess[i].bg_color = Colors.GREY.value
                for key in self.keys:
                    if key.text == letter.upper():
                        key.bg_color = Colors.GREY.value
                        key.draw(self.screen)
                self.current_guess[i].text_color = Colors.GRAY.value
                self.game_result = ""
                game_decided = True
            self.current_guess[i].draw(self.screen)
            pygame.display.update()

        self.guesses_count += 1
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110

        if self.guesses_count == 6 and self.game_result == "":
            self.warning.get_warning_bottom("loser")
            self.reset_game()

        if self.guesses_count < 6 and self.game_result == "Win":
            self.warning.get_warning_bottom("winner")
            self.reset_game()

    def reset_game(self):
        self.guesses = [[]] * 6
        self.guesses_count = 0
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110
        self.game_result = ""
        self.screen.fill(Colors.BACKGROUND.value)
        self.screen.blit(Setup.BACKGROUND, self.background_rect)
        Setup.CORRECT_WORD = random.choice(words)
        print(Setup.CORRECT_WORD)
        for key in self.keys:
            key.bg_color = Setup.OUTLINE
            key.draw(self.screen)
        pygame.display.update()

    def create_new_letter(self, key_pressed):
        self.current_guess_string += key_pressed
        new_letter = Letter(key_pressed,
                            (self.current_letter_bg_x + 54, self.guesses_count * 100 + Setup.LETTER_Y_SPACING + 60))
        self.current_letter_bg_x += Setup.LETTER_X_SPACING
        self.guesses[self.guesses_count].append(new_letter)
        self.current_guess.append(new_letter)
        for guess in self.guesses:
            for letter in guess:
                letter.draw(self.screen)

    def delete_letter(self):
        self.guesses[self.guesses_count][-1].delete(self.screen)
        self.guesses[self.guesses_count].pop()
        self.current_guess_string = self.current_guess_string[:-1]
        self.current_guess.pop()
        self.current_letter_bg_x -= Setup.LETTER_X_SPACING
