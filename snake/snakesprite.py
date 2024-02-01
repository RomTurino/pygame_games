from mysprite import MySprite
from constants import *
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
from color import PERSIAN_BLUE
import status
from status import GameStatus

class Snake(MySprite):
    def __init__(self, length, parent_window):
        self.length = length
        self.parent_window = parent_window
        self.image = pygame.Surface(
            (TILE_WIDTH, TILE_HEIGHT))
        self.image.fill(PERSIAN_BLUE)
        self.rect = self.image.get_rect()
        self.direction = "right"
        self.is_move = True
        self.center_x = [TILE_WIDTH * COLUMN_COUNT /
                         2 - TILE_WIDTH/2] * self.length
        self.center_y = [TILE_HEIGHT * ROW_COUNT /
                         2 - TILE_HEIGHT/2] * self.length

    def grow_bigger(self, points):
        self.length += points
        self.parent_window.score += 1
        self.center_x.append(-TILE_WIDTH)
        self.center_y.append(-TILE_HEIGHT)

    def is_collide(self, collide_sprite):
        head_x = self.center_x[0]
        head_y = self.center_y[0]
        if type(collide_sprite) != pygame.rect.Rect:
            colspr_centerx = collide_sprite.rect.centerx
            colspr_centery = collide_sprite.rect.centery
        else:
            colspr_centerx = collide_sprite.centerx
            colspr_centery = collide_sprite.centery
        if head_x < colspr_centerx < head_x + TILE_WIDTH:
            if head_y < colspr_centery < head_y + TILE_HEIGHT:
                return True
        return False

    def draw(self, screen):
        for i in range(self.length):
            screen.blit(self.image, (self.center_x[i], self.center_y[i]))

    def move_left(self):
        if not self.direction == "right":
            self.direction = "left"

    def move_right(self):
        if not self.direction == "left":
            self.direction = "right"

    def move_up(self):
        if not self.direction == "down":
            self.direction = "up"

    def move_down(self):
        if not self.direction == "up":
            self.direction = "down"

    def walk(self):
        global game_status
        for i in range(self.length-1, 0, -1):
            self.center_x[i] = self.center_x[i-1]
            self.center_y[i] = self.center_y[i-1]

        if self.direction == "left":
            self.center_x[0] -= TILE_WIDTH
        elif self.direction == "right":
            self.center_x[0] += TILE_WIDTH
        elif self.direction == "up":
            self.center_y[0] -= TILE_HEIGHT
        elif self.direction == "down":
            self.center_y[0] += TILE_HEIGHT

        if self.is_collide(self.parent_window.egg):
            self.grow_bigger(self.parent_window.egg.growth_points)
            self.parent_window.egg.set_location()
        for i in range(self.length):
            if i != 0:
                rect = pygame.Rect(
                    self.center_x[i], self.center_y[i], TILE_WIDTH, TILE_HEIGHT)
                if self.is_collide(rect):
                    status.game_status = GameStatus.GAME_OVER
                    self.parent_window.update_record()
                    print("Бьют")
                    print(status.game_status)
                    
                    

    def teleport(self, left, right, top, bottom):
        if self.center_x[0] < left:
            self.center_x[0] = right - TILE_WIDTH
        elif self.center_x[0] > right-TILE_WIDTH:
            self.center_x[0] = 0
        elif self.center_y[0] < top:
            self.center_y[0] = bottom - TILE_HEIGHT
        elif self.center_y[0] > bottom - TILE_HEIGHT:
            self.center_y[0] = top


