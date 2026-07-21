import pygame
import pygame.freetype
from states import State

class Pause:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.freetype.Font(None, size=50)

    def paused(self):

        self.font.render_to(self.screen, (self.screen.get_width()//2 - 65, self.screen.get_height()//2 - 120), "PAUSED", fgcolor=(255, 255, 255))
        
        pygame.display.flip()
        