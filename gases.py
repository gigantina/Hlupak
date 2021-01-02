import pygame as pg
import math
import pygame_gui
import os
import sys
import random
from all_sprites import Molecule, Border, all_sprites, molecule_group, horizontal_borders, vertical_borders

pg.init()

pg.display.set_caption("Симулятор газа")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

"""А вот тут будет волшебство)"""
clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)

"""Физичиские величины"""
T = 100  # K
G = 9.8  # м/с**2
P = 101325  # Па, давление воздуха
M = 4.82 * (10 ** -26)  # масса малекулы воздуха
N = 0
K = 1.38 * (10 ** -23)  # Постоянная Больцмана


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


# Немного теории, мы делаем идеальный газ, где молекулы не сталкиваются друг с другом


Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)


def fon():
    fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    screen.blit(fon, (0, 0))


def create_molecule():
    """Создает по 15 молекул"""
    global N
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(15):
        Molecule(width - 100, height - 100, 10, color)
    N += 15


def calculating_the_average_speed_of_molecules():
    """Рассчитывает среднюю квадратичную скорость молекул"""
    V = math.sqrt((3 * K * T) / M)
    return V


def calculating_the_pressure():
    """Возвращает давление, которое газ оказывает на стенки"""
    P = (N * M * pow(calculating_the_average_speed_of_molecules(), 2)) / 3
    return P


def change_t(num):
    """Эта функция увеличивает температуру в кельвинах на 10 кельвинов"""
    global T
    T += num


def show_parametrs():
    font = pg.font.Font(None, 30)
    text = font.render(str(f"Температура: {T}K/ {round(T - 273.15)}C"), 1, BLACK)
    screen.blit(text, (width - 300, 10))
    text = font.render(str(f"Скорость молекул: {round(calculating_the_average_speed_of_molecules())}м/с"), 1, BLACK)
    screen.blit(text, (width - 300, 40))
    text = font.render(str(f"Давление: {calculating_the_pressure()}Па"), 1,
                       BLACK)
    screen.blit(text, (10, 10))



def start_game():
    run = True
    SPEED = 60
    create_molecule()
    while run:
        fon()
        all_sprites.update()
        all_sprites.draw(screen)
        time_delta = clock.tick(SPEED) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    create_molecule()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if T > 10:
                        change_t(-10)
                        SPEED -= 5
                if event.key == pg.K_UP:
                    change_t(10)
                    SPEED += 5

        show_parametrs()

        pg.display.flip()  # Обновление кадра