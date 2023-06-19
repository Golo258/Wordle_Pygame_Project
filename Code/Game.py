
from Board import Board
import pygame
import random
import sys
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import  *
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import  *

class Game:
    def __init__(self, screen, secret_word):
        self.turn = 0
        self.game_over = False
        self.letters = 0
        self.turn_active = True
        self.screen = screen
        self.secret_word = secret_word
        self.board = Board()

    def run(self):
        def update(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.flag_win or self.flag_lose:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.reset_game()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if self.curr_word:
                                self.curr_word = self.curr_word[:-1]
                                self.curr_letter -= 1
                        elif event.key == pygame.K_RETURN:
                            if len(self.curr_word) == LETTER_LENGTH:
                                if self.curr_word.lower() in self.wordlist:
                                    self.word_count += 1
                                    self.used_words.append(self.curr_word)
                                    self.curr_word = ""
                                    self.curr_letter = 0
                                else:
                                    self.flag_invalid_word = True
                                    self.timer_flag_1 = 0
                            else:
                                self.flag_not_enough_letters = True
                                self.timer_flag_2 = 0
                        else:
                            if len(self.curr_word) < LETTER_LENGTH:
                                if event.unicode.isalpha():
                                    self.curr_word += event.unicode.upper()
                                    self.curr_letter += 1