import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
movSpeedPad = 7
colisionSpeed = 25


movSpeedBallx = -250
movSpeedBally = random.randint(-1,1)*250

radius = 5
dt = 0

player_pos1 = 320
player_pos2 = 320
ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)


paddle = pygame.Rect(75, player_pos1, 10, 80)
enemy = pygame.Rect(screen.get_width() - 85, player_pos2, 10, 80)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "white", paddle, width=0)
    pygame.draw.rect(screen, "white", enemy, width=0)
    pygame.draw.circle(screen, "white", ball_pos, radius, width=0)

    keys = pygame.key.get_pressed()
    
    ball_pos.x += movSpeedBallx * dt
    ball_pos.y += movSpeedBally * dt

    if paddle.collidepoint(ball_pos.x - radius, ball_pos.y - radius):
        movingUp = movSpeedBally < 0
        movSpeedBallx *= -1

        signX = 1 if movSpeedBallx > 0 else -1
        signY = 1 if movSpeedBally > 0 else -1

        if keys[pygame.K_w] and movingUp:
            movSpeedBallx += colisionSpeed * signX
            movSpeedBally += colisionSpeed * signY
        if keys[pygame.K_w] and not movingUp:
            movSpeedBallx -= colisionSpeed *signX
            movSpeedBally -= colisionSpeed *signY
        if keys[pygame.K_s] and not movingUp:
            movSpeedBallx -= colisionSpeed *signX
            movSpeedBally -= colisionSpeed *signY
        if keys[pygame.K_s] and movingUp:
            movSpeedBallx += colisionSpeed *signX
            movSpeedBally += colisionSpeed *signY
            
    if enemy.collidepoint(ball_pos.x - radius + 10, ball_pos.y - radius):
        movingUp = movSpeedBally < 0
        movSpeedBallx *= -1

        signX = 1 if movSpeedBallx > 0 else -1
        signY = 1 if movSpeedBally > 0 else -1

        if keys[pygame.K_UP] and movingUp:
            movSpeedBallx += colisionSpeed *signX
            movSpeedBally += colisionSpeed *signY
        if keys[pygame.K_UP] and not movingUp:
            movSpeedBallx -= colisionSpeed *signX
            movSpeedBally -= colisionSpeed  *signY
        if keys[pygame.K_DOWN] and not movingUp:
            movSpeedBallx -= colisionSpeed *signX
            movSpeedBally -= colisionSpeed *signY
        if keys[pygame.K_DOWN] and movingUp:
            movSpeedBallx += colisionSpeed *signX
            movSpeedBally += colisionSpeed *signY

    if ball_pos.y - radius <= 0 or ball_pos.y + radius >= screen.get_height():
         movSpeedBally *= -1

    #Player Move
    if keys[pygame.K_w] and player_pos1 > 0:
        paddle.move_ip(0,-movSpeedPad)
        player_pos1 -= movSpeedPad
        

    if keys[pygame.K_s] and player_pos1 < 650:
        paddle.move_ip(0,movSpeedPad)
        player_pos1 += movSpeedPad

    if keys[pygame.K_UP] and player_pos2 > 0:
        enemy.move_ip(0,-movSpeedPad)
        player_pos2 -= movSpeedPad

    if keys[pygame.K_DOWN] and player_pos2 < 650:
        enemy.move_ip(0,movSpeedPad)
        player_pos2 += movSpeedPad

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if keys[pygame.K_q] or ball_pos.x - radius < 0 or ball_pos.x + radius > screen.get_width():
        running = False

pygame.quit()