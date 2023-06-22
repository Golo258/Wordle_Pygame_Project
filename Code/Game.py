import pygame
import random
import sys
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *
from Keyboard import Keyboard
from Warnings import Warnings


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Setup.WIDTH, Setup.HEIGHT))
        pygame.display.set_caption("Wordle GG Game!")
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
