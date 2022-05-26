import pygame
from utils.point import Point
from gui.gui_labels.label import LabelGUI
from utils.color import Color
from utils.font import Font


class InfoLabel(LabelGUI):
    DESCRIPTION_HEIGHT = 300

    def __init__(self, window: pygame.Surface, world, top_left: Point, board_position: tuple):
        super().__init__(window, world, top_left, board_position)
        self.organism = self.get_displayed_organism()
        self.organism_info = {
            'Age': self.organism.age,
            'Strength': self.organism.strength,
            'Initiative': self.organism.initiative,
            'Type': 'Animal' if self.organism.is_animal else 'Plant',
            'Description': ''
        }

    def display(self):
        self.draw_window(f'{self.organism}')
        self.draw_info_list()
        self.draw_exit_button((self.top_left.x + self.width - 50, self.top_left.y + self.height - 50))

    def get_displayed_organism(self):
        return self.world.board[self.board_position.x][self.board_position.y]

    def draw_info_list(self):
        text_position = Point(self.top_left.x, self.top_left.y + 50)
        gap = self.DESCRIPTION_HEIGHT / (len(self.organism_info) + 2)
        for info in self.organism_info.keys():
            info += f':   {self.organism_info[info]}'
            pygame.draw.line(self.window, color=Color.GREY, start_pos=text_position.get_tuple(),
                             end_pos=(text_position.x + self.width, text_position.y))
            text = Font.CHOICE_LIST_FONT.render(info, False, (0, 0, 0))
            self.window.blit(text, text_position.get_tuple())
            text_position.update(text_position.x, text_position.y + gap)
        self.draw_description(text_position)

    def draw_description(self, text_position):

        info = self.organism.get_description()
        description_text = ""
        text_left = len(info)
        for letter in info:
            description_text += letter
            if len(description_text) > 30:
                text = Font.SMALL_FONT.render(description_text, False, (0, 0, 0))
                self.window.blit(text, text_position.get_tuple())
                text_position.update(text_position.x, text_position.y + 15)
                description_text = ""
                text_left -= 30
            elif text_left < 30:
                description_text = info[len(info)-text_left:-1]
                text = Font.SMALL_FONT.render(description_text, False, (0, 0, 0))
                self.window.blit(text, text_position.get_tuple())

    def delete_label(self):
        self.world.info_label = None
        del self

    def handle_user_input(self, position: tuple):
        if self.is_position_on_exit(position):
            self.delete_label()

