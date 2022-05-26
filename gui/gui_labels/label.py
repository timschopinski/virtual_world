import pygame
from utils.color import Color
from utils.point import Point
from utils.font import Font


class LabelGUI:
    SCREEN_WIDTH = 750
    SCREEN_HEIGHT = 750

    def __init__(self, window: pygame.Surface, world, top_left: Point, board_position: tuple, width=200, height=400):
        self.window = window
        self.world = world
        self.width = width
        self.height = height
        self.board_position = Point(board_position)
        self.top_left = top_left
        if top_left.x + self.width > self.SCREEN_WIDTH:
            new_top_left_x = self.SCREEN_WIDTH - self.width
            self.top_left.x = new_top_left_x
        if top_left.y + self.height > self.SCREEN_HEIGHT:
            new_top_left_y = self.SCREEN_HEIGHT - self.height
            self.top_left.y = new_top_left_y

    def draw_window(self, title, color=Color.LIGHT_GREY):
        pygame.draw.rect(self.window, color, (self.top_left.x, self.top_left.y, self.width, self.height))
        title = Font.TITLE_CHOICE_LIST_FONT.render(title, False, (0, 0, 0))
        self.window.blit(title, self.top_left.get_tuple())

    def draw_exit_button(self, position: tuple):
        text = Font.CHOICE_LIST_FONT.render('Exit', False, (0, 0, 0))
        self.window.blit(text, position)

    def is_position_on_exit(self, position: tuple) -> bool:
        if self.top_left.x + 100 < position[0] < self.top_left.x + self.width \
                and self.top_left.y + 350 < position[1] < self.top_left.y + self.height:
            return True
        else:
            return False

