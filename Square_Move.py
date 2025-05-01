# import pygame
# pygame.init()

# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Move a Square with arrow key")

# #define square properties
# width, height = 50, 50
# x, y = 200, 150
# speed = 5  

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#         keys = pygame.key.get_pressed()
        
#         if keys[pygame.K_LEFT]:
#             x -= speed
#         if keys[pygame.K_RIGHT]:
#             x += speed
#         if keys[pygame.K_UP]:
#             y -= speed
#         if keys[pygame.K_DOWN]:
#             y += speed
         
#         screen.fill("white")   
#         pygame.draw.rect(screen, "blue", pygame.Rect(x, y, width, height))    
#         pygame.display.update()
        
# pygame.quit()


import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square Move")

speed = 10
x, y = 150, 200
height, width = 50, 50

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            x -= speed
            
        if keys[pygame.K_RIGHT]:
            x += speed
            
        if keys[pygame.K_UP]:
            y += speed
            
        if keys[pygame.K_DOWN]:
            y -= speed
        
        screen.fill("white")   
        pygame.draw.rect(screen, "blue", pygame.Rect((x, y),(height, width)))
            
        pygame.display.update()
            
            
pygame.quit()  
