import pygame

wall_img = pygame.image.load("../assets/wallsAndWater/wall.jpg")
sea_img = pygame.image.load("../assets/wallsAndWater/Water.jpg")


class Obstacle:

    def __init__(self, sprite, row, column, size):
        self.sprite = sprite
        self.image = pygame.transform.scale(self.sprite, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = column * size
        self.rect.y = row * size
        self.row = row
        self.column = column
        self.position = (row, column)


class Wall(Obstacle):
    def __init__(self, row, column, size):
        super().__init__(wall_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class Sea(Obstacle):
    def __init__(self, row, column, size):
        super().__init__(sea_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))
