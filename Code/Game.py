import pygame
import sys
import random

from Wordle_Pygame_Project.Resources.Settings import *
from Wordle_Pygame_Project.Resources.words_eng import *
from Board import Board

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Wordle Knockoff')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.turn = 0
        self.secret_word = words[random.randint(0, len(words) - 1)]
        self.game_over = False
        self.letters = 0
        self.turn_active = True

    def check_words(self):
        for col in range(0, 5):
            for row in range(0, 6):
                letter = self.board.letters.sprites()[row * 5 + col]
                if self.secret_word[col] == letter.letter and self.turn > row:
                    pygame.draw.rect(self.screen, GREEN, letter.rect, 0, 5)
                elif letter.letter in self.secret_word and self.turn > row:
                    pygame.draw.rect(self.screen, YELLOW, letter.rect, 0, 5)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            self.check_words()
            self.board.draw(self.screen)
            pygame.key.set_repeat(500, 100)
            pygame.event.set_grab(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.TEXTINPUT and self.turn_active and not self.game_over:
                    entry = event.__getattribute__("text")
                    if entry != " ":
                        entry = entry.lower()
                        self.board.letters.sprites()[self.letters].set_letter(entry)
                        self.letters += 1
                        print(entry)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and self.letters > 0:
                        self.board.letters.sprites()[self.letters - 1].clear_letter()
                        self.letters -= 1
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.turn += 1
                        self.letters = 0
                    if  event.key == pygame.K_SPACE and self.game_over:
                        self.turn = 0
                        self.letters = 0
                        self.game_over = False
                        self.secret_word = words[random.randint(0, len(words) - 1)]
                        for letter in self.board.letters:
                            letter.clear_letter()

                # Control turn active based on letters
                if self.letters == 5:
                    self.turn_active = False
                if self.letters < 5:
                    self.turn_active = True

            # Check if guess is correct and update game state
            word = self.board.get_word()
            if word == self.secret_word and self.turn < 6:
                self.game_over = True

            # Draw game over messages
            if self.turn == 6:
                game_over = True
                loser_text = HUGE_FONT.render('Loser!', True, WHITE)
                self.screen.blit(loser_text, (40, 610))

            if self.game_over and self.turn < 6:
                winner_text = HUGE_FONT.render('Winner!', True, WHITE)
                self.screen.blit(winner_text, (40, 610))

            pygame.display.flip()
    # Run the game
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
