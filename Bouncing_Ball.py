import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# Initial screen color
screen.fill("lightblue")

# Ball properties (None until user clicks)
ball_pos = None
ball_radius = 30
ball_color = (255, 0, 0)
ball_speed = [5, 4]  # x and y speed

running = True

while running:
    screen.fill("lightblue")  # Clear and redraw every frame

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # When mouse is clicked, create a ball at that position
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            ball_pos = list(mouse_pos)  # Store position as [x, y]
            ball_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

    # If ball exists, move and draw it
    if ball_pos:
        # Move the ball
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Bounce off edges
        if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= 500:
            ball_speed[0] *= -1
        if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= 500:
            ball_speed[1] *= -1

        # Draw the ball
        pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
