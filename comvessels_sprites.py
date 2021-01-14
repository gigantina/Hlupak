import pygame as pg
import sys
import os
import random
import groups
from functions import *
import all_sprites


class Liquid():
    def __init__(self, color, r):
        self.color = color
        self.height_liquid = 0
        self.r = r


all_sprites_group = all_sprites.all_sprites_group
vessel_group, liquid_group, choice_group = groups.create_vessel_groups()


class Vessels(pg.sprite.Sprite):
    """Класс сосуда"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, vessel_group)
        self.image = all_sprites.load_image("vessel.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pg.sprite.Sprite):

    def __init__(self, x, y, color, liquid, side, text):
        super().__init__(all_sprites_group, choice_group)
        self.height = 30
        self.width = 100

        self.liquid = liquid
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side

        pg.draw.rect(self.image, color, pg.Rect(0, 0, self.width, self.height))

        font = pg.font.Font(None, 30)
        p = font.render(text, 1,
                        (0, 0, 0))
        self.image.blit(p, (12, 5))


class Vessel(pg.sprite.Sprite):

    def __init__(self, x, y, liquid, h):
        super().__init__(all_sprites_group, liquid_group)
        self.width = 57
        self.height = 333
        self.liquid = liquid
        self.height_liquid = h * 100

        self.image = pg.Surface((self.width, self.height), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.draw_liquid()

    def draw_liquid(self):
        pg.draw.rect(self.image, pg.Color(255, 255, 255), pg.Rect(0, 0, self.width, self.height))
        pg.draw.rect(self.image, self.liquid.color,
                     pg.Rect(0, self.height - self.height_liquid, self.width, self.height_liquid))
