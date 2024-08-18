import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width = 640
height = 480

# Определение цветов
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Создание игрового окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Определение параметров змейки
snake_block = 10
snake_speed = 15

# Определение шрифта для отображения счета
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
    pygame.display.update()


# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    # Изначальное положение змейки
    x1 = width / 2
    y1 = height / 2

    # Изменение координат змейки при движении
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Генерация случайных координат для яблока появляющегося на экране
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Основной цикл игры
    while not game_over:

        while game_close:
            screen.fill(white)
            message("Вы проиграли! Нажмите Q-Выход или C-Сыграть заново", red)
            pygame.display.update()

            # Обработка нажатий клавиш при завершении игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка нажатий клавиш во время игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка на выход змейки за границы экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Изменение координат змейки при движении
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаление лишних сегментов змейки, если ее длина превышает длину
        # одного сегмента
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка на столкновение с собственным телом змейки
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Отображение змейки на экране
        our_snake(snake_block, snake_list)

        # Отображение счета
        score = length_of_snake - 1
        score_text = score_font.render("Счет: " + str(score), True, black)
        screen.blit(score_text, [0, 0])
        pygame.display.update()

        # Проверка на поедание яблока и генерацию нового
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Установка скорости змейки
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()


# Запуск игры
game_loop()