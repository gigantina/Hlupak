import pygame as pg
import sys
import os
import random
import groups
from functions import *
import all_sprites

all_sprites_group = all_sprites.all_sprites_group
lever_group, weights_group, fulcrum_group = groups.create_lever_groups()


class Lever(pg.sprite.Sprite):
    """Класс рычага"""

    def __init__(self, x1, y1, image_path):
        super().__init__(all_sprites_group, lever_group)
        self.image = pg.Surface(load_image(image_path))
        self.rect = pg.Rect(x1, y1)

    """Поворот рычага в случае неравенства моментов сил с двух сторон рычага"""

    def right(self):
        pass

    def left(self):
        pass

    def equal(self):
        pass


class Weight(pg.sprite.Sprite):
    """Класс любого груза"""

    def __init__(self, x, y, image_path, value):
        super().__init__(all_sprites_group, weights_group)
        self.image = pg.Surface(load_image(image_path))
        self.power = value * 10  # сила тяжести груза
        self.rect = pg.Rect(x, y)

    """Здесь будет перетаскивание предмета"""


class Fulcrum(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__(all_sprites_group, weights_group)
        self.image = pg.Surface(load_image(image_path))
        self.value = 0.5
        self.rect = pg.Rect(x, y)

    """Здесь будет изменение значение self.value, т.е изменение положения точки опоры рычага"""
