import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (130, 50, 200)

screen_resolution = (800, 600)

screen = pygame.display.set_mode(screen_resolution)

pygame.display.set_caption('Purple Rain')

clock = pygame.time.Clock()

gameLoop = True

class Rain:

    def __init__(self, x, y, width, height, yspeed):
        self.rect = pygame.Rect(x,y,width,height)
        self.yspeed = yspeed
        self.x = x
        self.y = y

    def fall(self):
        self.rect.move_ip(0, self.yspeed)

    def draw(self):
        pygame.draw.rect(screen, PURPLE, self.rect)

drop = Rain(400,300,2,20,9)

while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    drop.draw()
    drop.fall()
    pygame.display.flip()
    clock.tick(FPS)