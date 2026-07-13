import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
movSpeedPad = 5


movSpeedBallx = -200
movSpeedBally = random.randint(-1,1)*200

radius = 5
dt = 0

player_pos = 320
ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)


paddle = pygame.Rect(75, player_pos, 10, 80)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "white", paddle, width=0)
    pygame.draw.circle(screen, "white", ball_pos, radius, width=0)

    keys = pygame.key.get_pressed()
    
    
    ball_pos.x += movSpeedBallx * dt
    ball_pos.y += movSpeedBally * dt

    if paddle.collidepoint(ball_pos.x - radius, ball_pos.y - radius):
        movSpeedBallx *= -1
    if ball_pos.y - radius <= 0 or ball_pos.y + radius >= screen.get_height():
         movSpeedBally *= -1

    if keys[pygame.K_w] and player_pos > 0:
        paddle.move_ip(0,-movSpeedPad)
        player_pos -= movSpeedPad
        print(player_pos)

    if keys[pygame.K_s] and player_pos < 650:
        paddle.move_ip(0,movSpeedPad)
        player_pos += movSpeedPad
        print(player_pos)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if keys[pygame.K_q] or ball_pos.x - radius < 0 or ball_pos.x + radius > screen.get_width():
        running = False

pygame.quit()