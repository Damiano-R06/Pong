import pygame

import pygame.freetype
from states import State

class Start:
    def __init__(self, screen):
        self.screen = screen
        self.startButton = pygame.Rect(screen.get_width()//2 - 200, screen.get_height()//2 - 150, 400,100)
        self.helpButton = pygame.Rect(screen.get_width()//2 - 200, screen.get_height()//2 - 25, 400,100)
        self.font = pygame.freetype.Font(None, size=50)
    
    def startUI(self,events):
        curState = State.START
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.startButton.collidepoint(event.pos):
                    curState = State.RUNNING
                    return curState

        self.screen.fill("black")

        pygame.draw.rect(self.screen, "white", self.startButton, width=0)
        self.font.render_to(self.screen, (self.screen.get_width()//2 - 65, self.screen.get_height()//2 - 120), "Start", fgcolor=(0, 0, 0))

        pygame.draw.rect(self.screen, "white", self.helpButton, width=0)
        self.font.render_to(self.screen, (self.screen.get_width()//2 - 63, self.screen.get_height()//2 + 5), "Help", fgcolor=(0, 0, 0))

        pygame.display.flip()

        return curState


