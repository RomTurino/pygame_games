import pygame
from constants import *
from mysprite import MySprite

class Dino(MySprite):
    JUMP_VEL = 8.5
    def __init__(self, window):
        super().__init__(DINO_IMG, DINO_SCALE)
        self.window = window
        self.rect.center = (self.window.width/8, self.window.height/1.4)
        self.jump_vel = self.JUMP_VEL
        self.dino_jump = False
        self.velocity = VELOCITY
    
    def on_draw(self):
        super().draw(self.window.screen)
        
    def control(self, pressed_key):
        if pressed_key == pygame.K_UP or pressed_key == pygame.K_SPACE:
            self.dino_jump = True
        
        
    
    def update(self):
        # if self.rect.bottom < self.window.road.rect.bottom:
        if self.dino_jump:
            if self.window.jump_triger:
                self.rect.centery -= self.velocity
                self.velocity -= GRAVITY
                if self.velocity < -JUMP_HEIGHT:
                    self.dino_jump = False
                    self.velocity = JUMP_HEIGHT
        
