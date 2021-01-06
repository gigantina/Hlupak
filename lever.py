import pygame as pg
import math
import os
import sys
import random
from functions import *
from all_sprites import Border, all_sprites_group, theory_group, Theory
from lever_sprites import Lever, Point, Fulcrum, Weight, weights_group, lever_group, fulcrum_group, points_group

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
lever_board = [[0 for i in range(10)], [0 for _ in range(10)]]
lever_board_r = list(range(10, 0, -1)) + list(range(1, 11))


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def clear_group():
    global all_sprites_group
    for i in all_sprites_group:
        i.kill()


def left_moment():
    F = 0
    for i in range(len(lever_board[0])):
        F += ((lever_board_r[i] * lever_board[0][i]) / 10)
    return F


def right_moment():
    F = 0
    for i in range(len(lever_board[0])):
        F += ((lever_board_r[i + 9] * lever_board[1][i]) / 10)
    return F


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
    offset_x = 0
    offset_y = 0
    fon()
    SPEED = 60
    BORDER = 10
    theory = Theory(10, height - 50, 20, "#00ff00")
    lever = Lever(BORDER, 250)
    orient = True
    for i in range(20):
        Point((BORDER - 1) + 40 * i + 10, 250, lever_board_r[i], orient)
        if i == 10:
            orient = False
    fulcrum = Fulcrum(393, 225)
    moving = False
    Weight(40, 40, 'weight_5kg.png', 5)
    Weight(40, 60, 'weight_5kg.png', 10)
    while run:
        fon()
        all_sprites_group.update()
        all_sprites_group.draw(screen)

        time_delta = clock.tick(SPEED) / 1000.0
        theory_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                m1 = left_moment()
                m2 = right_moment()
                for weight in weights_group:
                    if weight.rect.collidepoint(event.pos):
                        moving = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weight.rect.x - mouse_x
                        offset_y = weight.rect.y - mouse_y
                        break
                for point in points_group:
                    for weight_for_points in weights_group:
                        if weight_for_points.rect.collidepoint(point.rect.x, point.rect.y):
                            if point.orientation:
                                weight.orientation = True
                                lever_board[0][10 - point.lenght] = weight.weight
                            else:
                                weight.orientation = False
                                lever_board[1][point.lenght - 1] = weight.weight
                        else:
                            if point.orientation:
                                lever_board[0][10 - point.lenght] = 0
                            else:
                                lever_board[1][point.lenght - 1] = 0

                if m1 == m2:
                    print('УРАВНОВЕШЕНО')
                    # lever.equal()
                elif m1 > m2:
                    print('')
                    # lever.left()
                else:
                    print('')
                    # lever.right()

            if event.type == pg.MOUSEBUTTONUP:
                if theory.rect.collidepoint(event.pos):
                    theory.open_theory(screen, "Тут текст для теории\n :)")
                if event.button == 1:
                    moving = False
                print(lever_board)

            if event.type == pg.MOUSEMOTION:
                if moving:
                    mouse_x, mouse_y = event.pos
                    weight.rect.x = mouse_x + offset_x
                    weight.rect.y = mouse_y + offset_y
        show_parametrs()
        pg.display.flip()  # Обновление кадра
