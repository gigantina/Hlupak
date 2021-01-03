import os
import sys
import pygame as pg
from all_sprites import all_sprites, Border


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


def main_title():
    title("Симуляторы физических явлений")


def title(caption):
    pg.display.set_caption(caption)


def clear_group():
    global all_sprites
    for i in all_sprites:
        i.kill()


def borders(width, height):
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
