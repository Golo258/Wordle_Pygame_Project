import pygame
import sys
import random

from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import  *
from Board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            self.board.check_words(self.screen)
            self.board.draw(self.screen)
            self.board.update()
            pygame.key.set_repeat(500, 100)
            pygame.event.set_grab(True)

            if self.board.player_turn == 6:
                self.board.game_over = True
                loser_text = HUGE_FONT.render('Loser!', True, WHITE)
                self.screen.blit(loser_text, (40, 610))

            if self.board.game_over and self.board.player_turn < 6:
                winner_text = HUGE_FONT.render('Winner!', True, WHITE)
                self.screen.blit(winner_text, (40, 610))

            pygame.display.flip()
    # Run the game
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
