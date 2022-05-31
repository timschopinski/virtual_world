from utils.point import Point
from random import randint
from pygame import Surface


class Organism:
    def __init__(self, position: Point, world, *args, **kwargs):
        self.position = position
        self.world = world
        self.age = 0
        self.world.organisms.append(self)
        self.world.board[self.position.x][self.position.y] = self
        self.chance_to_reproduce = 50
        self.is_alive = True
        self.is_human = False
        self.strength = None
        self.initiative = None
        self.AVATAR: Surface = NotImplemented
        self.AVATAR_WIDTH = None
        self.AVATAR_HEIGHT = None
        self.is_animal = None

    def eat_enemy(self, enemy: 'Organism'):
        """ Removes the enemy """
        self.world.organisms.remove(enemy)
        enemy.is_alive = False
        self.world.board[self.position.x][self.position.y] = self
        self.world.info.add_comment(
            f'{self}[{self.position.x}][{self.position.y}] ate a {enemy}[{enemy.position.x}][{enemy.position.y}]')
        del enemy

    def die(self, enemy: 'Organism'):
        """ Removes self """
        self.is_alive = False
        self.world.organisms.remove(self)
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

    def get_empty_field(self, friend: 'Organism') -> tuple:
        """ Returns empty neighbor field """
        if friend.position.x > 0:
            if self.world.board[friend.position.x-1][friend.position.y] is None:
                return friend.position.x-1, friend.position.y
        elif friend.position.x < self.world.rows - 1:
            if self.world.board[friend.position.x+1][friend.position.y] is None:
                return friend.position.x+1, friend.position.y
        elif friend.position.y > 0:
            if self.world.board[friend.position.x][friend.position.y-1] is None:
                return friend.position.x, friend.position.y - 1
        elif friend.position.y < self.world.columns - 1:
            if self.world.board[friend.position.x][friend.position.y+1] is None:
                return friend.position.x, friend.position.y + 1
        return None, None

    def reproduce(self, friend):
        new_organism_x, new_organism_y = self.get_empty_field(friend)
        if new_organism_x is not None and new_organism_y is not None:
            if randint(1, 100) < self.chance_to_reproduce:
                new_organism = self.__class__(Point(new_organism_x, new_organism_y), self.world)
                self.world.info.add_comment(
                    f'A baby {new_organism}[{new_organism.position.x}][{new_organism.position.y}] is born')

    def action(self):
        self.age += 1

    def collision(self):
        pass

    def draw(self):
        """this method draws the organism on the screen"""
        organism_position = ((self.position.y + 1) * self.world.field_width
                             - self.world.field_width / 2 - self.AVATAR_WIDTH / 2,
                             (self.position.x + 1) * self.world.field_height - self.AVATAR_HEIGHT)
        self.world.window.blit(self.AVATAR, organism_position)

    @staticmethod
    def get_description():
        return "This Organism has no additional skills."
