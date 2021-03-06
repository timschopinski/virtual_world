from utils.color import Color
import pygame
from abc import ABC


class BoardGUI(ABC):
    SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
    BOARD_WIDTH, BOARD_HEIGHT = 750, 750
    BOARD_ROWS, BOARD_COLUMNS = 10, 10

    def __init__(self):
        self.field_width = round(self.SCREEN_WIDTH / self.BOARD_COLUMNS)
        self.field_height = round(self.SCREEN_HEIGHT / self.BOARD_ROWS)

    @staticmethod
    def _is_even(number: int) -> bool:
        """ Returns True if number is even"""
        if number % 2 == 0:
            return True
        else:
            return False

    def draw_field(self, window, x, y):
        """ Draws a rectangle field on the screen at given coordinates"""
        if self._is_even(x) and self._is_even(y):
            color = Color.BOARD_COLOR_1
        elif self._is_even(x) and not self._is_even(y):
            color = Color.BOARD_COLOR_2
        elif not self._is_even(x) and self._is_even(y):
            color = Color.BOARD_COLOR_2
        elif not self._is_even(x) and not self._is_even(y):
            color = Color.BOARD_COLOR_1
        else:
            color = Color.WHITE
        pygame.draw.rect(window, color,
                         (y * self.field_width, x * self.field_height, self.field_width, self.field_height))
