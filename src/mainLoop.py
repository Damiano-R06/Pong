import pygame

from running import Pong

from enum import Enum

class State(Enum):
    START = 1
    RUNNING = 2
    END = 3

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True
curState = State.RUNNING

game = Pong(screen)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if curState == State.RUNNING:
        run = game.mainLoop()

pygame.quit()