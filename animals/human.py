from animal import Animal
from utils.direction import Direction
import pygame
import os


class Human(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        print(world.__class__)
        self.HUMAN_SIZE_WIDTH = self.world.field_width * 2
        self.HUMAN_SIZE_HEIGHT = self.world.field_height
        self.strength = 5
        self.is_human = True
        self.initiative = 4
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "human_2.png")),
                                             (self.HUMAN_SIZE_WIDTH, self.HUMAN_SIZE_HEIGHT))

    def __str__(self):
        return 'Human'

    def draw(self):
        organism_position = (self.position.y * self.world.field_width - self.world.field_height
                             / 2, self.position.x * self.world.field_height + 5)
        self.world.window.blit(self.AVATAR, organism_position)

    def set_direction(self, direction: int):
        self.direction = direction

    def action(self):
        self.age += 1
        self.world.clear_position(self.position.x, self.position.y)
        if self.direction == Direction.UP.value:
            self.move_up()
        elif self.direction == Direction.DOWN.value:
            self.move_down()
        elif self.direction == Direction.RIGHT.value:
            self.move_right()
        elif self.direction == Direction.LEFT.value:
            self.move_left()

    def unset_direction(self):
        self.direction = None

    @staticmethod
    def get_description():
        return """Unlike animals the direction of his movement is determined by the use of keyboard arrows before the start of the turn. Human also has a special skill which can be activated with a P button."""
