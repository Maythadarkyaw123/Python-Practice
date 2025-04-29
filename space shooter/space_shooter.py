

#basic pygame setup
import pygame
pygame.init()

w,h = 800,500
screen = pygame.display.set_mode((w,h))

# change the title of the window
pygame.display.set_caption("Space Shooter")

#surface
surface = pygame.Surface((100,200))

# To run the window
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #draw the game
    screen.fill("darkgray")
    screen.blit(surface, (100,100))
    
    pygame.display.update()
    
    
            
pygame.quit()