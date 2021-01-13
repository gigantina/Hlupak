import pygame as pg


def create_default_groups():
    horizontal_borders = pg.sprite.Group()
    vertical_borders = pg.sprite.Group()
    all_sprites = pg.sprite.Group()
    return horizontal_borders, vertical_borders, all_sprites


def create_gases_groups():
    molecule_group = pg.sprite.Group()
    return molecule_group


def create_lever_groups():
    lever_group = pg.sprite.Group()
    weights_group = pg.sprite.Group()
    fulcrum_group = pg.sprite.Group()
    points_group = pg.sprite.Group()
    return lever_group, weights_group, fulcrum_group, points_group


def create_theory_group():
    t = pg.sprite.Group()
    return t
