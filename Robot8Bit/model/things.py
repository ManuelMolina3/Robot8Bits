import pygame
import random
from model.wall import Wall

water_protected = pygame.image.load("")
bomb = pygame.image.load("")
diamond = pygame.image.load("")


class Things:
    def __init__(self, sprite, position, size):
        self.sprite = sprite
        self.position = position
        self.size = size
        self.hitbox = (self.position[0], self.position[1], self.size[0], self.size[1])
        self.recollected = False


class WaterPotion(Things):
    def __init__(self, position):
        super().__init__(water_protected, position, [42, 48])


class Bomb(Things):
    def __init__(self, position):
        super().__init__(bomb, position, [50, 50])
        self.radius_damage = (self.position[0] - 50, self.position[1] - 50, self.size[0] * 3, self.size[1] * 3)

    def destroyed_wall(self, wall):
        if isinstance(wall, Wall):
            self.radius_damage = (self.position[0] - 50, self.position[1] - 50, self.size[0] * 3, self.size[1] * 3)
            bomb_damage_radius_rect = pygame.Rect(self.radius_damage)
            wall_rect = pygame.Rect(wall.hitbox)
            return bomb_damage_radius_rect.colliderect(wall_rect)


class Diamond(Things):
    def __init__(self, position):
        super().__init__(diamond, position, [42, 48])
