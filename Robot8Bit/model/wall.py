import pygame
from config import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, row, column, size):
        super().__init__()
        self.image = pygame.image.load("../assets/wallsAndWater/wall.jpg").convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = column * size
        self.rect.y = row * size
        self.row = row
        self.column = column
        self.position = (row, column)
        self.size = size
        self.hitbox = (self.position[0], self.position[1], self.size[0], self.size[1])

    def dibujar(self, screen):
        screen.blit(self.image, self.rect)
