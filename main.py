import pygame as pg
import math
import os
from functions import main_title
import sys
import random
from functions import *
from gases import start_gases
from lever import start_lever
from realistic_gases import start_realistic_gases
from magnet import start_magnet
from comvessels import start_vessel
from menu_sprites import ObjectMenu, menu_group

pg.init()

main_title()

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

"""А вот тут будет волшебство)"""
clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)
page = 1

gases_obj = ObjectMenu(10, 10, "gases.png", "Симуляция идеального газа", 1, start_gases)
lever_obj = ObjectMenu(10, 300, "lever.png", "Симуляция рычага", 1, start_lever)
real_gases_obj = ObjectMenu(400, 10, "real_gases.png", "Симуляция реального газа", 1, start_realistic_gases)
magnet_obj = ObjectMenu(400, 300, "magnets.png", "Симуляция магнитной стрелки", 1, start_magnet)

vessel_obj = ObjectMenu(10, 10, "vas.png", "Сообщающийся сосуды", 2, start_vessel)

all_menu_obj = [gases_obj, lever_obj, real_gases_obj, magnet_obj, vessel_obj]





def fon():
    # fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    # screen.blit(fon, (0, 0))
    screen.fill((255, 255, 255))


def show_menu(page=1):
    for i in all_menu_obj:
        if i.page != page:
            i.kill()
        else:
            menu_group.add(i)
    font = get_font(20)
    text = font.render("Для перемещения по меню используйте стрелки", 1, BLACK)
    screen.blit(text, (450, 580))



SPEED = 60
while run:
    fon()
    show_menu(page)
    time_delta = clock.tick(SPEED) / 1000.0
    menu_group.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                menu_group.update(event.pos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                pass
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_RIGHT:
                page = 2
            if event.key == pg.K_LEFT:
                page = 1

    pg.display.flip()  # Обновление кадра

# TODO сделать сообщающиеся сосуды
# TODO можно сделать гарелку, у которой есть анимация, надо добавить анимацию
# TODO сделать симуляцию падающий шариков
# TODO Добавить частицы итд
