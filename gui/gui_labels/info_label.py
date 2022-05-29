import pygame
from utils.point import Point
from gui.gui_labels.label import LabelGUI
from utils.color import Color
from utils.font import Font


class InfoLabel(LabelGUI):
    """ This Class represents the GUI list of organism attributes
        and special abilities """

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
        """ This method draws list with information about the organism"""
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

    def get_description_list(self):
        """ This method returns a list of sentences ready to add to the info label"""

        description = self.organism.get_description()
        description = description.split(' ')
        description_list = []
        sentence = ""
        for index, word in enumerate(description):
            if "\n" in word:
                word = word[:len(word)-1]
            sentence += (word + " ")
            if len(sentence) + len(word) > 25:
                description_list.append(sentence)
                sentence = ""
            elif index == len(description) - 1:
                sentence += (word + " ")
                description_list.append(sentence)

        return description_list

    def draw_description(self, text_position):
        """ This method draws a description sentences on the info_label label"""
        description = self.get_description_list()
        for sentence in description:
            text = Font.SMALL_FONT.render(sentence, False, (0, 0, 0))
            self.window.blit(text, text_position.get_tuple())
            text_position.update(text_position.x, text_position.y + 15)

    def delete_label(self):
        self.world.info_label = None
        del self

    def handle_user_input(self, position: tuple):
        if self.is_position_on_exit(position):
            self.delete_label()

