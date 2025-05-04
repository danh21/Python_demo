# Click to a mole

from random import *
import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *

class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("assets\mole.gif")
        self.rect = self.image.get_rect()
    def flee(self):
        self.rect.left = randint(0, 600-220) # random location
        self.rect.top = randint(0, 400-220)

# main
pygame.init()
clock = pygame.time.Clock()
display.set_caption("Whack-a-Mole")
screen = display.set_mode((640, 480))
my_mole = Mole() # initialize sprites
all_sprites = Group(my_mole)
screen.fill((255, 255, 255)) # white background

while True:
    ev = event.wait() # wait for an event
    if ev.type == QUIT:
        pygame.quit()
        break
    elif ev.type == MOUSEBUTTONDOWN:
        if my_mole.rect.collidepoint(mouse.get_pos()):
            my_mole.flee() 
            screen.fill((255, 255, 255)) # white background
    display.update()
    all_sprites.draw(screen)  