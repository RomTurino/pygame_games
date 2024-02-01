import color
import pygame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"
FPS = 30

class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename:str, scale:int):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, 
                                                         self.image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.center_x = SCREEN_WIDTH/2
        self.center_y = SCREEN_HEIGHT/2
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        



class GameWindow():
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        # self.bg = pygame.image.load(BG_IMG)
        # self.bg = pygame.transform.scale(
        #     self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        

    def setup(self):
        pass

    def on_draw(self):
        self.screen.fill(color.APRICOT)

    def on_key_press(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass
        
    def on_key_release(self, event: pygame.event.Event):
        if event.type == pygame.KEYUP:
            pass

    def on_mouse_press(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def on_mouse_motion(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            pass

    def run(self):
        clock = pygame.time.Clock()
        RUNNING = True
        self.setup()
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                self.on_key_press(event)
                self.on_key_release(event)
                self.on_mouse_press(event)
                self.on_mouse_motion(event)
            self.on_draw()
            pygame.display.update()
            clock.tick(FPS)


window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()
