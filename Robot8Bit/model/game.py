import pygame
from player import Player
from config import *
import sys
from ground import Ground
from wall import Wall
from sea import Sea


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    mapa_elegido = 'map.txt'

    def create_map(self):
        for i, row in enumerate(self.mapa):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Wall(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "W":
                    Sea(self, j, i)

    def cargar_mapa(mapa):
        with open('map.txt', 'r') as archivo:
            primera_linea = archivo.readline().strip().split(', ')
            diccionario = {item.split(':')[0]: int(item.split(':')[1]) for item in primera_linea}
            contenido = [linea.strip() for linea in archivo]

        return diccionario, contenido

    objetos, mapa = cargar_mapa(mapa_elegido)
    print(objetos)

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.block = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screem(self):
        pass


g = Game()
g.intro_screem()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()
