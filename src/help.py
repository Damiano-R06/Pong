import pygame
from states import State

class Instructions:

    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.freetype.Font(None, size=25)
        self.fontS = pygame.freetype.Font(None, size=20)
    
    def helpUI(self, events):
        curState = State.HELP

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                curState = State.START
                return curState

        self.screen.fill("black")

        self.font.render_to(self.screen, (self.screen.get_width()//2 - 200, self.screen.get_height()//2 - 120), "Welcom to Damiano's Pong!", fgcolor=(255, 255, 255))
        self.font.render_to(self.screen, (self.screen.get_width()//2 - 350, self.screen.get_height()//2 - 80), "The first player to reach 10 points WIN!", fgcolor=(255, 255, 255))
        self.font.render_to(self.screen, (self.screen.get_width()//2 - 350, self.screen.get_height()//2 - 40), "Use WASD for P1 and arrow keys for P2.", fgcolor=(255, 255, 255))
        self.font.render_to(self.screen, (self.screen.get_width()//2 - 350, self.screen.get_height()//2), "You can also press Q at any time to close the application.", fgcolor=(255, 255, 255))
        self.fontS.render_to(self.screen, (self.screen.get_width()//2 - 200, self.screen.get_height()//2 + 40), "Press S to return to start screen.", fgcolor=(255, 255, 255))

        pygame.display.flip()

        return curState