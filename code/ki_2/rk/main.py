import pygame as pg
import random as rd
from math import pi, radians, sin
WIDTH = 800
HEIGHT = 600

BLUE = (145, 159, 245)
WHITE = (255, 255, 255)
W_WW = (244, 255, 255)
YELLOW = (239, 255, 0)
Y_B = (173, 216, 230)
SEA = (51, 0, 255)
BROWN = (117, 62, 20)
BLACK = (0, 0, 0)
GREY = (119, 119, 119)
RED = (245, 105, 180)
DARK_GREEN = (34, 139, 34)
SKY = (135, 206, 250)
GREEN = (60, 179, 113)
HOUSE = (204, 82, 0)
HOUSE1 = (200, 162, 200)



def draw_sky():
    pg.draw.rect(screen, WHITE, (0, 0, 800, 600))


def draw_sinnn():
    x = -50
    y = 280
    pg.draw.arc(screen, BLACK, (x, y, 50, 50), 0 , pi/2)
    pg.draw.arc(screen, BLACK, (x + 50, y, 50, 50), pi, 3*pi/2)
    pg.draw.arc(screen, BLACK, (x + 100, y, 50, 50), 3*pi/2, 2*pi)
    pg.draw.arc(screen, BLACK, (x + 150, y, 50, 50), pi/2, pi)
    pg.draw.arc(screen, BLACK, (x + 200, y, 50, 50), 0 , pi/2)
    pg.draw.arc(screen, BLACK, (x + 250, y, 50, 50), pi, 3*pi/2)
    pg.draw.arc(screen, BLACK, (x + 300, y, 50, 50), 3*pi/2, 2*pi)
    pg.draw.arc(screen, BLACK, (x + 350, y, 50, 50), pi/2, pi)
    pg.draw.arc(screen, BLACK, (x + 400, y, 50, 50), 0 , pi/2)
    pg.draw.arc(screen, BLACK, (x + 450, y, 50, 50), pi, 3*pi/2)
    pg.draw.arc(screen, BLACK, (x + 500, y, 50, 50), 3*pi/2, 2*pi)
    pg.draw.arc(screen, BLACK, (x + 550, y, 50, 50), pi/2, pi)

    
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('CAR AND SUN')
clock = pg.time.Clock()
screen.fill(WHITE)
pg.display.flip()
fi = float(input("Введите угол в градусах "))
fi = radians(fi)

    
x, y = WIDTH // 2, HEIGHT // 2
state = True
running = True
angle = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            
    draw_sky()
    draw_sinnn()

    y = 250 + sin(x / 10) * 25
    if x >= WIDTH - 100:
        state = False
    if x <= 0:
        state = True
    if state:
        x += 1
        angle -= fi
    else:
        x -= 1
        angle += fi
    y = int(y)
    pg.draw.arc(screen, RED, (x, y, 100, 100), 0 + angle, pi/2 + angle, 50)
    pg.draw.arc(screen, HOUSE1, (x, y, 100, 100), pi/2+ angle, pi+ angle, 50)
    pg.draw.arc(screen, DARK_GREEN, (x, y, 100, 100), pi+ angle, 3*pi/2+ angle, 50)
    pg.draw.arc(screen, BLUE, (x, y, 100, 100), 3*pi/2+ angle, 2*pi+ angle, 50)
      


    pg.display.update()
    clock.tick(90)