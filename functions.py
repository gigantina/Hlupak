import os
import sys
import pygame as pg

from gases_sprites import molecule_group





def main_title():
    title("Симуляторы физических явлений")


def title(caption):
    pg.display.set_caption(caption)


def theory(name):
    f = open(name, 'r', encoding='utf-8')
    lines = ''.join(f.readlines())
    f.close()
    return lines

def kill_15():
    k = 0
    for i in molecule_group:
        i.kill()
        k += 1
        if k == 15:
            break
