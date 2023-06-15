import pygame
from Letter import Letter
from Wordle_Game.Wordle_Pygame_Project.Resources.Settings import  *
import random
from Wordle_Game.Wordle_Pygame_Project.Resources.words_eng import  *

class Board:
    def __init__(self):
        self.player_turn = 0
        self.game_over = False
        self.letters = [Letter(col, row) for row in range(6) for col in range(5)]
        self.secret_word = words[random.randint(0, len(words) - 1)]

    def draw(self, screen):
        for letter in self.letters:
            letter.draw(screen)
        pygame.draw.rect(screen, GREEN, [5, self.player_turn * 100 + 5, WIDTH - 10, 90], 3, 5)
    #     dwrawing the green rect

    def check_words(self, screen):
        for letter in self.letters:
            if self.secret_word[letter.row_positon] == letter.value and self.player_turn > letter.letter_number:
                pygame.draw.rect(screen, GREEN, letter.rect, 0, 5)
            elif letter.value in self.secret_word and self.player_turn > letter.letter_number:
                pygame.draw.rect(screen, YELLOW, letter.rect, 0, 5)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.TEXTINPUT and self.player_turn < 6 and not self.game_over:
                tile_entry = event.__getattribute__("text")
                for letter in self.letters:
                    if letter.value == " ":
                        letter.set_letter(tile_entry.lower())
                        break

            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    for letter in self.letters:
                        if letter.value != " ":
                            letter.clear_letter()
                            break
                elif event.key == pygame.K_SPACE and not self.game_over:
                    self.player_turn += 1
                    self.clear_letters()
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.player_turn = 0
                    self.clear_letters()
                    self.game_over = False
                    self.secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]


    def clear_letters(self):
        for letter in self.letters:
            letter.clear_letter()