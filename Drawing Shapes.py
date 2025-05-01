import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw Shapes")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #drawing circle (surface, colour, center, radius)
        pygame.draw.circle(screen, "blue", [130,50], 20)
        
        #drawing rectangle(surface,  colour, pygame.Rect(x,y, width, height), thickness)  thickness = 0 is default fill rectangle
        pygame.draw.rect(screen, "blue", pygame.Rect(30,30,60, 60), 2)
        
        #drawing a line (surface, colour, start-pos, end-pos, thickness)
        pygame.draw.line(screen, "blue", (50, 50), (200, 150), 3)
        
        
        pygame.display.update()
            
pygame.quit()
