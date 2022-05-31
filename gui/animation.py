from utils.point import Point
from typing import List
from pygame import Surface


class Animation:

    def __init__(self, sprites: List[Surface], position: Point, animation_time: int = 3):
        self.sprites = sprites
        self.position = position
        self.animation_time = animation_time
        self.animation_time_counter = 0
        self.animation_index = 0
        self.is_end_of_animation = False

    def draw(self, window: Surface):
        self.animation_cooldown()
        if self.animation_time_counter == 0:
            sprite = self.sprites[self.animation_index]
            window.blit(sprite, (self.position.x, self.position.y))
            self.animation_time_counter = 1
        if self.animation_index >= len(self.sprites) - 1:
            self.animation_index = 0
            self.animation_time_counter = 1
            self.sprites.clear()
            self.is_end_of_animation = True

    def animation_cooldown(self):
        if self.animation_time_counter >= self.animation_time:
            self.animation_time_counter = 0
            self.animation_index += 1
        elif self.animation_time_counter > 0:
            self.animation_time_counter += 1
