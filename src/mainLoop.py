import pygame

from running import Pong
from start import Start
from states import State
from pause import Pause
from gameOver import GameOver

pygame.init()

screen = pygame.display.set_mode((1280, 720))
curState = State.START

game = Pong(screen)
startScreen = Start(screen)
pause = Pause(screen)
gameOver = GameOver(screen)

startedRun = False
winner = 0

while curState != State.END:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            curState = State.END
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            curState = State.END
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if curState == State.RUNNING:
                curState = State.PAUSE
            elif curState == State.PAUSE:
                curState = State.RUNNING
                game.clock = pygame.time.Clock()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and winner != 0:
            game = Pong(screen)
            winner = 0
            startedRun = False
            curState = State.START

    if curState == State.RUNNING:
        if not startedRun:
            game.clock = pygame.time.Clock()
            game.dt = 0
            startedRun = True
        curState = game.mainLoop()
    
    if curState == State.START:
        curState = startScreen.startUI(events)
    
    if curState == State.PAUSE:
       pause.paused()

    if curState == State.P1WIN:
        winner = 1
        gameOver.over(winner)
    
    if curState == State.P2WIN:
        winner = 2
        gameOver.over(winner)
    
        
pygame.quit()