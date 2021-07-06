import pygame as pg
import random as rd
w = 800
h = 600
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
        
class Fish(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (200, 140))
        self.rect = self.image.get_rect(center=(x, 550))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

class Fish1(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (170, 140))
        self.rect = self.image.get_rect(center=(x, 320))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

class Fish2(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect(center=(x, 400))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

class Fish3(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (200, 140))
        self.rect = self.image.get_rect(center=(x, 480))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

class Bubble(pg.sprite.Sprite):
    def __init__(self, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(50, y))
    def update(self):
        if self.rect.y > h-260:
            self.rect.y -= 1
        else:
            self.rect.y = h
class Bubble1(pg.sprite.Sprite):
    def __init__(self, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(center=(500, y))
    def update(self):
        if self.rect.y > h-260:
            self.rect.y -= 1
        else:
            self.rect.y = h
class Bubble2(pg.sprite.Sprite):
    def __init__(self, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(700, y))
    def update(self):
        if self.rect.y > h-260:
            self.rect.y -= 1
        else:
            self.rect.y = h
class Bubble3(pg.sprite.Sprite):
    def __init__(self, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(350, y))
    def update(self):
        if self.rect.y > h-260:
            self.rect.y -= 1
        else:
            self.rect.y = h
class Bubble4(pg.sprite.Sprite):
    def __init__(self, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(200, y))
    def update(self):
        if self.rect.y > h-260:
            self.rect.y -= 1
        else:
            self.rect.y = h
def draw_sky():
    pg.draw.rect(screen, SKY, (0, 0, 800, 600 - 130))

def draw_sea():
    pg.draw.rect(screen, SEA, (0, 250, 800, 600 - 130))

def draw_sun():
    pg.draw.circle(screen, Y_B, (10, 10), 100)
    pg.draw.circle(screen, YELLOW, (10, 10), 40)         

def draw_cloud(start_x, w):
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 130), 25)

def draw_cloud1(start_x, w):
    pg.draw.ellipse(screen, W_WW, (start_x, 100, w, 60))
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 135), 20)

def draw_things():
    pg.draw.ellipse(screen, DARK_GREEN, (50, 500, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (50, 470, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (50, 440, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (50, 410, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (250, 500, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (250, 470, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (250, 440, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (250, 410, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (250, 380, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (450, 520, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (450, 490, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (450, 460, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (650, 460, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (650, 430, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (650, 400, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (650, 370, 20, 50))
    pg.draw.ellipse(screen, DARK_GREEN, (650, 340, 20, 50))
    pg.draw.circle(screen, BROWN, (50, h), 70)
    pg.draw.circle(screen, BROWN, (150, h), 80)
    pg.draw.circle(screen, BROWN, (w-150, h), 100)
    pg.draw.circle(screen, BROWN, (220, h), 70)
    pg.draw.circle(screen, BROWN, (440, h), 40)
    pg.draw.circle(screen, BROWN, (330, h), 100)
    pg.draw.circle(screen, BROWN, (500, h), 60)
    pg.draw.circle(screen, BROWN, (750, h), 70)
      
pg.init()
screen = pg.display.set_mode((w, h))
pg.display.set_caption('SEA AND SUN')
clock = pg.time.Clock()
screen.fill(SKY)
pg.display.flip()

def main():
    cstart = rd.randint(0, 200)
    cstart1 = rd.randint(200, 600)
    cstart2 = rd.randint(500, 800)
    cwidth = 250
    cwidth1 = 200
    cwidth2 = 200
    running = True
    fish = Fish(100, '1.png')
    fish1 = Fish1(100, 'Sprite-0001.png')
    fish2 = Fish2(100, 'l3.png')
    fish3 = Fish3(100, 'H11.png')
    bubble = Bubble(400, 'bubble-128px.png')
    bubble1 = Bubble1(400, 'bubble-128px.png')
    bubble2 = Bubble2(400, 'bubble-128px.png')
    bubble3 = Bubble3(400, 'bubble-128px.png')
    bubble4 = Bubble4(400, 'bubble-128px.png')
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                return
        draw_sky()
        draw_sun()
        draw_sea()
        draw_things()
        
        '''Отрисовка облаков(динамические объекты)'''
        draw_cloud(cstart, cwidth)
        draw_cloud1(cstart1, cwidth1)
        draw_cloud(cstart2, cwidth2)

        screen.blit(fish.image, fish.rect)
        screen.blit(fish1.image, fish1.rect)
        screen.blit(fish2.image, fish2.rect)
        screen.blit(fish3.image, fish3.rect)
        screen.blit(bubble.image, bubble.rect)
        screen.blit(bubble1.image, bubble1.rect)
        screen.blit(bubble2.image, bubble2.rect)
        screen.blit(bubble3.image, bubble3.rect)
        screen.blit(bubble4.image, bubble4.rect)

        '''Движение облаков'''
        cstart -= 1
        cstart1 -= 2
        cstart2 -= 1
        if cstart <= -250:
            cstart = w + 200
        if cstart1 <= -250:
            cstart1 = w + 200
        if cstart2 <= -250:
            cstart2 = w + 200

        '''Движение машины'''
        if fish.rect.x < w - 100:
            fish.rect.x += 1
        else:
            fish.rect.x = 0
        if fish1.rect.x > 0:
            fish1.rect.x -= 2
        else:
            fish1.rect.x = w
        if fish2.rect.x < w - 100:
            fish2.rect.x += 2
        else:
            fish2.rect.x = 0
        if fish3.rect.x > 0:
            fish3.rect.x -= 1
        else:
            fish3.rect.x = w
        if bubble.rect.y > h - 260:
            bubble.rect.y -= 1
        else:
            bubble.rect.y = h
        if bubble1.rect.y > h - 260:
            bubble1.rect.y -= 0.75
        else:
            bubble1.rect.y = h
        if bubble2.rect.y > h - 260:
            bubble2.rect.y -= 0.5
        else:
            bubble2.rect.y = h
        if bubble3.rect.y > h - 260:
            bubble3.rect.y -= 1.5
        else:
            bubble3.rect.y = h
        if bubble4.rect.y > h - 260:
            bubble4.rect.y -= 1.25
        else:
            bubble4.rect.y = h
        pg.display.update()
        clock.tick(90)
if __name__ == '__main__':
    main()
