import pygame
import time
import math
pygame.init()
screen=pygame.display.set_mode((500,600))
GREY=(120,120,120)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

font=pygame.font.SysFont('sans',50)

text_1=font.render('+',True,BLACK)
text_2=font.render('-',True,BLACK)
text_3=font.render('+',True,BLACK)
text_4=font.render('-',True,BLACK)
text_5=font.render('Start',True,BLACK)
text_6=font.render('Reset',True,BLACK)

total_secs=0
total=0
is_start=False
secs=0
mins=0
running=True

r_sec=90
r_min=50

clock=pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREY)
    sound=0

    mouse_x,mouse_y=pygame.mouse.get_pos();

    #draw buttons
    pygame.draw.rect(screen, WHITE,(100,50,50,50))
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))

    #draw text
    screen.blit(text_1,(100,50))
    screen.blit(text_2, (100, 200))
    screen.blit(text_3, (200, 50))
    screen.blit(text_4, (200, 200))
    screen.blit(text_5, (300, 50))
    screen.blit(text_6, (300, 150))

    #draw progress bar
    pygame.draw.rect(screen, BLACK , (50, 520, 400, 50))
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pygame.mixer.pause()
                if (100<mouse_x<150) and(50<mouse_y<100):
                    total_secs+=60
                    total=total_secs
                    print('press + minutes')
                if (100<mouse_x<150) and(200<mouse_y<250):
                    total_secs-=60
                    total=total_secs
                    print('press - minutes')
                if (200<mouse_x<250) and(50<mouse_y<100):
                    total_secs+=1
                    total=total_secs
                    print('press + second')
                if (200<mouse_x<250) and(200<mouse_y<250):
                    total_secs-=1
                    total=total_secs
                    print('press - second')
                if (300<mouse_x<400) and(50<mouse_y<100):
                    is_start=True
                    total=total_secs
                    print('total_secs: '+str(total_secs))
                    print('press Start')
                if (300<mouse_x<400) and(150<mouse_y<200):
                    total_secs=0
                    is_start=False
                    print('press Reset')

    if is_start:
        total_secs-=1
        if total_secs==0:
            print('Het Gio')
            pygame.mixer.Sound.play(sound)
        time.sleep(0.03)

    if total_secs <0:
        is_start=False
        total_secs=0
        total=0

    secs=total_secs%60
    mins=(total_secs-secs)/60
    mins=int(mins)
    time_str=str(mins)+' : '+str(secs)

    text_min=font.render(time_str,True,BLACK)
    screen.blit(text_min,(120,120))

    #draw clock
    pygame.draw.circle(screen, BLACK, (250,400),100)
    pygame.draw.circle(screen, WHITE, (250,400),95)
    pygame.draw.circle(screen, BLACK, (250,400),5)

    #draw kim
    pygame.draw.line(screen, BLACK, (250,400),(int(250+90*math.sin(6*secs*math.pi/180)),int(400-90*math.cos(6*secs*math.pi/180))))
    pygame.draw.line(screen, RED, (250, 400), (int(250+40*math.sin(6*mins*math.pi/180)), int(400-40*math.cos(6*mins*math.pi/180))))

    if total !=0:
        pygame.draw.rect(screen,RED,(60,530,380*int((total_secs/total)),30))

    pygame.display.flip()

pygame.quit()
