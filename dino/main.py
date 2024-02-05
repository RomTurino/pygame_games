from constants import *
from cactus import Cactus
from back import Road
from dino import Dino
import pygame
import random


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
        self.cactus_group = pygame.sprite.Group()
        self.road = Road(self)
        self.road2 = Road(self)
        self.road2.go_to_end()
        self.dino = Dino(self)

    def set_timer(self):
        self.user_event = pygame.USEREVENT + 1
        self.cactus_appear = pygame.USEREVENT + 2
        self.jump_event = pygame.USEREVENT + 3
        self.anim_triger = False
        self.cactus_triger = False
        self.jump_triger = False
        pygame.time.set_timer(self.cactus_appear, random.randint(2000, 4000))
        pygame.time.set_timer(self.user_event,ANIM_DELAY)
        # pygame.time.set_timer(self.jump_event,0)# 40)

    def on_draw(self):
        self.screen.fill(SCREEN_COLOR)
        self.cactus_group.draw(self.screen)
        self.road.on_draw()
        self.road2.on_draw()
        self.dino.on_draw()

    def on_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            self.dino.control(event.key)

    def group_generate(self):
        for i in range(random.randint(1, 3)):
            cactus = Cactus(self)
            cactus.rect.centerx += i*50
            self.cactus_group.add(cactus)

    def update(self):
        pygame.display.update()
        self.cactus_group.update()
        self.dino.update()
        if self.cactus_triger:
            self.group_generate()
        self.road.update()
        self.road2.update()

    def run(self):
        RUNNING = True
        while RUNNING:
            self.anim_triger = False
            self.cactus_triger = False
            self.jump_triger = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                if event.type == self.user_event:
                    self.anim_triger = True
                if event.type == self.cactus_appear:
                    self.cactus_triger = True
                if event.type == self.jump_event:
                    self.jump_triger = True
                self.on_key_press(event)
            self.update()
            self.on_draw()
            self.clock.tick(FPS)


window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()
