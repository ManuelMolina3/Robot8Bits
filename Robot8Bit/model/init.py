from game import Game

rows = 30
columns = 50
size = 30
map_link = 'map.txt'
background_image_link = 'assets/background.jpg'

game = Game(rows, columns, size, map_link, background_image_link)

while True:
    game.run(size)

    if game.reboot:
        game.reboot = False
        game = Game(rows, columns, size, map_link, background_image_link)
        game.run(size)
    else:
        break
