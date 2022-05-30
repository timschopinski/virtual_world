import os
import pygame_menu
from gui.world_gui import WorldGUI
from utils.type import OrganismType
from utils.point import Point

class Load:

    def __init__(self, file_path):
        self.file_path = os.path.join("storage/saves/", file_path)

    def is_path_valid(self):
        return os.path.exists(self.file_path)

    def initialize(self):
        """ Loads the world state from a file """
        world = WorldGUI()
        with open(file=self.file_path, mode="r") as f:
            world_data = f.readline().split(' ')
            world_data.remove('\n')
            rows, columns, round_number = tuple(world_data)
            world.load_world(int(rows), int(columns), int(round_number))
            while organism_data := f.readline().split(' '):
                print(len(organism_data))
                if len(organism_data) == 1: # last empty line
                    break
                organism_data.remove('\n')
                organism_type, x, y, age, strength, initiative = tuple(organism_data)
                world.create_new_organism(OrganismType.get_organism_type(organism_type), Point(int(x), int(y)))

        world.display()

        #     for world_data in self.world_state['world'].values():
        #         f.write(str(world_data))
        #         f.write(' ')
        #     f.write('\n')
        #     for organisms in self.world_state['organisms']:
        #         for organism_data in organisms.values():
        #             f.write(str(organism_data))
        #             f.write(' ')
        #         f.write('\n')
