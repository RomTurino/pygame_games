import os
from constants import *
from color import YELLOW_GREEN, JUNE_BUD, PERSIAN_BLUE
from barrier import Barrier
from snakesprite import Snake
from food import Food
import status
from status import GameStatus
import pygame
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


class GameWindow():
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.egg = Food()
        self.snake = Snake(SNAKE_INITIAL_LENGTH, self)
        self.snake_moves = True
        self.text_font = pygame.font.Font(FONT_FILE, 41)
        self.score = 0
        self.record = self.read_record()

    def write_record(self, record: int):
        with open(RECORD_FILE, "w", encoding="utf-8") as file:
            file.write(f"{record}")

    def read_record(self):
        if not os.path.exists(RECORD_FILE):
            return 0
        with open(RECORD_FILE, "r", encoding="utf-8") as file:
            return int(file.read())

    def update_record(self):
        if self.score > self.record:
            self.record = self.score
            self.write_record(self.record)

    def setup(self):
        self.barriers = pygame.sprite.Group()
        self.bar_coords = []
        for column in range(0, COLUMN_COUNT, 2):
            barrier = Barrier()
            barrier.rect.centerx = TILE_WIDTH/2 + TILE_WIDTH * column
            barrier.rect.centery = TILE_HEIGHT/2
            self.barriers.add(barrier)
            barrier = Barrier()
            barrier.rect.centerx = TILE_WIDTH/2 + TILE_WIDTH * column
            barrier.rect.centery = SCREEN_HEIGHT - TILE_HEIGHT/2
            self.barriers.add(barrier)
        for row in range(0, ROW_COUNT, 2):
            barrier = Barrier()
            barrier.rect.centerx = SCREEN_WIDTH - TILE_WIDTH/2
            barrier.rect.centery = TILE_HEIGHT/2 + TILE_HEIGHT * row
            self.barriers.add(barrier)
            barrier = Barrier()
            barrier.rect.centerx = TILE_WIDTH/2
            barrier.rect.centery = TILE_HEIGHT/2 + TILE_HEIGHT * row
            self.barriers.add(barrier)

    def draw_bg(self):
        color = JUNE_BUD
        for row in range(0, ROW_COUNT):
            for column in range(0, COLUMN_COUNT):
                if color == JUNE_BUD:
                    color = YELLOW_GREEN
                else:
                    color = JUNE_BUD
                pygame.draw.rect(self.screen, color,
                                 (row*TILE_WIDTH, column*TILE_HEIGHT,
                                  TILE_WIDTH, TILE_HEIGHT))

    def draw_points(self, is_center: bool = False):
        points_text = self.text_font.render(
            f"Счет: {self.score}", True, YELLOW_GREEN, PERSIAN_BLUE)
        if status.game_status == GameStatus.GAME_ON:
            self.screen.blit(points_text, (0, SCREEN_HEIGHT-41))
        else:
            record_text = self.text_font.render(
                f"Рекорд: {self.record}", True, YELLOW_GREEN, PERSIAN_BLUE)
            self.screen.blit(points_text, (COLUMN_COUNT//2 *
                             TILE_WIDTH - TILE_WIDTH*2 + 10, SCREEN_HEIGHT/4))
            self.screen.blit(record_text, (COLUMN_COUNT//2 *
                             TILE_WIDTH - TILE_WIDTH*2 + 10, SCREEN_HEIGHT/2))

    def on_draw(self):
        self.draw_bg()
        if status.game_status == GameStatus.GAME_ON:
            self.egg.draw(self.screen)
            self.barriers.draw(self.screen)
            self.snake.draw(self.screen)
        self.draw_points()

    def on_key_press(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake.move_left()
            if event.key == pygame.K_RIGHT:
                self.snake.move_right()
            if event.key == pygame.K_UP:
                self.snake.move_up()
            if event.key == pygame.K_DOWN:
                self.snake.move_down()
            if event.key == pygame.K_SPACE:
                print(status.game_status)

    def on_key_release(self, event: pygame.event.Event):
        if event.type == pygame.KEYUP:
            pass

    def on_mouse_press(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def on_mouse_motion(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            pass

    def is_on_barrier(self):
        for barrier in self.barriers:
            if barrier.rect.centerx == self.egg.rect.centerx:
                if barrier.rect.centery == self.egg.rect.centery:
                    return True
        return False

    def run(self):
        global game_status
        clock = pygame.time.Clock()
        RUNNING = True
        self.setup()
        is_move = True
        is_egg = True
        # self.draw_bg()
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.update_record()
                    RUNNING = False
                self.on_key_press(event)
                self.on_key_release(event)
                self.on_mouse_press(event)
                self.on_mouse_motion(event)
            self.on_draw()
            if status.game_status == GameStatus.GAME_ON:
                is_egg = self.egg.count_time(is_egg, FOOD_DELAY_SEC)
                if is_egg:
                    self.egg.set_location()
                    while self.is_on_barrier():
                        self.egg.set_location()
                is_move = self.snake.count_time(
                    is_move, SNAKE_MOVEMENT_DELAY_SEC)
                if is_move:
                    self.snake.walk()
                    self.snake.teleport(0, self.width, 0, self.height)
                self.snake.update()
                
                for barrier in self.barriers:
                    if self.snake.is_collide(barrier):
                        self.update_record()
                        status.game_status = GameStatus.GAME_OVER

            pygame.display.update()
            clock.tick(FPS)
