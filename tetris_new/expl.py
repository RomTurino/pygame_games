import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры окна
width, height = 400, 400

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Вращение вектора")
clock = pygame.time.Clock()

# Начальные координаты вектора
vector = pygame.math.Vector2(100, 100)

# Угол поворота в радианах
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle -= 0.05
            if event.key == pygame.K_LEFT:
                angle -= 0.05

    # Очистка экрана
    screen.fill(WHITE)

    # Рисование вектора
    pygame.draw.line(screen, BLACK, (width // 2, height // 2), vector, 2)

    # Поворот вектора
    rotated_vector = vector.rotate(-math.degrees(angle))

    # Обновление координат вектора
    vector.update(rotated_vector.x, rotated_vector.y)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для стабильного отображения
    clock.tick(30)
