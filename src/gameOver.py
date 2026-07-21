import pygame

import pygame.freetype

class GameOver:
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.freetype.Font(None, size=50)
    
    def over(self, winner):


        self.screen.fill("black")

        self.font.render_to(self.screen, (self.screen.get_width()//2 - 150, self.screen.get_height()//2 - 120), "GAME OVER :(", fgcolor=(255, 255, 255))
        
        if winner == 1:
            self.font.render_to(self.screen, (self.screen.get_width()//2 -150, self.screen.get_height()//2 - 70), "PLAYER 1 WINS", fgcolor=(255, 255, 255))
        
        if winner == 2:
            self.font.render_to(self.screen, (self.screen.get_width()//2-150, self.screen.get_height()//2 - 70), "PLAYER 2 WINS", fgcolor=(255, 255, 255))

        pygame.display.flip()

