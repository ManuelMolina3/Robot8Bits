import pygame
from wall import Wall

potion_img = pygame.image.load("../assets/potions/Potion.jpg")
bomb_img = pygame.image.load("../assets/potions/bomb.png")
water_potion_img = pygame.image.load("../assets/potions/water_potion.jpg")
diamond_img = pygame.image.load("../assets/Diamod.jpg")


class Item:

    def __init__(self, sprite, row, column, size):
        self.sprite = sprite
        self.image = pygame.transform.scale(self.sprite, (size, size))
        self.rect = self.image.get_rect()
        self.position = [row, column]
        self.size = size
        self.hitbox = (self.position[0], self.position[1], self.size[0], self.size[1])


class Potion(Item):
    def __init__(self, row, column, size):
        super().__init__(potion_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class WaterPotion (Item):
    def __init__(self, row, column, size):
        super().__init__(water_potion_img, row, column, size)
        self.used = False

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class Bomb(Item):
    def __init__(self, row, column, size):
        super().__init__(bomb_img, row, column, size)
        self.radius_damage = (self.position[0] - 50, self.position[1] - 50, self.size[0] * 3, self.size[1] * 3)

    def destroy_wall(self, wall):
        if isinstance(wall, Wall):
            self.radius_damage = (self.position[0] - 50, self.position[1] - 50, self.size[0] * 3, self.size[1] * 3)
            bomb_damage_radius_rect = pygame.Rect(self.radius_damage)
            wall_rect = pygame.Rect(wall.hitbox)
            return bomb_damage_radius_rect.colliderect(wall_rect)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class Diamond(Item):
    def __init__(self, row, column, size):
        super().__init__(diamond_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
