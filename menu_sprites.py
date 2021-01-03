import pygame as pg
import sys
import os
import random
from functions import *
from gases import start_gases
from lever import start_lever

menu_group = pg.sprite.Group()
FUNCTIONS = [start_lever, start_gases]

class ObjectMenu(pg.sprite.Sprite):
    """Класс объекта меню"""

    def __init__(self, x, y, image_path, desc, func):
        super().__init__(menu_group)
        image = load_image(image_path)
        image = pg.transform.scale(image, (350, 250))
        self.image = pg.Surface((500, 300),
                                pg.SRCALPHA, 32)
        self.image.blit(image, (0, 20))
        self.rect = pg.Rect(x, y, 500, 300)
        self.func = func
        font = pg.font.Font(None, 30)
        text = font.render(desc, 1, (201, 37, 237))
        self.image.blit(text, (40, 0))

    def update(self, pos) -> None:
        x, y = pos
        if self.rect.collidepoint(x, y):
            self.func()

ObjectMenu(10, 10, "gases.png", "Симуляция идеального газа", start_gases)
ObjectMenu(10, 300, "lever.png", "Симуляция рычага", start_lever)
