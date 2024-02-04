import pygame
from constants import *
from mysprite import MySprite

class Road(MySprite):
    def __init__(self, window):
        super().__init__(ROAD_IMG, ROAD_SCALE)
        self.window = window
        self.rect.topleft=(0, self.window.height/1.5+50)
        self.speed = ROAD_SPEED
        
    def on_draw(self):
        self.window.screen.blit(self.image, self.rect)
        
    def go_to_end(self):
        self.rect.left = self.image.get_width()
    
    def update(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.go_to_end()