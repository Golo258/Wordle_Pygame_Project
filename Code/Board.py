class Board:
    def __init__(self):
        self.letters = pygame.sprite.Group()
        self.current_row = 0
        self.current_column = 0
        self.word_to_find = random.choice(words)

        for row in range(6):
            for column in range(5):
                x = column * 100 + 12
                y = row * 100 + 12
                letter = Letter(x, y)
                self.letters.add(letter)

    def update(self):
        self.letters.update()

    def draw(self):
        self.letters.draw(screen)
        pygame.draw.rect(screen, GREEN, [5, self.current_row * 100 + 5, WIDTH - 10, 90], 3, 5)

    def handle_event(self, event):
        for letter in self.letters:
            letter.handle_event(event)

    def handle_key_event(self, event):
        for letter in self.letters:
            letter.handle_key_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.current_row += 1
                if self.current_row >= 6:
                    self.current_row = 5
            elif event.key == pygame.K_RETURN:
                self.check_word()

    def check_word(self):
        player_word = ""
        for column in range(5):
            for letter in self.letters:
                if letter.rect.collidepoint((column * 100 + 50, letter.rect.centery)):
                    player_word += letter.letter
        if player_word == self.word_to_find:
            print("You win!")
        else:
            print("Wrong guess!")

    def reset(self):
        self.current_row = 0
        self.word_to_find = random.choice(words)
        for letter in self.letters:
            letter.clear_letter()

