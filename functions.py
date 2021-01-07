import os
import sys
import pygame as pg


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


def theory(name):
    f = open(name, 'r', encoding='utf-8')
    lines = ''.join(f.readlines())
    f.close()
    return lines
