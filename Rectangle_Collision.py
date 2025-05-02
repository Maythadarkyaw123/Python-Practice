import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Rectangle Collision")
screen.fill("lightblue")

# Rectangles
rect1 = pygame.Rect(100, 100, 100, 60)  # Static rectangle
rect2 = pygame.Rect(300, 200, 100, 60)  # Movable with arrow keys

# Colors
color1 = (0, 128, 255)
color2 = (0, 255, 128)
collision_color = (255, 0, 0)

speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Move rect2 with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect2.x -= speed
    if keys[pygame.K_RIGHT]:
        rect2.x += speed
    if keys[pygame.K_UP]:
        rect2.y -= speed
    if keys[pygame.K_DOWN]:
        rect2.y += speed

    # Check for collision
    if rect1.colliderect(rect2):
        pygame.draw.rect(screen, collision_color, rect1)
        pygame.draw.rect(screen, collision_color, rect2)
    else:
        pygame.draw.rect(screen, color1, rect1)
        pygame.draw.rect(screen, color2, rect2)
    
    pygame.display.update()
           
pygame.quit()