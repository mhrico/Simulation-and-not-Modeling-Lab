import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *

vf = None
xb = []
yb = []
inputs = []

with open('./pp_input.txt') as file:
    for line in file.readlines():
        inputs.append(line.rstrip().rsplit(','))

vf = int(inputs[0][0])
xb = [int(x) for x in inputs[1]]
yb = [int(x) for x in inputs[2]]

xf = [0]
yf = [50]

for i in range(len(xb)):
    if i > 10:
        print('Time limit exceed!')
        break

    dist = np.sqrt( (yb[i] - yf[i])**2 + (xb[i] - xf[i])**2 )
    if dist <= 10:
        print('caught at time', i)
        break

    cosx = (xb[i] - xf[i]) / dist
    sinx = (yb[i] - yf[i]) / dist

    xf.append(xf[i] + vf * cosx)
    yf.append(yf[i] + vf * sinx)

size = width, height = (1500, 800)
center_coords = (width/2, height/2)

fighter_screen_x = [(center_coords[0]+x*4) for x in xf]
fighter_screen_y = [(center_coords[1]+y*4) for y in yf]
bomber_screen_x = [(center_coords[0]+x*4) for x in xb]
bomber_screen_y = [(center_coords[1]+y*4) for y in yb]

print('Red line = Bomber, Blue line = Fighter')

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pure Pursuit')
screen.fill((255, 255, 255))
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.draw.line(screen, (0, 0, 0), (center_coords[0]-2000,center_coords[1]), (center_coords[0]+2000,center_coords[1]))
    pygame.draw.line(screen, (0, 0, 0), (center_coords[0],center_coords[1]-2000), (center_coords[0],center_coords[1]+2000))
    pygame.draw.lines(screen, (0, 0, 255), False, tuple(zip(fighter_screen_x, fighter_screen_y)), 4)
    pygame.draw.lines(screen, (255, 0, 0), False, tuple(zip(bomber_screen_x, bomber_screen_y)), 4)

    pygame.display.flip()
pygame.quit()