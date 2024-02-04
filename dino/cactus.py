from constants import *
from mysprite import MySprite
import pygame
import random


class Cactus(MySprite):
    def __init__(self, window):
        super().__init__(INIT_CACTUS_FILENAME, CACTUS_SCALE)
        self.window = window
        self.image = random.choice(self.load_images())
        self.rect = self.image.get_rect()
        self.speed = CACTUS_SPEED
        self.rect.bottomleft = (self.window.width, self.window.height/1.25)
        
    def load_images(self):
        images = [pygame.image.load(file).convert_alpha() for file in LITTLE_CACTUS_FILENAMES+BIG_CACTUS_FILENAMES]
        # images = [pygame.transform.scale(image, (image.get_width()*CACTUS_SCALE, image.get_height()*CACTUS_SCALE)) for image in images]
        return images
    
    def on_draw(self):
        self.window.screen.blit(self.image,self.rect )
        
    
    def update(self):
        if self.window.anim_triger:
            self.rect.centerx -= self.speed
            if self.rect.right < 0:
                self.kill()
    
    