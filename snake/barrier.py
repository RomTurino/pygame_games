from mysprite import MySprite
from constants import BARRIER_IMG, BARRIER_SCALE

class Barrier(MySprite):
    def __init__(self):
        super().__init__(BARRIER_IMG, BARRIER_SCALE)
