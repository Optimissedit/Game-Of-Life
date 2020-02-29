import pygame as pg
from cell import Cell

pg.init()

# COLORS
WHITE = (255, 255, 255)
RED = (255, 20, 20)
BLUE = (0, 0, 255)

# Set up display window
size = (800, 800)
screen = pg.display.set_mode(size)
pg.display.set_caption("Pygame of Life")

# Set to represent all currently living cells
world = {Cell(400, 400, 4), Cell(404, 400, 4), Cell(400, 404, 4), Cell(404, 408, 4)}

# List of objects to be drawn to screen
draw_list = []

# Boolean variable to control main loop
clock = pg.time.Clock()

# Size of cells, also amount to add/subtract to find neighbors


def get_world_rect():
    for obj in world:
        temp = pg.Rect((obj.x, obj.y), (obj.size, obj.size))
        draw_list.append(temp)


def main(running):
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(20)
        screen.fill(WHITE)
        pg.event.pump()

        get_world_rect()

        for cell in draw_list:
            pg.draw.rect(screen, RED, cell)

        pg.display.flip()


main(1)

# Testing finding neighbors
for val in world:
    test = val.get_neighbors()
    break
for cell in test:
    print(cell)

pg.quit()
