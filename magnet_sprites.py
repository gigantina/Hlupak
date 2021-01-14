import pygame as pg
import sys
import os
import random
import groups
from functions import *
import all_sprites

all_sprites_group = all_sprites.all_sprites_group
lode_group, arrow_group, compass_group = groups.create_magnet_groups()

RED = pg.Color(255, 0, 0)
BLUE = pg.Color(0, 0, 255)


class Lode(pg.sprite.Sprite):
    """Класс магнита"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, lode_group)
        self.width = 300
        self.height = 75

        self.is_rotate = False
        self.image = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.rect = pg.Rect(x, y, 300, 75)
        self.rect.x = x
        self.rect.y = y
        self.x_des = 0
        self.y_des = 0
        self.rotate()

    def rotate(self):
        self.is_rotate = not self.is_rotate
        if not self.is_rotate:
            pg.draw.rect(self.image, RED, pg.Rect(0, 0, self.width / 2, self.height))
            pg.draw.rect(self.image, BLUE, pg.Rect(self.width / 2, 0, self.width / 2, self.height))
        else:
            pg.draw.rect(self.image, BLUE, pg.Rect(0, 0, self.width / 2, self.height))
            pg.draw.rect(self.image, RED, pg.Rect(self.width / 2, 0, self.width / 2, self.height))


class Arrow(pg.sprite.Sprite):
    """Класс стрелки"""

    def __init__(self, x, y, lenght):
        super().__init__(all_sprites_group, arrow_group)
        self.lenght = lenght
        self.image = pg.Surface((self.lenght, self.lenght * 2), pg.SRCALPHA)
        self.draw_arrow()
        self.rect = pg.Rect(x, y, self.lenght, 2 * self.lenght)
        self.orig_rect = self.rect
        self.rect.x = x
        self.rect.y = y
        self.orig = self.image
        self.is_changed = False
        self.addictional = 0

    def change(self):
        self.is_changed = not self.is_changed
        if self.is_changed:
            self.addictional = 180
        else:
            self.addictional = 0


    def polar(self, coord):
        x, y, w, h = self.rect
        direction = coord - pg.Vector2(x + w // 2, y + h // 2)
        radius, angle = direction.as_polar()
        return (radius, angle)

    def draw_arrow(self, color_1=BLUE, color_2=RED):
        pg.draw.polygon(self.image, color_1, [(self.lenght / 2, 0), (0, self.lenght), (self.lenght, self.lenght)])
        pg.draw.polygon(self.image, color_2,
                        [(0, self.lenght), (self.lenght, self.lenght), (self.lenght / 2, self.lenght * 2)])

    def rotate(self, angle):
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pg.transform.rotate(self.orig, angle)


class Compass(pg.sprite.Sprite):
    """Класс рычага"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, compass_group)
        self.image = all_sprites.load_image("compass.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
