from utils.color import Color
import pygame


class BoardGUI:
    SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
    BOARD_WIDTH, BOARD_HEIGHT = 750, 750
    BOARD_ROWS, BOARD_COLUMNS = 10, 10

    def __init__(self):
        self.field_width = round(self.SCREEN_WIDTH / self.BOARD_COLUMNS)
        self.field_height = round(self.SCREEN_HEIGHT / self.BOARD_ROWS)

    @staticmethod
    def is_even(number: int) -> bool:
        if number % 2 == 0:
            return True
        else:
            return False

    def draw_field(self, x, y):
        if self.is_even(x) and self.is_even(y):
            color = Color.BOARD_COLOR_1
        elif self.is_even(x) and not self.is_even(y):
            color = Color.BOARD_COLOR_2
        elif not self.is_even(x) and self.is_even(y):
            color = Color.BOARD_COLOR_2
        elif not self.is_even(x) and not self.is_even(y):
            color = Color.BOARD_COLOR_1
        else:
            color = Color.WHITE
        pygame.draw.rect(self.window, color,
                         (y * self.field_width, x * self.field_height, self.field_width, self.field_height))
