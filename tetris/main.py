import pygame
from constants import *
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from tetris import Tetris, Text
import os

class GameWindow:
    def __init__(self, width, height, title):
        pygame.init()
        # window attributes
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
    
    def on_draw(self):
        self.screen.fill(SCREEN_COLOR)
        self.screen.fill(BG_COLOR, rect=(0,0, FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE))
        self.tetris.on_draw()
        self.text.on_draw()

    
    def load_images(self):
        d = "tetris_new/img/"
        files = [d+"red.jpg", d+"green.jpg", d+"blue.jpg"]
        images = [pygame.image.load(file).convert_alpha() for file in files]
        images = [pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images
            
    def set_timer(self):
        self.user_event = pygame.USEREVENT + 1
        self.fast_user_event = pygame.USEREVENT + 2
        self.anim_triger = False
        self.fast_anim_triger = False
        try:
            pygame.time.set_timer(self.user_event, self.tetris.tetramino.speed - self.tetris.level*10)
        except:
            pygame.time.set_timer(self.user_event, ANIM_DELAY)
        pygame.time.set_timer(self.fast_user_event, FAST_ANIM_DELAY)

    def on_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            self.tetris.control(event.key)
        
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)
        pygame.display.update()


    def run(self):
        RUNNING = True
        while RUNNING:
            self.anim_triger = False
            self.fast_anim_triger = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.tetris.write_record(self.tetris.record)
                    RUNNING = False
                self.on_key_press(event)
                if event.type == self.user_event:
                    self.anim_triger = True
                if event.type == self.fast_user_event:
                    self.fast_anim_triger = True
            self.update()
            self.on_draw()


window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()
