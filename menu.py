import pygame
import pygame_menu
from comment import Comment
from utils.font import Font
from utils.color import Color
from world import World
from gui.board import BoardGUI
from gui.world_gui import WorldGUI
from storage.save import Save
from storage.load import Load


class Menu:
    THEME = pygame_menu.Theme(
        background_color=(0, 0, 0, 0),
        title_background_color=(0, 0, 0),
        title_font_shadow=True,
        widget_padding=20,
        widget_offset=(0, 0),
        widget_font=Font.MENU_FONT,
        widget_font_color=(255, 255, 255)
    )

    def __init__(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_caption("World Simulator")
        self.surface = pygame.display.set_mode((750, 750))

    @staticmethod
    def save_rows(number_of_rows: tuple, *args, **kwargs):
        BoardGUI.BOARD_ROWS = number_of_rows[1] + 2

    @staticmethod
    def save_columns(number_of_columns: tuple, *args, **kwargs):
        BoardGUI.BOARD_COLUMNS = number_of_columns[1] + 2

    @staticmethod
    def save_color_1(color):
        Color.BOARD_COLOR_1 = color

    @staticmethod
    def save_color_2(color):
        Color.BOARD_COLOR_2 = color

    @staticmethod
    def save_concentration(concentration):
        World.CONCENTRATION = concentration

    def set_difficulty(self, difficulty, x):
        pass

    @staticmethod
    def start_simulation():
        world = WorldGUI()
        world.initialize()
        world.display()

    @staticmethod
    def set_highlight():
        pygame_menu.widgets.HighlightSelection(border_width=100, margin_x=30, margin_y=20)

    def add_menu_buttons(self, menu: pygame_menu.Menu):
        menu.add.button('Play', self.start_simulation)
        menu.add.button('Load', self.load_simulation)
        menu.add.button('Save', self.save_simulation)
        menu.add.button('Comments', self.display_comments)
        menu.add.button('Settings', self.display_settings)
        menu.add.button('Quit', pygame_menu.events.EXIT)

    def display_menu(self):
        menu = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()
        self.add_menu_buttons(menu)
        menu.mainloop(self.surface)

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
        self.settings.add.selector('ROWS: ', [(str(i), i) for i in range(2, 20)], onchange=self.save_rows, default=8)
        self.settings.add.selector('COLUMNS: ', [(str(i), i) for i in range(2, 20)], onchange=self.save_columns, default=8)
        self.settings.add.range_slider('CONCENTRATION[%]: ', range_values=(0, 100), default=100, increment=10,
                                       onchange=self.save_concentration)
        self.settings.mainloop(self.surface)

    def save_simulation(self):

        def save(file_path):
            save = Save(file_path)
            if not file_path:
                save_menu.clear()
                save_menu.add.label('No file entered', font_size=20)
                save_menu.add.button('BACK', self.display_menu)
            elif not save.world_state:
                save_menu.clear()
                save_menu.add.label('Uninitialized world can not be saved!', font_size=20)
                save_menu.add.button('BACK', self.display_menu)
            else:
                save.save_world_state()
                save_menu.clear()
                save_menu.add.label('world has been saved successfully!', font_size=20)
                save_menu.add.button('BACK', self.display_menu)

        save_menu = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()
        save_menu.add.text_input(title="Enter filename: ", default="my_simulation.txt", onreturn=save)
        save_menu.mainloop(self.surface)

    def load_simulation(self):

        def load(file_path):
            loaded_world = Load(file_path)
            if file_path == "":
                load_menu.clear()
                load_menu.add.label('No file entered', font_size=20)
                load_menu.add.button('BACK', self.display_menu)
            elif not loaded_world.is_path_valid():
                load_menu.clear()
                load_menu.add.label('This file does not contain a saved world', font_size=20)
                load_menu.add.button('BACK', self.display_menu)
            else:
                load_menu.clear()
                self.add_menu_buttons(load_menu)
                loaded_world.initialize()

        load_menu = pygame_menu.Menu('', BoardGUI.SCREEN_WIDTH, BoardGUI.SCREEN_HEIGHT, theme=self.THEME)
        self.set_highlight()
        load_menu.add.text_input(title="Enter filename: ", default="my_simulation.txt", onreturn=load)
        load_menu.mainloop(self.surface)
