import random
import pygame
import sys
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import *
from enum import Enum

pygame.init()


class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (192, 192, 192)
    DARK_GRAY = (64, 64, 64)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    BROWN = (165, 42, 42)
    GOLD = (255, 215, 0)
    GREY = (100, 100, 100)
    DARK_GREY = (20, 20, 20)
    INCORRECT_CHOOSE = (50, 50, 50)
    MISPLACED_CHOOSE = (255, 193, 53)
    CORRECT_CHOOSE = (0, 185, 6)
    BACKGROUND = (51, 51, 51)


class Setup():
    WIDTH = 633 + 110  # 750 - x - 110
    HEIGHT = 900 + 80  # 980  - y -  80
    FPS = 60
    ICON = None
    ALPHABETS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    fonts= pygame.font.get_fonts()
    GUESSED_LETTER_FONT = pygame.font.SysFont(fonts[0], 50)
    AVAILABLE_LETTER_FONT = pygame.font.SysFont(fonts[0], 25)
    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 12
    LETTER_SIZE = 75
    OUTLINE = "#d3d6da"
    FILLED_OUTLINE = "#878a8c"
    CORRECT_WORD = "coder"
    print(CORRECT_WORD)
    BACKGROUND = pygame.image.load("assets/Background_tile.png")
    PLAY_AGAIN_FONT = pygame.font.SysFont(fonts[0], 40)


class Letter(pygame.sprite.Sprite):
    def __init__(self, text, bg_position):
        super().__init__()
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = Colors.GRAY.value
        self.text_color = Colors.BLACK.value
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, Setup.LETTER_SIZE, Setup.LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == Colors.GRAY.value:
            pygame.draw.rect(screen, Setup.FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self, screen):
        pygame.draw.rect(screen, Colors.GRAY.value, self.bg_rect)
        pygame.draw.rect(screen, Setup.OUTLINE, self.bg_rect, 3)
        pygame.display.update()


class Letter_Key:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = Setup.OUTLINE

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = Setup.AVAILABLE_LETTER_FONT.render(self.text, True, Colors.GRAY.value)
        self.text_rect = self.text_surface.get_rect(center=(self.x + 20, self.y + 23))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()


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
        unknown_word_rect = unknown_word_text.get_rect(center=(Setup.WIDTH / 2, 30))
        return unknown_word_text, unknown_word_rect

    def word_has_to_have_5_letter_warning(self):
        wrong_letter_number_text = Setup.PLAY_AGAIN_FONT.render("Word has to have 5 letter!", True, "black")
        wrong_letter_number_rect = wrong_letter_number_text.get_rect(center=(Setup.WIDTH / 2, 30))
        return wrong_letter_number_text, wrong_letter_number_rect


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Setup.WIDTH, Setup.HEIGHT))
        pygame.display.set_caption("Wordle Grzesiuniunia Game!")
        self.game_result = ""
        self.keyboard = Keyboard(self.screen, self.game_result)
        self.warning = Warnings(self.screen)
        self.is_top_warning = False

    def run(self):

        self.screen.fill(Colors.BACKGROUND.value)
        self.screen.blit(Setup.BACKGROUND, self.keyboard.background_rect)
        pygame.display.update()
        self.keyboard.draw_keyboard()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.keyboard.current_guess_string) == 5 and self.keyboard.current_guess_string.lower() in words:
                            self.keyboard.check_guess_correctness()
                            pygame.draw.rect(self.screen, Colors.BACKGROUND.value, (129, 5, 500, 50))
                            pygame.display.update()
                            self.is_top_warning = False
                        elif len(self.keyboard.current_guess_string) < 5:
                            if self.is_top_warning:
                                pygame.draw.rect(self.screen, Colors.BACKGROUND.value, (129, 5, 500, 50))
                                pygame.display.update()
                            self.warning.get_warning_top("letter_nr")
                            self.is_top_warning = True

                        elif self.keyboard.current_guess_string not in words:
                            if self.is_top_warning:
                                pygame.draw.rect(self.screen, Colors.BACKGROUND.value, (129, 5, 500, 50))
                                pygame.display.update()
                            self.warning.get_warning_top("base_error")
                            self.is_top_warning = True

                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.keyboard.current_guess_string) > 0:
                            self.keyboard.delete_letter()
                    else:
                        key_pressed = event.unicode.upper()
                        if key_pressed.isalpha() and key_pressed != "":
                            if len(self.keyboard.current_guess_string) < 5 and self.keyboard.guesses_count < 6:
                                self.keyboard.create_new_letter(key_pressed)
                            else:
                                self.game_result = "Lose"

            pygame.draw.rect(
                self.screen, Colors.BLACK.value,
                (0, 0, Setup.WIDTH, Setup.WIDTH + 237), 5
            )
            pygame.display.update()

    def reset_game(self):
        self.keyboard.reset_game()


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
