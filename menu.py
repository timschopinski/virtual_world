import pygame
import pygame_menu
import os
from utils.font import Font
from utils.color import Color
import world
from gui.board import BoardGUI


class Menu:
    THEME = pygame_menu.Theme(background_color=(0, 0, 0, 0),
                              title_background_color=(0, 0, 0),
                              title_font_shadow=True,
                              widget_padding=20,
                              widget_offset=(0, 0),
                              widget_font=Font.MENU_FONT,
                              widget_font_color=(255, 255, 255)
                              )

    def __init__(self, main_function):
        pygame.font.init()
        pygame.init()
        pygame.display.set_caption("World Simulator")
        self.surface = pygame.display.set_mode((750, 750))
        self.main_function = main_function

    @staticmethod
    def save_rows(number_of_rows: tuple, *args):
        BoardGUI.BOARD_ROWS = number_of_rows[1]

    @staticmethod
    def save_columns(number_of_columns: tuple, *args):
        BoardGUI.BOARD_COLUMNS = number_of_columns[1]

    @staticmethod
    def save_color_1(color):
        Color.BOARD_COLOR_1 = color

    @staticmethod
    def save_color_2(color):
        Color.BOARD_COLOR_2 = color

    @staticmethod
    def save_concentration(concentration):
        # Size.CONCENTRATION = int(concentration)
        world.World.CONCENTRATION = concentration

    def set_difficulty(self, difficulty, x):
        pass

    @staticmethod
    def set_highlight():
        pygame_menu.widgets.HighlightSelection(border_width=100, margin_x=30, margin_y=20)

    def display_menu(self):
        self.menu = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()
        self.menu.add.button('Play', self.main_function)
        self.menu.add.button('Settings', self.display_settings)
        self.menu.add.button('Comments', self.display_comments)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.surface)

    def display_comments(self):
        comment_section = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()
        comment_section.add.button('BACK', self.display_menu)
        info = Comment(self.surface)
        if info.comments:
            for comment in info.comments:
                if 'Round' in comment:
                    comment_section.add.label(comment, font_size=20)
                else:
                    comment_section.add.label(comment, font_size=10)
        else:
            comment_section.add.label('No comments available...', font_size=20)
        comment_section.mainloop(self.surface)

    def display_settings(self):
        self.settings = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()

        self.settings.add.button('BACK', self.display_menu)
        # self.menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=self.set_difficulty)
        self.settings.add.color_input('BOARD COLOR 1: ',
                                      color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                                      default=Color.GREEN, font_size=18, onchange=self.save_color_1)
        self.settings.add.color_input('BOARD COLOR 2: ',
                                      color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                                      default=Color.GREY, font_size=18, onchange=self.save_color_2)
        self.settings.add.selector('ROWS: ', [(str(i), i) for i in range(20)], onchange=self.save_rows, default=10)
        self.settings.add.selector('COLUMNS: ', [(str(i), i) for i in range(20)], onchange=self.save_columns,
                                   default=10)
        self.settings.add.range_slider('CONCENTRATION[%]: ', range_values=(0, 100), default=100, increment=10,
                                       onchange=self.save_concentration)
        self.settings.mainloop(self.surface)


class Comment:
    WIDTH, HEIGHT = 750, 100
    LEFT, TOP = 0, 0
    pygame.font.init()
    MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "background-black.png")),
                                     (WIDTH, HEIGHT))
    comments = []

    def __init__(self, surface, *args, **kwargs):
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
