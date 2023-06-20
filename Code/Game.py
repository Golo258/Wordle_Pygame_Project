
import pygame
import random
import sys
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import  *
from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import  *
from Keyboard import Keyboard
from Warnings import Warnings

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
