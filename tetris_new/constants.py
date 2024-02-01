from color import ANTIQUE_BRASS, BLACK, RED, ANTIQUE_FUCHSIA
from pygame.math import Vector2
import os

vec = Vector2


# tetris
TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
INIT_POS = vec(FIELD_W//2-1, 0)
NEXT_POS = vec(FIELD_W*1.3, FIELD_H*0.45)
ANIM_DELAY = 400
FAST_ANIM_DELAY = 20

FONT_PATH = "tetris_new/shrift.ttf"
RECORD_FILE = "tetris_new/record.txt"

# colors
BG_COLOR = ANTIQUE_BRASS
MARGIN_COLOR = BLACK
TILE_COLOR = RED

# window
SCREEN_COLOR = ANTIQUE_FUCHSIA
SCREEN_SCALE_W, SCREEN_SCALE_H = 1.7, 1
SCREEN_WIDTH = FIELD_W * TILE_SIZE * SCREEN_SCALE_W
SCREEN_HEIGHT = FIELD_H * TILE_SIZE * SCREEN_SCALE_H
SCREEN_TITLE = "Тетрис"
FPS = 25

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

DIRECTIONS = {
    "left": vec(-1, 0),
    "right": vec(1, 0),
    "down": vec(0, 1)
}
