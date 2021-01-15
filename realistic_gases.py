import pygame as pg
import math
import random
from functions import *
from all_sprites import Border, all_sprites_group, theory_group, Theory
from gases_sprites import Molecule, molecule_group

pg.init()

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
M = 4.82 * (10 ** -26)  # масса молекулы воздуха(кг)
N = 0
K = 1.38 * (10 ** -23)  # Постоянная Больцмана

# Немного теории, мы делаем идеальный газ, где молекулы не сталкиваются друг с другом
THEORY_TEXT = theory('real_gases.txt')


def fon():
    fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    screen.blit(fon, (0, 0))


def borders(width, height):
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)


def create_molecule():
    """Создает по 15 молекул"""
    global N, molecule_group
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in molecule_group:
        i.set_color((200, 200, 200))
    for i in range(15):
        Molecule(random.randint(40, width - 40), random.randint(40, height - 40), 5, color)
    N += 15


def show_parametrs():
    font = get_font(30)
    text = font.render(str(f"Температура: {T}K/ {round(T - 273.15)}C"), 1, BLACK)
    screen.blit(text, (width - 300, 10))
    text = font.render(str(f"Скорость молекул: {round(calculating_the_average_speed_of_molecules(K, M, T))}м/с"), 1,
                       BLACK)
    screen.blit(text, (width - 300, 40))
    text = font.render(str(f"Давление: {calculating_the_pressure(K, M, T, N)}Па"), 1,
                       BLACK)
    screen.blit(text, (10, 10))


def start_realistic_gases():
    global N, T
    clear_group(all_sprites_group)
    borders(width, height)
    run = True
    title("Симулятор реального газа")
    SPEED = 60
    create_molecule()
    fon()
    pause = False
    theory = Theory(10, height - 50, 20, "#00ff00")
    while run:
        fon()
        if not pause:
            all_sprites_group.update(True)
        all_sprites_group.draw(screen)

        time_delta = clock.tick(SPEED) / 1000.0

        show_parametrs()
        theory_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if theory.rect.collidepoint(event.pos[0], event.pos[1]):
                        theory.open_theory(screen, THEORY_TEXT)
                    else:
                        create_molecule()
                elif event.button == 3:
                    kill_15()
                    if N != 0:
                        N -= 15
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if T > 10:
                        T = change_t(-10, T)
                        SPEED -= 5
                if event.key == pg.K_UP:
                    T = change_t(10, T)
                    SPEED += 5
                if event.key == pg.K_SPACE:
                    pause = not pause

        pg.display.flip()  # Обновление кадра

    N = 0
    T = 100  # K
