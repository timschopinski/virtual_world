import pygame
from utils.point import Point
from gui.gui_labels.label import LabelGUI
from utils.type import OrganismType


class ChoiceList(LabelGUI):
    """ This Class represents the GUI list of organisms,
        which is responsible for adding new organisms to the world """

    LIST_SIZE = 300
    list_of_organisms = [
        OrganismType.GRASS, OrganismType.WOLF, OrganismType.TURTLE,
        OrganismType.SHEEP, OrganismType.CYBER_SHEEP, OrganismType.BORSCH,
        OrganismType.BORSCH, OrganismType.WOLF, OrganismType.GUARANI
    ]

    def __init__(self, window: pygame.Surface, world, top_left: Point, board_position: tuple):
        super().__init__(window, world, top_left, board_position)

    def display(self):
        self.draw_window('Choose organism...')
        self.draw_organisms_list()
        self.draw_exit_button((self.top_left.x + self.width - 50, self.top_left.y + self.height - 50))

    def draw_organisms_list(self):
        text_position = Point(self.top_left.x, self.top_left.y + 50)
        gap = self.LIST_SIZE / len(self.list_of_organisms)
        organism_names = [organism.name for organism in self.list_of_organisms]
        super().draw_list(text_position, organism_names, gap)

    def is_position_on_choice_list(self, position: tuple):
        if self.top_left.x < position[0] < self.top_left.x + self.width \
                and self.top_left.y + 50 < position[1] < self.top_left.y + self.height - 50:
            return True
        else:
            return False

    def get_organism_on_position(self, position) -> OrganismType:
        gap = self.LIST_SIZE / len(self.list_of_organisms)
        choice_number = int((position[1] - self.top_left.y - 50) / gap)
        return self.list_of_organisms[choice_number]

    def delete_label(self):
        self.world.choice_list = None
        del self

    def handle_user_input(self, position: tuple):
        if self.is_position_on_exit(position):
            self.delete_label()
        elif self.is_position_on_choice_list(position):
            organism = self.get_organism_on_position(position)
            self.world.create_new_organism(organism, self.board_position)
            self.delete_label()
