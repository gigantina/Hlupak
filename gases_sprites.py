import pygame as pg
import random
import groups
import all_sprites

all_sprites_group = all_sprites.all_sprites_group
horizontal_borders, vertical_borders = all_sprites.horizontal_borders, all_sprites.vertical_borders
molecule_group = groups.create_gases_groups()


class Molecule(pg.sprite.Sprite):
    """Класс молекулы"""

    def __init__(self, x, y, radius, color):
        super().__init__(all_sprites_group, molecule_group)
        self.radius = radius
        self.image = pg.Surface((2 * radius, 2 * radius),
                                pg.SRCALPHA, 32)
        pg.draw.circle(self.image, color,
                       (radius, radius), radius)
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-8, -3)
        self.vy = random.randrange(-8, -3)

    def update(self, real=False):
        """Обновление положения молекулы, а также скорость в зависимости от скорости(уже реальной, но она слишком огромная)"""
        self.rect = self.rect.move(self.vx, self.vy)
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pg.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        if real:
            """чтобы не сделать лишний класс реального газа, можно сделать так, чтобы по флагу были реализованы
                                                                                        столкновения молекул"""
            for mol in molecule_group:
                if mol != self and pg.sprite.collide_mask(self, mol):
                    if random.choice([True, False]):
                        self.vx *= -1
                    if random.choice([True, False]):
                        self.vy *= -1
                    break

    def set_color(self, color):
        """изменяет цвет отдельной молекулы"""
        pg.draw.circle(self.image, color,
                       (self.radius, self.radius), self.radius)
