import pygame
import sys
import random

from Wordle_Pygame_Project.Resources.Settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Wordle Game GG")
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            self.board.update()
            self.board.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.handle_event(event)
                    self.board.handle_key_event(event)
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
