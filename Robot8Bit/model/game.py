import pygame
import sys

from map import Map
from config import *


class Game:
    def __init__(self, row, column, size, link_map, background_link):
        pygame.init()
        self.rows = row
        self.columns = column
        self.size = size
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((column * size, row * size + 30))
        self.playing = True
        self.reboot = False
        pygame.display.set_caption("Hero Game")
        self.map = Map(link_map, size)
        self.background = pygame.image.load(background_link)
        self.background = pygame.transform.scale(self.background, (column * size, row * size))

    def draw_info(self):
        font = pygame.font.Font(None, 24)

        bomb_img = pygame.image.load("../assets/potions/bomb.png")
        bomb_img = pygame.transform.scale(bomb_img, (self.size // 2, self.size // 2))

        self.screen.blit(bomb_img, (160, self.rows * self.size + 5))

        bomb_text = font.render(f" {len(self.map.player.bombas)}", True, BLACK)
        self.screen.blit(bomb_text, (175, self.rows * self.size + 5))

        life_img = pygame.image.load("../assets/Heart.jpg")
        life_img = pygame.transform.scale(life_img, (self.size // 2, self.size // 2))

        self.screen.blit(life_img, (55, self.rows * self.size + 5))

        life_text = font.render(f" {self.map.player.life}", True, BLACK)
        self.screen.blit(life_text, (70, self.rows * self.size + 5))

        water_potion_img = pygame.image.load("../assets/")
        water_potion_img = pygame.transform.scale(water_potion_img, (self.size // 2, self.size // 2))

        self.screen.blit(water_potion_img, (110, self.rows * self.size + 5))

        water_potion_text = font.render(f" {len(self.map.player.water_potions)}", True, BLACK)
        self.screen.blit(water_potion_text, (125, self.rows * self.size + 5))

        potion_img = pygame.image.load("../assets/potions/Potion.jpg")
        potion_img = pygame.transform.scale(potion_img, (self.size // 2, self.size // 2))

        self.screen.blit(potion_img, (210, self.rows * self.size + 5))

        potion_text = font.render(f" {len(self.map.player.pociones)}", True, BLACK)
        self.screen.blit(potion_text, (225, self.rows * self.size + 5))

        diamond_img = pygame.image.load("../assets/Diamod.jpg")
        diamond_img = pygame.transform.scale(diamond_img, (self.size // 2, self.size // 2))

        self.screen.blit(diamond_img, (10, self.rows * self.size + 5))

        diamond_text = font.render(f" {len(self.map.player.diamonds)}", True, BLACK)
        self.screen.blit(diamond_text, (25, self.rows * self.size + 5))

    def game_over(self):
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Game Over!", True, RED)
        self.screen.blit(game_over_text,
                         (self.columns * self.size // 2 - 200, self.rows * self.size // 2))
        pygame.display.flip()
        pygame.time.wait(1500)

    def winner_message(self):
        font = pygame.font.Font(None, 50)
        winner_text = font.render("Congratulation, You are winner!", True, RED)
        self.screen.blit(winner_text,
                         (self.columns * self.size // 2 - 150, self.rows * self.size // 2))
        pygame.display.flip()
        pygame.time.wait(1500)

    def reboot_screem(self):
        reboot_text = "Press 'R' for reboot o 'Q' for exit."
        font = pygame.font.Font(None, 30)
        reboot_text = font.render(reboot_text, True, RED)
        self.screen.blit(reboot_text,
                         (self.columns * self.size // 2 - 200, self.rows * self.size // 2 + 50))
        pygame.display.flip()

        self.playing = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reboot = True
                        return
                    elif event.key == pygame.K_q:
                        self.exit_game()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self, size):
        winner = False

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.map.player.movement("up", self.map, size)
            elif keys[pygame.K_DOWN]:
                self.map.player.movement("down", self.map, size)
            elif keys[pygame.K_LEFT]:
                self.map.player.movement("left", self.map, size)
            elif keys[pygame.K_RIGHT]:
                self.map.player.movement("right", self.map, size)

            if keys[pygame.K_t]:
                self.map.player.potion_water_taken()

            if keys[pygame.K_b]:
                self.map.player.explode_bombs(self.map)

            if keys[pygame.K_p]:
                self.map.player.potion_taken()

            self.map.player.add_diamonds(self.map)
            self.map.player.add_water_potions(self.map)
            self.map.player.add_bomb(self.map)
            self.map.player.add_potion(self.map)

            if len(self.map.player.diamonds) >= self.map.num_diamonds:
                winner = True
                self.playing = False

            if self.map.player.life <= 0:
                print("You haven´t more lives! Game over!.")
                self.playing = False

            self.screen.fill(WHITE)
            self.screen.blit(self.background, (0, 0))
            self.map.draw(self.screen)
            self.screen.blit(self.map.player.image,
                             (self.map.player.position[1] * self.size,
                              self.map.player.position[0] * self.size))

            self.draw_info()

            pygame.display.flip()

            self.clock.tick(10)

        if winner:
            self.winner_message()
            self.reboot_screem()
        else:
            self.game_over()
            self.reboot_screem()
