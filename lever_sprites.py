import pygame as pg
import sys
import os
import random
import groups
from functions import *
import all_sprites

all_sprites_group = all_sprites.all_sprites_group
lever_group, weights_group, fulcrum_group, points_group = groups.create_lever_groups()


class Lever(pg.sprite.Sprite):
    """Класс рычага"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, lever_group)
        self.image = load_image("lever_sprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_des = 0
        self.y_des = 0
        self.weight = value * 10
        self.moving = False
        self.orientation = None

    """Здесь будет перетаскивание предмета"""


class Fulcrum(pg.sprite.Sprite):
    """Класс рычага"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, lever_group)
        self.image = load_image("fulcrum.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    """Поворот рычага в случае неравенства моментов сил с двух сторон рычага"""

    def right(self):
        pass

    def left(self):
        pass

    def equal(self):
        pass


class Point(pg.sprite.Sprite):
    def __init__(self, x, y, lenght, orientation):
        super().__init__(all_sprites_group, points_group)
        self.image = pg.Surface((3, 30))
        self.rect = pg.Rect(x, y, 3, 30)
        self.color = (0, 0, 0)
        self.colored = False
        self.lenght = lenght
        self.orientation = orientation
