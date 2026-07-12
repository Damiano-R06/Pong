import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
movSpeed = 5
dt = 0

player_pos = 200
paddle = pygame.Rect(75, player_pos, 10, 75)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "white", paddle, width=0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos > 0:
        paddle.move_ip(0,-movSpeed)
        player_pos -= movSpeed
        print(player_pos)
    if keys[pygame.K_s] and player_pos < 650:
        paddle.move_ip(0,movSpeed)
        player_pos += movSpeed
        print(player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if keys[pygame.K_q]:
        running = False

pygame.quit()