import pygame

from running import Pong
from start import Start

from enum import Enum

class State(Enum):
    START = 1
    RUNNING = 2
    END = 3

pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True
curState = State.START

game = Pong(screen)
startScreen = Start(screen)

while run:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if curState == State.RUNNING:
        run = game.mainLoop()
    
    if curState == State.START:
        startScreen.startUI(events)
        
pygame.quit()