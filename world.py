from random import randint
from operator import attrgetter
from animals.human import Human
from animals.wolf import Wolf
from plants.grass import Grass
from plants.guarani import Guarani
from organism import Organism
from gui.board import BoardGUI
import copy

class World:
    SPECIES = [Grass, Guarani]  # Species available in the world
    CONCENTRATION = 100  # Organisms concentration

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.organisms = []
        self.round = 0
        self.rows = BoardGUI.BOARD_ROWS
        self.columns = BoardGUI.BOARD_COLUMNS
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def _sort_organisms(self):
        self.organisms = sorted(self.organisms, key=attrgetter('age'))
        self.organisms = sorted(self.organisms, key=attrgetter('initiative'), reverse=True)

    def get_human(self) -> Human | None:
        for organism in self.organisms:
            if organism.is_human:
                return organism
        return None

    def initialize(self):
        human = Human((randint(0, self.rows - 1), randint(0, self.columns - 1)), self)
        for x in range(self.rows):
            for y in range(self.columns):
                if human.position.x == x and human.position.y == y:
                    pass
                else:
                    if randint(0, 99) < self.CONCENTRATION:
                        self.create_random_organism((x, y))

    def another_round(self):
        self._sort_organisms()
        organisms = copy.copy(self.organisms)
        for organism in organisms:
            if organism.is_alive:
                organism.action()
                organism.collision()
        self.round += 1

    def add_to_remove_queue(self, organism):
        self.dead_organisms.append(organism)

    def clear_position(self, x: int, y: int):
        """This function clears the board position at given coordinates"""
        self.board[x][y] = None

    def remove_organisms(self):
        """This function removes all organisms from the board and class"""
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.organisms.clear()

    def create_random_organism(self, position: tuple):
        random_species = self.SPECIES[randint(0, len(self.SPECIES) - 1)]
        random_species(position, self)
        # return new_organism

    def get_organism_on_field(self, position: tuple) -> Organism | None:
        x, y = position
        return self.board[x][y]

    def is_field_empty(self, position):
        x, y = position
        if self.board[x][y] is None:
            return True
        else:
            return False

    def create_new_organism(self, name, position):
        if self.is_field_empty(position):
            if name == 'Grass':
                Grass(position, self)
            elif name == 'Wolf':
                Wolf(position, self)
            elif name == 'Guarani':
                Guarani(position, self)


if __name__ == "__main__":
    pass
