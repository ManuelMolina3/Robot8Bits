import pygame


player_stay = pygame.image.load("../assets/player/PlayerStay.jpg")
player_right = pygame.image.load("../assets/player/PlayerRightWalk1.jpg")
player_left = pygame.image.load("../assets/player/PlayerLeftWalk1.jpg")
player_up = pygame.image.load("../assets/player/PlayerWalk1.jpg")
player_down = pygame.image.load("../assets/player/PlayerWalk1.jpg")
player_water = pygame.image.load("../assets/player/playerWater.png")


class Player(pygame.sprite.Sprite):
    def __init__(self, row, column, size):
        super().__init__()
        self.image = player_stay
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.position = [row, column]
        self.life = 10
        self.parpadear = False
        self.tiempo_parpadeo = 0
        self.water_potions = []
        self.diamonds = []
        self.bombs = []
        self.potions = []
        self.water_potion_effect = False

    def movement(self, direction, mapa, size):
        new_position = self.position.copy()

        if direction == "up" and new_position[0] > 0:
            new_position[0] -= 1
            self.image = player_up
            self.image = pygame.transform.scale(self.image, (size, size))
        elif direction == "down" and new_position[0] < mapa.rows - 1:
            new_position[0] += 1
            self.image = player_down
            self.image = pygame.transform.scale(self.image, (size, size))
        elif direction == "left" and new_position[1] > 0:
            new_position[1] -= 1
            self.image = player_left
            self.image = pygame.transform.scale(self.image, (size, size))
        elif direction == "right" and new_position[1] < mapa.columns - 1:
            new_position[1] += 1
            self.image = player_right
            self.image = pygame.transform.scale(self.image, (size, size))

        for water in mapa.water:
            if new_position == [water.fila, water.columna]:
                if self.water_potion_effect:
                    self.image = player_water
                    self.image = pygame.transform.scale(self.image, (size, size))
                else:
                    self.life -= 2
                    print("Life:", self.life)
                break
            if self.position == [water.row, water.column] and new_position not in [(w.row, w.column) for w in
                                                                                   mapa.water]:
                if self.water_potion_effect:
                    self.quit_water_potion()
                    self.water_potion_effect = False
                break
        if new_position not in [(diamond.posicion[0], diamond.posicion[1]) for diamond in mapa.diamonds]:
            for wall in mapa.wall:
                if new_position == [wall.row, wall.column]:
                    self.life -= 1
                    print("¡Chocaste con un obstáculo! Vidas restantes:", self.life)
                    return
            self.position = new_position

    def add_diamonds(self, mapa):
        for diamond in mapa.diamonds:
            if self.position == diamond.position:
                mapa.diamonds.remove(diamond)
                self.diamonds.append(diamond)
                print(len(mapa.diamonds))
                break

    def add_water_potions(self, mapa):
        for water_potion in mapa.water_potions:
            if self.position == water_potion.position:
                mapa.water_potions.remove(water_potion)
                self.water_potions.append(water_potion)
                print(len(self.water_potions))
                break

    def add_bomb(self, mapa):
        for bomb in mapa.bombs:
            if self.position == bomb.position:
                mapa.bombs.remove(bomb)
                self.bombs.append(bomb)
                print(len(self.bombs))
                break

    def add_potion(self, mapa):
        for potion in mapa.potions:
            if self.position == potion.position:
                mapa.potions.remove(potion)
                self.potions.append(potion)
                print(len(self.potions))
                break

    def potion_water_taken(self):
        if self.water_potions:
            state_actual = self.water_potions.pop(0)
            if not state_actual.usado:
                self.water_potion_effect = True
                print("Estás usando un traje de agua")
            else:
                print("Este traje de agua ya ha sido usado.")
        else:
            print("No tienes trajes de agua disponibles.")

    def quit_water_potion(self):
        state_not_actual = [state for state in self.water_potions if not state.actual]
        if state_not_actual:
            state = state_not_actual.pop(0)
            state.actual = True

    def explode_bombs(self, mapa):
        if self.bombs:
            bomb = self.bombs.pop(0)
            bomb.explotar(mapa)

    def potion_taken(self):
        if self.potions:
            if self.life >= 10:
                print("Ya tienes la vida al máximo")
            else:
                self.life = min(10, self.life + 5)
                self.potions.remove(self.potions[0])
                print("Tomaste una poción. Vidas restantes:", self.life)
        else:
            print("No tienes pociones disponibles.")

    def check_win(self, mapa):
        return len(mapa.diamonds) == 0