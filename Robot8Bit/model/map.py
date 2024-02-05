from obstacle import Sea, Wall
from items import Potion, WaterPotion, Bomb, Diamond
from player import Player
import random


class Map:
    def __init__(self, archivo, size, num_diamond=3, num_water_potion=2, num_bomb=6, num_potion=2):
        self.diamonds = []
        self.player = None
        self.walls = []
        self.seas = []
        self.water_potions = []
        self.bombs = []
        self.potions = []
        self.size = size
        self.num_bombs = num_bomb
        self.num_water_potions = num_water_potion
        self.num_diamonds = num_diamond
        self.num_potions = num_potion
        self.load_mapa(archivo)

    def load_mapa(self, archivo):
        with open(archivo, 'r') as archivo:
            lines = archivo.readlines()

        self.rows = len(lines)
        self.columns = max(len(linea.strip()) for linea in lines)

        for row, linea in enumerate(lines):
            for column, character in enumerate(linea.strip()):
                character = lines[row][column]
                if character == 'W':
                    wall = Wall(row, column, self.size)
                    self.walls.append(wall)
                elif character == 'P':
                    self.player = Player(row, column, self.size)
                elif character == 'A':
                    sea = Sea(row, column, self.size)
                    self.seas.append(sea)

        diamond_add = 0
        while diamond_add < self.num_diamonds:
            row = random.randint(0, self.rows - 2)
            column = random.randint(0, self.columns - 1)
            if all(((row, column) not in (wall.position for wall in self.walls),
                    (row, column) != self.player.position,
                    (row, column) not in (diamond.position for diamond in self.diamonds))):
                diamond = Diamond(row, column, self.size)
                self.diamonds.append(diamond)
                diamond_add += 1

        water_potion_used = 0
        while water_potion_used < self.num_water_potions:
            row = random.randint(0, self.rows - 2)
            column = random.randint(0, self.columns - 1)
            if all(((row, column) not in (wall.position for wall in self.walls),
                    (row, column) != self.player.position,
                    (row, column) not in (diamonds.position for diamonds in self.diamonds),
                    (row, column) not in (water_potions.position for water_potions in self.water_potions),
                    (row, column) not in (seas.position for seas in self.seas))):
                water_potion = WaterPotion(row, column, self.size)
                self.water_potions.append(water_potion)
                water_potion_used += 1

        bomb_add = 0
        while bomb_add < self.num_bombs:
            row = random.randint(0, self.rows - 2)
            column = random.randint(0, self.columns - 1)
            if all(((row, column) not in (wall.position for wall in self.walls),
                    (row, column) != self.player.position,
                    (row, column) not in (diamond.position for diamond in self.diamonds),
                    (row, column) not in (water_potion.position for water_potion in self.water_potions),
                    (row, column) not in (bomb.position for bomb in self.bombs),
                    (row, column) not in (sea.position for sea in self.seas))):
                bomba = Bomb(row, column, self.size)
                self.bombs.append(bomba)
                bomb_add += 1

        add_potion = 0
        while add_potion < self.num_potions:
            row = random.randint(0, self.rows - 2)
            column = random.randint(0, self.columns - 1)
            if all(((row, column) not in (wall.position for wall in self.walls),
                    (row, column) != self.player.position,
                    (row, column) not in (diamond.position for diamond in self.diamonds),
                    (row, column) not in (water_potion.position for water_potion in self.water_potions),
                    (row, column) not in (bomb.position for bomb in self.bombs),
                    (row, column) not in (potion.position for potion in self.potions),
                    (row, column) not in (sea.position for sea in self.seas))):
                potion = Potion(row, column, self.size)
                self.potions.append(potion)
                add_potion += 1

    def add_wall(self, row, column):
        for wall in self.walls:
            if wall.row == row and wall.column == column:
                return wall
        return None

    def add_water_potion(self, row, column):
        for water_potion in self.water_potions:
            if water_potion.posicion == [row, column]:
                return water_potion
        return None

    def add_bomb(self, row, column):
        for bomb in self.bombs:
            if bomb.position == [row, column]:
                return bomb
        return None

    def destroyed_wall(self, wall):
        self.walls.remove(wall)
        print(wall.position)

    def quit_water_potion(self, water_potion):
        self.water_potions.remove(water_potion)

    def draw(self, screen):
        for walls in self.walls:
            walls.draw(screen)
        for diamonds in self.diamonds:
            diamonds.draw(screen)
        for sea in self.seas:
            sea.draw(screen)
        for water_potion in self.water_potions:
            water_potion.draw(screen)
        for bombs in self.bombs:
            bombs.draw(screen)
        for potions in self.potions:
            potions.draw(screen)
