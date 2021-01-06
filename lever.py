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
F1 = 0
l1 = 0
F2 = 0
l2 = 0



def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))

def clear_group():
    global all_sprites_group
    for i in all_sprites_group:
        i.kill()

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
        lever = Lever(95, 250)
        fulcrum = Fulcrum(406, 225)

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
