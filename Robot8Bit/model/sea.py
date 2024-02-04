import pygame


class Sea(pygame.sprite.Sprite):
    def __init__(self, row, column, size):
        super().__init__()
        self.image = pygame.image.load("../assets/wallsAndWater/Water.jpg").convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = column * size
        self.rect.y = row * size
        self.row = row
        self.column = column
        self.posicion = (row, column)

    def dibujar(self, screen):
        screen.blit(self.image, self.rect)
