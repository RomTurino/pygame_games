import pygame
from constants import *
from mysprite import MySprite
import random


class Block(pygame.sprite.Sprite):
    def __init__(self, tetramino, pos):
        self.tetramino = tetramino
        self.pos = vec(pos) + INIT_POS
        self.next_pos = vec(pos) + NEXT_POS
        super().__init__(self.tetramino.tetris.tetramino_list)
        self.image = tetramino.image
        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)
        self.sfx_speed = random.uniform(0.2, 0.6)
        self.sfx_cycles = random.randint(6, 8)
        self.cycle_counter = 0
        self.rect = self.image.get_rect()
        self.alive = True
    
    def sfx_end_time(self):
        if self.tetramino.tetris.window.anim_triger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True
        
    def sfx_run(self):
        self.image = self.sfx_image
        self.pos.y -= self.sfx_speed
        self.image = pygame.transform.rotate(self.image, pygame.time.get_ticks()*self.sfx_speed)
        
        
    def is_alive(self):
        if not self.alive:
            if not self.sfx_end_time():
                self.sfx_run()
            else:
                self.kill()

    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetramino.current]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetramino.tetris.field[y][x]):
            return False
        return True

    def rotate(self, pivot_pos):
        transported = self.pos - pivot_pos
        rotated = transported.rotate(90)
        return rotated + pivot_pos
        

class Tetramino:
    def __init__(self, tetris, current = True):
        self.current = current
        self.tetris = tetris
        self.image = random.choice(tetris.window.images)
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = []
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.speed = ANIM_DELAY
        
    def rotate(self):
        pivot = self.blocks[0].pos
        new_positions = [block.rotate(pivot) for block in self.blocks]
        if not self.is_collide(new_positions) and not self.shape == "O":
            for i, block in enumerate(self.blocks):
                self.blocks[i].pos = new_positions[i]

    def move(self, direction: str):
        move_direction = DIRECTIONS[direction]
        new_block_positions = [block.pos +
                               move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)
        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True

    def update(self):
        self.move("down")

    def is_collide(self, block_positions: list) -> bool:
        return any(map(Block.is_collide, self.blocks, block_positions))
