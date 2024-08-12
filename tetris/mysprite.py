from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame



class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename: str, scale: int):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale,
                                                         self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.center_x = 0
        self.center_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # pygame.display.flip()

    def count_time(self, is_on: bool, delay: int):
        if is_on:
            self.start_time = pygame.time.get_ticks() / 1000
            return False
        else:
            self.end_time = pygame.time.get_ticks() / 1000
            if self.end_time - self.start_time > delay:
                return True

