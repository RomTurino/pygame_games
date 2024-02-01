from constants import *
from tetromino import Tetramino
import pygame
import pygame.freetype as ft
from color import ANTIQUE_WHITE

class Text:
    def __init__(self, window):
        self.window = window
        self.font = ft.Font(FONT_PATH)
    
    def on_draw(self):
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.595, SCREEN_HEIGHT * 0.02),
                            text='TETRIS', fgcolor=ANTIQUE_WHITE,
                            size=TILE_SIZE * 1.15)
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.66, SCREEN_HEIGHT * 0.22),
                            text='next', fgcolor='orange',
                            size=TILE_SIZE * 1.2)
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.62, SCREEN_HEIGHT * 0.6),
                            text='score', fgcolor='orange',
                            size=TILE_SIZE * 1.2)
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.62, SCREEN_HEIGHT * 0.7),
                            text=f'{self.window.tetris.points}', fgcolor='white',
                            size=TILE_SIZE * 1.6)
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.62, SCREEN_HEIGHT * 0.8),
                            text='record', fgcolor='orange',
                            size=TILE_SIZE * 1.05)
        self.font.render_to(self.window.screen, (SCREEN_WIDTH * 0.62, SCREEN_HEIGHT * 0.9),
                            text=f'0', fgcolor='white',
                            size=TILE_SIZE * 1.6)

class Tetris:
    def __init__(self, window) -> None:
        self.window = window
        self.tetramino_list = pygame.sprite.Group() 
        self.field = self.get_field_matrix()       
        self.tetramino = Tetramino(self)
        self.next_tetramino = Tetramino(self, current=False)
        self.speed_up = False
        self.points = 0
    
    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1 , -1):
            for x in range(FIELD_W):
                self.field[row][x] = self.field[y][x]
                if self.field[y][x]:
                    self.field[row][x].pos = vec(x,y)
            if sum(map(bool, self.field[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field[row][x].alive = False
                    self.field[row][x] = 0

        
    def put_tetramino_blocks_in_matrix(self):
        for block in self.tetramino.blocks:
            x,y = int(block.pos.x), int(block.pos.y)
            self.field[y][x] = block
            
        
    def get_field_matrix(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
        
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.window.screen, 
                                 MARGIN_COLOR,
                                 (x * TILE_SIZE,
                                 y * TILE_SIZE,
                                 TILE_SIZE,
                                 TILE_SIZE),
                                 width=1
                                 )
    
    def is_game_over(self):
        if self.tetramino.blocks[0].pos.y == INIT_POS[1]:
            pygame.time.wait(300)
            return True
        
    
    def check_tetramino_landing(self):
        if self.tetramino.landing:
            if self.is_game_over():
                self.__init__(self.window)
            else:
                self.points+=1
                self.speed_up = False
                self.put_tetramino_blocks_in_matrix()
                self.next_tetramino.current = True
                self.tetramino = self.next_tetramino   
                self.next_tetramino = Tetramino(self, current=False)
    
    def on_draw(self):
        self.draw_grid()
        self.tetramino_list.draw(self.window.screen)
    
    def update(self):
        trigger = [self.window.anim_triger, self.window.fast_anim_triger][self.speed_up]
        if trigger:
            self.tetramino.update()
            self.check_full_lines()
            self.check_tetramino_landing()
        self.tetramino_list.update()
    
    def control(self, pressed_key):
        if pressed_key == pygame.K_LEFT:
            self.tetramino.move(direction="left")
        elif pressed_key == pygame.K_RIGHT:
            self.tetramino.move(direction="right")
        elif pressed_key == pygame.K_UP:
            self.tetramino.rotate()
        elif pressed_key == pygame.K_DOWN:
            self.speed_up = True