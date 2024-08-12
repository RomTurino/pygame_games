import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))

# Создаем вектор начальной позиции
position = pygame.math.Vector2(100, 100)

# Создаем вектор скорости
velocity = pygame.math.Vector2(2, 1)


# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновляем позицию с учетом скорости
    position += velocity

    # Очищаем экран
    screen.fill((255, 255, 255))

    # Рисуем объект на новой позиции
    pygame.draw.circle(screen, (0, 0, 255),
                       (int(position.x), int(position.y)), 20)

    # Обновляем экран
    pygame.display.flip()

    # Задержка, чтобы не слишком быстро двигалось
    pygame.time.Clock().tick(60)
