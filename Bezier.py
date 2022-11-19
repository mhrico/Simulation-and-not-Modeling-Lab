import pygame
from pygame.locals import *

size = width, height = (1200, 800)
speed = 0.0005
t = 0

path_position = [
    (100.0, 500.0),
    (200.0, 100.0),
    (600.0, 80.0),
    (650.0, 410.0)
]

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bezier Curve')

screen.fill((255, 255, 255))
pygame.display.update()

font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

p0 = path_position[0]
p1 = path_position[1]
p2 = path_position[2]
p3 = path_position[3]

text1 = font.render('P0', True, (0,0,0), None)
text2 = font.render('P1', True, (0,0,0), None)
text3 = font.render('P3', True, (0,0,0), None)
text4 = font.render('P4', True, (0,0,0), None)

text1_rect = text1.get_rect()
text2_rect = text2.get_rect()
text3_rect = text3.get_rect()
text4_rect = text4.get_rect()

text1_rect.center = p0
text2_rect.center = p1
text3_rect.center = p2
text4_rect.center = p3

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    while t < 1:
        t += speed

        p0_x = 1 * (1-t)**3 * p0[0]
        p0_y = 1 * (1-t)**3 * p0[1]

        p1_x = 3 * (1-t)**2 * t * p1[0]
        p1_y = 3 * (1-t)**2 * t * p1[1]

        p2_x = 3 * (1-t) * t**2 * p2[0]
        p2_y = 3 * (1-t) * t**2 * p2[1]

        p3_x = 1 * t**3 * p3[0]
        p3_y = 1 * t**3 * p3[1]

        x = p0_x + p1_x + p2_x + p3_x
        y = p0_y + p1_y + p2_y + p3_y

        pygame.draw.circle(screen, (0, 0, 0), (round(x),round(y)), 1)
        pygame.draw.line(screen, (50, 50, 50), p0, p1)
        pygame.draw.line(screen, (50, 50, 50), p2, p3)

        

        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text4, text4_rect)
    
    pygame.display.flip()

pygame.quit()