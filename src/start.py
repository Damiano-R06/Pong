import pygame

class Start:
    def __init__(self, screen):
        self.screen = screen
        self.startButton = pygame.Rect(screen.get_width()/2 - 250, screen.get_height()/2 - 150, 500,100)
    
    def startUI(self):
        self.screen.fill("black")

        pygame.draw.rect(self.screen, "white", self.startButton, width=0)

        pygame.display.flip()


