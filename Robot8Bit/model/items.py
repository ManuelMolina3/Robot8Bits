import pygame

potion_img = pygame.image.load("../assets/potions/potion.png")
bomb_img = pygame.image.load("../assets/potions/bomb.png")
water_potion_img = pygame.image.load("../assets/potions/water_potion.png")
diamond_img = pygame.image.load("../assets/Diamod.jpg")


class Item:

    def __init__(self, sprite, row, column, size):
        self.sprite = sprite
        self.image = pygame.transform.scale(self.sprite, (size, size))
        self.rect = self.image.get_rect()
        self.position = [row, column]
        self.size = size


class Potion(Item):
    def __init__(self, row, column, size):
        super().__init__(potion_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class WaterPotion(Item):
    def __init__(self, row, column, size):
        super().__init__(water_potion_img, row, column, size)
        self.used = False

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class Bomb(Item):
    def __init__(self, row, column, size):
        super().__init__(bomb_img, row, column, size)

    def destroy_wall(self, mapa, position):
        scope = [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1)
        ]

        for row, column in scope:
            if 0 <= row < mapa.row and 0 <= column < mapa.columns:
                wall = mapa.add_wall(row, column)
                if wall:
                    mapa.destroyed_wall(wall)
                bomba = mapa.add_bomb(row, column)
                if bomba:
                    bomba.explotar(map, position)

    def draw(self, screen):
        screen.blit(self.image, (self.position[1] * self.rect.width, self.position[0] * self.rect.height))


class Diamond(Item):
    def __init__(self, row, column, size):
        super().__init__(diamond_img, row, column, size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
