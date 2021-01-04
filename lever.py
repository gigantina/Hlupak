import pygame as pg
import math
import os
import sys
import random
from functions import *
from all_sprites import Border, all_sprites_group
from lever_sprites import Lever, Fulcrum, Weight, weights_group, lever_group, fulcrum_group

pg.init()

pg.display.set_caption("Симулятор рычага")  # заголовок

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
F1 = 10
l1 = 4
F2 = 20
l2 = 2

# Немного теории, мы делаем идеальный газ, где молекулы не сталкиваются друг с другом


Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def left_moment():
    return F1 * l1


def right_moment():
    return F2 * l2


def show_parametrs():
    font = pg.font.Font(None, 30)
    text = font.render(str(f"Момент силы правого плеча: {right_moment()}Н*м"), 1, BLACK)
    screen.blit(text, (10, 40))
    text = font.render(str(f"Момент силы левого плеча: {left_moment()}Н*м"), 1,
                       BLACK)
    screen.blit(text, (10, 10))


def start_lever():
    global N, T
    clear_group()
    run = True
    title("Симулятор рычага")
    SPEED = 60
    fon()

    while run:
        fon()
        all_sprites_group.update()
        all_sprites_group.draw(screen)
        lever = Lever(width - 100, height - 100, 10, (0, 0, 0))

        time_delta = clock.tick(SPEED) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    m1 = left_moment()
                    m2 = right_moment()
                    if m1 == m2:
                        print('УРАВНОВЕШЕНО')
                        # lever.equal()
                    elif m1 > m2:
                        print('')
                        # lever.left()
                    else:
                        print('')
                        # lever.right()
        show_parametrs()

        pg.display.flip()  # Обновление кадра

    N = 0
    T = 100  # K