import pygame
import os
from utils.color import Color
from utils.font import Font


class Comment:
    WIDTH, HEIGHT = 750, 100
    LEFT, TOP = 0, 0

    MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "background-black.png")),
                                     (WIDTH, HEIGHT))
    comments = []

    def __init__(self, surface):
        pygame.font.init()
        pygame.init()
        self.surface = surface
        self.surface.blit(self.MENU_BG, (self.LEFT, self.TOP))

    def draw_window(self):
        # pygame.draw.rect(self.surface, Color.BLACK, (self.LEFT, self.TOP, Size.SCREEN_WIDTH, Size.SCREEN_HEIGHT))
        pass

    def add_round_text(self, round_number: int):
        x_cor = self.LEFT + 10
        y_cor = self.TOP + 10
        round_text = Font.ROUND_FONT.render(f'Round: {round_number}', False, Color.BLACK)
        self.surface.blit(round_text, (x_cor, y_cor))

    def add_comment(self, text):
        self.comments.append(text)

    def display_comments(self):
        x_cor = self.LEFT + self.WIDTH / 2
        y_cor = self.TOP + 20
        for comment_text in self.comments:
            comment = Font.COMMENT_FONT.render(comment_text, False, Color.WHITE)
            self.surface.blit(comment, (x_cor, y_cor))
            y_cor += 20

    def delete_comments(self):
        self.comments.clear()
