import pygame as pg
import sys
import os
import random
from gases import start_gases
menu_group = pg.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class GasesMenu(pg.sprite.Sprite):
    """Один из классов меню, где газы, чтобы запускать эту симуляцию"""

    def __init__(self, x, y):
        super().__init__(menu_group)
        image = load_image("gases.png")
        image = pg.transform.scale(image, (350, 250))
        self.image = pg.Surface((500, 300),
                                pg.SRCALPHA, 32)
        self.image.blit(image, (0, 20))
        self.rect = pg.Rect(x, y, 500, 300)

        font = pg.font.Font(None, 30)
        text = font.render(str(f"Симуляция идеального газа"), 1, (201, 37, 237))
        self.image.blit(text, (40, 0))

    def update(self, pos) -> None:
        x, y = pos
        if self.rect.collidepoint(x, y):
            start_gases()

GasesMenu(10, 10)
