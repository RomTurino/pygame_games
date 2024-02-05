from os import path
from pygame import Vector2

# window
SCREEN_COLOR = (200, 200, 200)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Google Dinosaur"
MAIN_DIR = path.abspath("dino")
IMG_DIR = path.join(MAIN_DIR, "images")
FPS = 60


# cactus
LITTLE_CACTUS_FILENAMES = [path.join(IMG_DIR, f"cactus{i}.png") for i in range(1, 7)]
BIG_CACTUS_FILENAMES = [path.join(IMG_DIR, f"bigcactus{i}.png") for i in range(1, 6)]
INIT_CACTUS_FILENAME = path.join(IMG_DIR, "cactus2.png")
CACTUS_SCALE = 1
CACTUS_SPEED = 10
ANIM_DELAY = 4

# road
ROAD_IMG = path.join(IMG_DIR, "road.png")
ROAD_SCALE = 1
ROAD_SPEED = 10
ROAD_DELAY = 4


#динозавр
DINO_IMG = path.join(IMG_DIR, "dino1.png")
DINO_IMAGES = [path.join(IMG_DIR, f"dino{i}") for i in range(1,5)]
DINO_SCALE = 1
GRAVITY = 1
JUMP_HEIGHT = 20
VELOCITY = JUMP_HEIGHT
