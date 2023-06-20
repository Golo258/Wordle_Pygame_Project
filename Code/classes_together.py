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


class Setup():
    WIDTH = 633
    HEIGHT = 900
    FPS = 60
    ICON = None
    ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
    AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)
    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 12
    LETTER_SIZE = 75
    OUTLINE = "#d3d6da"
    FILLED_OUTLINE = "#878a8c"
    CORRECT_WORD = "coder"
    print(CORRECT_WORD)
    BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
    PLAY_AGAIN_FONT = pygame.font.Font("assets/FreeSansBold.otf", 40)
    # TODO render font from resource


class Letter(pygame.sprite.Sprite):
    def __init__(self, text, bg_position):
        super().__init__()
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, Setup.LETTER_SIZE, Setup.LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self, screen):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(screen, Setup.FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self, screen):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(screen, "white", self.bg_rect)
        pygame.draw.rect(screen, Setup.OUTLINE, self.bg_rect, 3)
        pygame.display.update()

        # todo check if screen is corectly assign in initialisation


class Letter_Key:
    # letter inditcator
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = Setup.OUTLINE

    def draw(self, screen):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = Setup.AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()


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


class Warnings:

    def __init__(self, screen):
        self.screen = screen
        pass  # todo definy attributes

    def play_again(self):
        pygame.draw.rect(self.screen, "white", (10, 600, 1000, 600))
        play_again_text = Setup.PLAY_AGAIN_FONT.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(Setup.WIDTH / 2, 700))
        word_was_text = Setup.PLAY_AGAIN_FONT.render(f"The word was {Setup.CORRECT_WORD}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(Setup.WIDTH / 2, 650))
        self.screen.blit(word_was_text, word_was_rect)
        self.screen.blit(play_again_text, play_again_rect)
        pygame.display.update()

class Game:
    def __init__(self):
        # pygame.display.set_icon(Setup.ICON) # TODO add new icon from resources
        self.screen = pygame.display.set_mode((Setup.WIDTH, Setup.HEIGHT))
        pygame.display.set_caption("Wordle Grzesiuniunia Game!")
        self.keyboard = Keyboard()
        self.warning = Warnings(self.screen)
        self.game_result = self.keyboard.game_result
        self.background_rect=  Setup.BACKGROUND.get_rect(center=(317, 300))

    def run(self):
        self.screen.fill("white")
        self.screen.blit(Setup.BACKGROUND, self.background_rect)
        pygame.display.update()
        self.keyboard.draw_keyboard(self.screen)
        while True:
            if self.game_result != "":
                self.warning.play_again()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game_result != "":
                            self.keyboard.reset_game(self.screen, self.background_rect)
                        else:
                            if len(self.keyboard.current_guess_string) == 5 and self.keyboard.current_guess_string.lower() in words:
                                self.keyboard.check_guess_correctness()
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.keyboard.current_guess_string) > 0:
                            self.keyboard.delete_letter(self.screen)
                    else:
                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                            if len(self.keyboard.current_guess_string) < 5:
                                self.keyboard.create_new_letter(key_pressed, self.screen)


if __name__ == '__main__':
    game = Game()
    game.run()

    pygame.quit()
