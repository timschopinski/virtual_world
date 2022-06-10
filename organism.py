import random

from utils.point import Point
from random import randint
from pygame import Surface
from typing import List
import copy


class Organism:
    def __init__(self, position: Point, world, *args, **kwargs):
        self.position = position
        self.world = world
        self.age = 0
        self.world.organisms.append(self)
        self.world.board[self.position.x][self.position.y] = self
        self.is_alive = True
        self.is_human = False
        self.strength = None
        self.chance_to_reproduce = None
        self.initiative = None
        self.AVATAR: Surface = NotImplemented
        self.AVATAR_WIDTH = None
        self.AVATAR_HEIGHT = None
        self.is_animal = False
        self.has_special_collision = False

    def eat_enemy(self, enemy: 'Organism'):
        """ Removes the enemy """
        if not enemy.is_alive:
            return
        self.world.organisms.remove(enemy)
        enemy.is_alive = False
        self.world.board[self.position.x][self.position.y] = self
        self.world.info.add_comment(
            f'{self}[{self.position.x}][{self.position.y}] ate a {enemy}[{enemy.position.x}][{enemy.position.y}]')
        del enemy

    def die(self, enemy: 'Organism'):
        """ Removes self from the board end organism list """
        if not self.is_alive:
            return
        self.is_alive = False
        self.world.organisms.remove(self)
        self.world.board[self.position.x][self.position.y] = enemy
        self.world.info.add_comment(
            f'{enemy}[{enemy.position.x}][{enemy.position.y}] ate a {self}[{self.position.x}][{self.position.y}]')
        del self

    def fight(self, enemy: 'Organism'):
        """ Compares self and enemies strengths and initiatives """
        if self.strength > enemy.strength:
            self.eat_enemy(enemy)
        elif self.strength < enemy.strength:
            self.die(enemy)
        else:
            if self.initiative > enemy.initiative:
                self.eat_enemy(enemy)
            else:
                self.die(enemy)

    def get_empty_field(self, position: Point) -> Point | None:
        """ Returns empty neighbor field """
        possible_positions: List[Point] = []
        if position.x > 0:
            if self.world.board[position.x-1][position.y] is None:
                possible_positions.append(Point((position.x-1, position.y)))
        if position.x < self.world.rows - 1:
            if self.world.board[position.x+1][position.y] is None:
                possible_positions.append(Point((position.x+1, position.y)))
        if position.y > 0:
            if self.world.board[position.x][position.y-1] is None:
                possible_positions.append(Point((position.x, position.y - 1)))
        if position.y < self.world.columns - 1:
            if self.world.board[position.x][position.y+1] is None:
                possible_positions.append(Point((position.x, position.y + 1)))
        if possible_positions:
            return random.choice(possible_positions)
        return None

    def reproduce(self, friend: 'Organism'):
        empty_field = self.get_empty_field(friend.position)
        if empty_field is not None:
            if randint(1, 100) < self.chance_to_reproduce:
                new_organism = self.__class__(empty_field, self.world)
                self.world.info.add_comment(
                    f'A baby {new_organism}[{new_organism.position.x}][{new_organism.position.y}] is born')

    def action(self):
        self.extra_action_behavior()
        self.age += 1

    def collision(self):
        pass

    def extra_collision_behavior(self, enemy):
        pass

    def extra_action_behavior(self):
        pass

    def draw(self):
        """this method draws the organism on the screen"""
        organism_position = ((self.position.y + 1) * self.world.field_width
                             - self.world.field_width / 2 - self.AVATAR_WIDTH / 2,
                             (self.position.x + 1) * self.world.field_height - self.AVATAR_HEIGHT)
        self.world.window.blit(self.AVATAR, organism_position)

    def remove_organism(self, removed_organism: 'Organism'):
        if not removed_organism.is_alive:
            return
        self.world.organisms.remove(removed_organism)
        removed_organism.is_alive = False
        self.world.board[removed_organism.position.x][removed_organism.position.y] = None
        del removed_organism

    def get_all_neighbours(self) -> List:
        """ Returns a list of all neighbour organisms """
        neighbour_organisms = []
        neighbour_field = copy.copy(self.position)

        if self.position.x > 0:
            neighbour_field.update(self.position.x - 1, self.position.y)
            neighbour_organisms.append(self.world.get_organism_on_field(neighbour_field))
        if self.position.x < self.world.rows - 1:
            neighbour_field.update(self.position.x + 1, self.position.y)
            neighbour_organisms.append(self.world.get_organism_on_field(neighbour_field))
        if self.position.y > 0:
            neighbour_field.update(self.position.x, self.position.y - 1)
            neighbour_organisms.append(self.world.get_organism_on_field(neighbour_field))
        if self.position.y < self.world.columns - 1:
            neighbour_field.update(self.position.x, self.position.y + 1)
            neighbour_organisms.append(self.world.get_organism_on_field(neighbour_field))
        return neighbour_organisms

    @staticmethod
    def get_description():
        return "This Organism has no additional skills."
