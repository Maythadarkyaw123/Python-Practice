import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Pygame Window")
screen.fill("lightblue")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            random_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            
            draw_circle = pygame.draw.circle(screen, random_color, mouse_pos, 30)
    
        pygame.display.update()
        
pygame.quit()