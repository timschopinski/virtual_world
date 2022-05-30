import os
from utils.color import Color
from gui.world_gui import WorldGUI
from utils.type import OrganismType
from utils.point import Point
from typing import List


class Load:

    def __init__(self, file_path):
        self.file_path = os.path.join("storage/saves/", file_path)

    @staticmethod
    def _get_colors_from_world_data(data: List) -> tuple:
        """ converts two strings and returns as color tuples """
        data.remove('\n')
        data = data[3:]
        for index, number in enumerate(data):
            if '(' in number:
                number = number[1:]
            elif')' in number:
                number = number[:len(number) - 1]
            if',' in number:
                number = number[:len(number) - 1]
            data[index] = int(number)
        color1 = tuple(data[:3])
        color2 = tuple(data[3:])
        return color1, color2

    def is_path_valid(self):
        """ Returns True if the file exists """
        return os.path.exists(self.file_path)

    def initialize(self):
        """ Loads the world state from a file """
        world = WorldGUI()
        with open(file=self.file_path, mode="r") as f:
            world_data = f.readline().split(' ')
            Color.BOARD_COLOR_1, Color.BOARD_COLOR_2 = self._get_colors_from_world_data(world_data)
            world_data = world_data[:3]
            rows, columns, round_number = tuple(world_data)
            world.load_world(int(rows), int(columns), int(round_number))
            while organism_data := f.readline().split(' '):
                if len(organism_data) == 1:  # last empty line
                    break
                organism_data.remove('\n')
                organism_type, x, y, age, strength, initiative = tuple(organism_data)
                loaded_organism = world.create_new_organism(OrganismType.get_organism_type(organism_type),
                                                            Point(int(x), int(y)))
                loaded_organism.strength = int(strength)
                loaded_organism.age = int(age)
                loaded_organism.initiative = int(initiative)

        world.display()
