import pygame

from running import Pong
from start import Start
from states import State

pygame.init()
screen = pygame.display.set_mode((1280, 720))
curState = State.START

game = Pong(screen)
startScreen = Start(screen)

startedRun = False

while curState != State.END:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            curState = State.END

    if curState == State.RUNNING:
        if not startedRun:
            game.clock = pygame.time.Clock()
            game.dt = 0
            startedRun = True
        curState = game.mainLoop()
    
    if curState == State.START:
        curState = startScreen.startUI(events)
    
        
pygame.quit()