import os
import sys
import math
import pygame as pg

from gases_sprites import molecule_group


def calculating_the_average_speed_of_molecules(K, M, T):
    """Рассчитывает среднюю квадратичную скорость молекул"""
    V = math.sqrt((3 * K * T) / M)
    return V


def calculating_the_pressure(K, M, T, N):
    """Возвращает давление, которое газ оказывает на стенки"""
    P = (N * M * pow(calculating_the_average_speed_of_molecules(K, M, T), 2)) / 3
    return P


def change_t(num):
    """Эта функция увеличивает температуру в кельвинах на 10 кельвинов"""
    global T
    T += num


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
