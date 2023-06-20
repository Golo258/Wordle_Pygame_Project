import random
import pygame
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *
from Letter_Key import Letter_Key
from Letter import Letter
class Keyboard:
    def __init__(self):
        self.guesses = [[]] * 6  # todo change name to guesses_list
        self.guesses_count = 0
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110
        self.indicators = []  # todo change name to letter_key
        self.indicator_x = 20
        self.indicator_y = 600
        self.game_result = ""

    def draw_keyboard(self, screen):
        for i in range(3):
            for letter in Setup.ALPHABET[i]:
                new_indicator = Letter_Key(self.indicator_x, self.indicator_y, letter)
                self.indicators.append(new_indicator)
                new_indicator.draw(screen)
                self.indicator_x += 60
            self.indicator_y += 100
            if i == 0:
                indicator_x = 50
            elif i == 1:
                indicator_x = 105

    def check_guess_correctness(self):
        game_decided = False
        for i in range(5):
            letter = self.current_guess[i].text.lower()
            if letter in Setup.CORRECT_WORD:
                # jest w tekscie
                if letter == Setup.CORRECT_WORD[i]:
                    self.current_guess[i].bg_color = Colors.GREEN.value  # setting color of board letter
                    for indicator in self.indicators:
                        if indicator.text == letter.upper():
                            indicator.bg_color = Colors.GREEN.value  # setting color of  keyboard letter
                            indicator.draw()
                    self.current_guess[i].text_color = "white"  # changing color of text
                    if not game_decided:
                        self.game_result = "W"  # setting game as win
                else:
                    self.current_guess[i].bg_color = Colors.YELLOW.value  # yellow letter
                    for indicator in self.indicators:
                        if indicator.text == letter.upper():
                            indicator.bg_color = Colors.YELLOW.value  # yellow keyboard letter
                            indicator.draw()
                    self.current_guess[i].text_color = "white"  # setting text color
                    self.game_result = ""
                    game_decided = True
            else:
                self.current_guess[i].bg_color = Colors.GREY.value  # not in word letter
                for indicator in self.indicators:
                    if indicator.text == letter.upper():
                        indicator.bg_color = Colors.GREY.value  # in keyboard
                        indicator.draw()
                self.current_guess[i].text_color = "white"
                self.game_result = ""
                game_decided = True
            self.current_guess[i].draw()  # drawing guess
            pygame.display.update()

        self.guesses_count += 1
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110

        if self.guesses_count == 6 and self.game_result == "":
            game_result = "L"  # loose game
            # todo check if game_result is correctly indicated

    def reset_game(self, screen, back_rect):
        screen.fill("white")
        screen.blit(Setup.BACKGROUND, back_rect)
        self.guesses_count = 0
        CORRECT_WORD = random.choice(words)
        guesses = [[]] * 6
        self.current_guess = []
        self.current_guess_string = ""
        self.game_result = ""
        pygame.display.update()
        for indicator in self.indicators:
            indicator.bg_color = Setup.OUTLINE
            indicator.draw()

    # todo consider in game class the key_pressed as argument in create_new_letter
    def create_new_letter(self, key_pressed, screen):
        self.current_guess_string += key_pressed
        new_letter = Letter(key_pressed, (self.current_letter_bg_x, self.guesses_count * 100 + Setup.LETTER_Y_SPACING))
        self.current_letter_bg_x += Setup.LETTER_X_SPACING
        self.guesses[self.guesses_count].append(new_letter)
        self.current_guess.append(new_letter)
        for guess in self.guesses:
            for letter in guess:
                letter.draw(screen)

    def delete_letter(self, screen):
        self.guesses[self.guesses_count][-1].delete(screen)
        self.guesses[self.guesses_count].pop()
        self.current_guess_string = self.current_guess_string[:-1]
        self.current_guess.pop()
        self.current_letter_bg_x -= Setup.LETTER_X_SPACING
