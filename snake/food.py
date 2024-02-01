from mysprite import MySprite
from constants import *
import random

class Food(MySprite):
    def __init__(self):
        super().__init__(FOOD_IMG, FOOD_SCALE)
        self.growth_points = 1
        self.set_location()

    def set_location(self):
        self.rect.centerx = TILE_WIDTH/2 + TILE_WIDTH * \
            random.randint(0, COLUMN_COUNT-1)
        self.rect.centery = TILE_HEIGHT/2 + \
            TILE_HEIGHT * random.randint(0, ROW_COUNT - 1)

