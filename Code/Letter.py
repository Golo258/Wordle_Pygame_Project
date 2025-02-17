from Wordle_Game.Wordle_Pygame_Project.Resources.Setup import *
from Wordle_Game.Wordle_Pygame_Project.Resources.Colors import *


class Letter(pygame.sprite.Sprite):
    def __init__(self, text, bg_position):
        super().__init__()
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = Colors.GRAY.value
        self.text_color = Colors.BLACK.value
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, Setup.LETTER_SIZE, Setup.LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == Colors.GRAY.value:
            pygame.draw.rect(screen, Setup.FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = Setup.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self, screen):
        pygame.draw.rect(screen, Colors.GRAY.value, self.bg_rect)
        pygame.draw.rect(screen, Setup.OUTLINE, self.bg_rect, 3)
        pygame.display.update()



