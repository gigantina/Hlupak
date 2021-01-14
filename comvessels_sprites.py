import pygame as pg
import sys
import os
import random
import groups
from functions import *
import all_sprites

all_sprites_group = all_sprites.all_sprites_group
vessel_group, liquid_group, choice_group = groups.create_vessel_groups()


class Vessel(pg.sprite.Sprite):
    """Класс сосуда"""

    def __init__(self, x, y):
        super().__init__(all_sprites_group, vessel_group)
        self.image = all_sprites.load_image("vessel.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
