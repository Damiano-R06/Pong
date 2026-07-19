import pygame
import random

class Pong:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.movSpeedPad = 7
        self.colisionSpeed = 25
        self.movSpeedBallx = -250
        self.movSpeedBally = random.randint(-1, 1) * 250 or 250
        self.radius = 5
        self.dt = 0
        self.player_pos1 = 320
        self.player_pos2 = 320
        self.ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        self.paddle = pygame.Rect(75, self.player_pos1, 10, 80)
        self.enemy = pygame.Rect(screen.get_width() - 85, self.player_pos2, 10, 80)


    def mainLoop(self):
        
        #fill the screen with a color to wipe away anything from last frame
        self.screen.fill("black")

        pygame.draw.rect(self.screen, "white", self.paddle, width=0)
        pygame.draw.rect(self.screen, "white", self.enemy, width=0)
        pygame.draw.circle(self.screen, "white", self.ball_pos, self.radius, width=0)

        keys = pygame.key.get_pressed()
        
        self.ball_pos.x += self.movSpeedBallx * self.dt
        self.ball_pos.y += self.movSpeedBally * self.dt

        if self.paddle.collidepoint(self.ball_pos.x - self.radius, self.ball_pos.y - self.radius):
            movingUp = self.movSpeedBally < 0
            self.movSpeedBallx *= -1

            signX = 1 if self.movSpeedBallx > 0 else -1
            signY = 1 if self.movSpeedBally > 0 else -1

            if keys[pygame.K_w] and movingUp:
                self.movSpeedBallx += self.colisionSpeed * signX
                self.movSpeedBally += self.colisionSpeed * signY
            if keys[pygame.K_w] and not movingUp:
                self.movSpeedBallx -= self.colisionSpeed *signX
                self.movSpeedBally -= self.colisionSpeed *signY
            if keys[pygame.K_s] and not movingUp:
                self.movSpeedBallx += self.colisionSpeed *signX
                self.movSpeedBally += self.colisionSpeed *signY
            if keys[pygame.K_s] and movingUp:
                self.movSpeedBallx -= self.colisionSpeed *signX
                self.movSpeedBally -= self.colisionSpeed *signY
            
                
        if self.enemy.collidepoint(self.ball_pos.x - self.radius + 10, self.ball_pos.y - self.radius):
            movingUp = self.movSpeedBally < 0
            self.movSpeedBallx *= -1

            signX = 1 if self.movSpeedBallx > 0 else -1
            signY = 1 if self.movSpeedBally > 0 else -1

            if keys[pygame.K_UP] and movingUp:
                self.movSpeedBallx += self.colisionSpeed *signX
                self.movSpeedBally += self.colisionSpeed *signY
            if keys[pygame.K_UP] and not movingUp:
                self.movSpeedBallx -= self.colisionSpeed *signX
                self.movSpeedBally -= self.colisionSpeed  *signY
            if keys[pygame.K_DOWN] and not movingUp:
                self.movSpeedBallx += self.colisionSpeed *signX
                self.movSpeedBally += self.colisionSpeed *signY
            if keys[pygame.K_DOWN] and movingUp:
                self.movSpeedBallx -= self.colisionSpeed *signX
                self.movSpeedBally -= self.colisionSpeed *signY

        if self.ball_pos.y - self.radius <= 0 or self.ball_pos.y + self.radius >= self.screen.get_height():
            self.movSpeedBally *= -1

        #Player Move
        if keys[pygame.K_w] and self.player_pos1 > 0:
            self.paddle.move_ip(0,-self.movSpeedPad)
            self.player_pos1 -= self.movSpeedPad
            

        if keys[pygame.K_s] and self.player_pos1 < 650:
            self.paddle.move_ip(0,self.movSpeedPad)
            self.player_pos1 += self.movSpeedPad

        if keys[pygame.K_UP] and self.player_pos2 > 0:
            self.enemy.move_ip(0,-self.movSpeedPad)
            self.player_pos2 -= self.movSpeedPad

        if keys[pygame.K_DOWN] and self.player_pos2 < 650:
            self.enemy.move_ip(0,self.movSpeedPad)
            self.player_pos2 += self.movSpeedPad

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        self.dt = self.clock.tick(60) / 1000

        if keys[pygame.K_q] or self.ball_pos.x - self.radius < 0 or self.ball_pos.x + self.radius > self.screen.get_width():
            return False
        return True