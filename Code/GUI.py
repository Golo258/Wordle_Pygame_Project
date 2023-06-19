import pygame
import random

from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import *
from Game import Game


class GUI:
    def __init__(self):
        # self.keyboard = Keyboard()
        self.warning = Warning()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.secret_word = words[random.randint(0, len(words) - 1)]
        self.game = Game(self.screen, self.secret_word)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)

            self.game.draw(self.screen)
            # self.keyboard.draw(screen)
            self.warning.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.game.update(event)

            guess = ""
            for col in range(0, 5):
                guess += self.game.board.letters[self.game.turn][col]
            if guess == self.secret_word and self.game.turn < 6:
                self.game.game_over = True
                self.warning.set_message("Congratulations! You guessed the word!")
            elif self.game.turn == 6:
                self.game.game_over = True
                self.warning.set_message("Game over. You didn't guess the word.")
            else:
                self.warning.set_message("")

            pygame.display.flip()

        pygame.quit()

# Uruchomienie gry
if __name__ == '__main__':
    gui = GUI()
    gui.run()