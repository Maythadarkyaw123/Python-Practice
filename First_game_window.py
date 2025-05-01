import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        pygame.display.update()
        
pygame.quit()