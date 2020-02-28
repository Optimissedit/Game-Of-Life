import pygame as pg

pg.init()

# COLORS
WHITE = (255, 255, 255)
RED = (255, 20, 20)
BLUE = (0, 0, 255)

# Set up display window
size = (500, 500)
screen = pg.display.set_mode(size)
pg.display.set_caption("Pygame of Life")

# Set to represent all currently living cells
world = {(250, 250)}

# List of objects to be drawn to screen
draw_list = []

# Boolean variable to control main loop
clock = pg.time.Clock()


def get_world_rect():
    for point in world:
        temp = pg.Rect(point, (1, 1))
        draw_list.append(temp)


def main(running):
    while(running):
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

pg.quit()
