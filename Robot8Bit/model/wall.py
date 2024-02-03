import pygame
from config import *

wall_img = pygame.image.load("")


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.sprite = wall_img
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
