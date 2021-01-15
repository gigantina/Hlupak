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
        self.image = all_sprites.load_image("lever_sprite.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orig = self.image

    """Поворот рычага в случае неравенства моментов сил с двух сторон рычага"""

    def rotate(self, angle):
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pg.transform.rotate(self.orig, angle)

    def right(self):
        self.rotate(-2)

    def left(self):
        self.rotate(2)

    def equal(self):
        self.rotate(0)


class Weight(pg.sprite.Sprite):
    """Класс любого груза"""

    def __init__(self, x, y, image_path, value):
        super().__init__(all_sprites_group, weights_group)
        self.image = all_sprites.load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_des = 0
        self.y_des = 0
        self.weight = value * 10
        self.moving = False
        self.orientation = None


class Fulcrum(pg.sprite.Sprite):
    """Класс рычага"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, lever_group)
        self.image = all_sprites.load_image("fulcrum.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Point(pg.sprite.Sprite):
    def __init__(self, x, y, id, orientation):
        super().__init__(all_sprites_group, points_group)
        self.image = pg.Surface((3, 30), pg.SRCALPHA)
        self.rect = pg.Rect(x, y, 3, 30)
        self.colored = False
        self.id = id
        self.orientation = orientation
        self.orig = self.image

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def rotate(self, angle):
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pg.transform.rotate(self.orig, angle)

    def right(self):
        self.rotate(-1)

    def left(self):
        self.rotate(1)

    def equal(self):
        self.rotate(0)