from random import randint
from operator import attrgetter
from animals.human import Human
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.cyber_sheep import CyberSheep
from animals.antelope import Antelope
from animals.turtle import Turtle
from animals.fox import Fox
from plants.grass import Grass
from plants.guarani import Guarani
from plants.borsch import Borsch
from plants.dandelion import Dandelion
from plants.wild_berries import WildBerries
from organism import Organism
from gui.board import BoardGUI
import copy
from utils.point import Point
from utils.type import OrganismType


class World:
    SPECIES = [Grass, Guarani, Sheep, Wolf, Borsch, CyberSheep, WildBerries, Fox, Antelope, Turtle, Dandelion]  # Species available in the world
    CONCENTRATION = 100  # Organisms concentration

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.organisms = []
        self.round = 0
        self.rows = BoardGUI.BOARD_ROWS
        self.columns = BoardGUI.BOARD_COLUMNS
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def _remove_all_organisms(self):
        """This function removes all organisms from the board and class"""
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.organisms.clear()

    def _sort_organisms(self):
        self.organisms = sorted(self.organisms, key=attrgetter('age'), reverse=True)
        self.organisms = sorted(self.organisms, key=attrgetter('initiative'), reverse=True)

    def load_world(self, rows: int, columns: int, round_number: int):
        self.rows = rows
        self.columns = columns
        self.round = round_number
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def get_human(self) -> Human | None:
        for organism in self.organisms:
            if organism.is_human:
                return organism
        return None

    def initialize(self):
        self._remove_all_organisms()
        human = Human(Point(randint(0, self.rows - 1), randint(0, self.columns - 1)), self)
        for x in range(self.rows):
            for y in range(self.columns):
                if human.position.x == x and human.position.y == y:
                    pass
                else:
                    if randint(0, 99) < self.CONCENTRATION:
                        self.create_random_organism(Point(x, y))

    def another_round(self):
        self._sort_organisms()
        organisms = copy.copy(self.organisms)
        for organism in organisms:
            if organism.is_alive:
                organism.action()
                organism.collision()
        self.round += 1

    def clear_position(self, x: int, y: int):
        """This function clears the board position at given coordinates"""
        self.board[x][y] = None

    def remove_organism_on_field(self, position: Point):
        dead_organism = self.get_organism_on_field(position)
        self.organisms.remove(dead_organism)
        dead_organism.is_alive = False
        self.board[position.x][position.y] = None
        del dead_organism

    def create_random_organism(self, position: Point):
        random_species = self.SPECIES[randint(0, len(self.SPECIES) - 1)]
        random_species(position, self)
        # return new_organism

    def get_organism_on_field(self, position: Point) -> Organism | None:
        return self.board[position.x][position.y]

    def is_field_empty(self, position: Point):
        if self.board[position.x][position.y] is None:
            return True
        else:
            return False

    def create_new_organism(self, organism_type: OrganismType, position: Point):
        new_organism = None
        if self.is_field_empty(position):
            if organism_type == OrganismType.HUMAN:
                new_organism = Human(position, self)
            elif organism_type == OrganismType.WOLF:
                new_organism = Wolf(position, self)
            elif organism_type == OrganismType.SHEEP:
                new_organism = Sheep(position, self)
            elif organism_type == OrganismType.CYBER_SHEEP:
                new_organism = CyberSheep(position, self)
            elif organism_type == OrganismType.FOX:
                new_organism = Fox(position, self)
            elif organism_type == OrganismType.ANTELOPE:
                new_organism = Antelope(position, self)
            elif organism_type == OrganismType.TURTLE:
                new_organism = Turtle(position, self)
            elif organism_type == OrganismType.GRASS:
                new_organism = Grass(position, self)
            elif organism_type == OrganismType.GUARANI:
                new_organism = Guarani(position, self)
            elif organism_type == OrganismType.BORSCH:
                new_organism = Borsch(position, self)
            elif organism_type == OrganismType.DANDELION:
                new_organism = Dandelion(position, self)
            elif organism_type == OrganismType.WILD_BERRIES:
                new_organism = WildBerries(position, self)
        return new_organism


if __name__ == "__main__":
    pass
