import pygame as pg
import groups
import functions
from functions import *

horizontal_borders, vertical_borders, all_sprites_group = groups.create_default_groups()

class Border(pg.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites_group)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


theory_group = groups.create_theory_group()


class Theory(pg.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super(Theory, self).__init__(theory_group)
        self.radius = radius
        self.image = pg.Surface((2 * radius, 2 * radius),
                                pg.SRCALPHA, 32)
        pg.draw.circle(self.image, pg.Color(color),
                       (radius, radius), radius)
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius)
        font = functions.get_font(30)
        text = font.render(str(f"?"), 1, (0, 0, 0))
        self.image.blit(text, (13, 10))

    def fon(self, screen):
        """изменяет фон"""
        size = width, height = 800, 600
        fon = pg.transform.scale(functions.load_image('blue-snow.png'), (width, height))
        screen.blit(fon, (0, 0))

    def draw_text(self, text, screen):
        """Выводим текст с теорией на экран"""
        text = text.split("\n")
        y = 100
        for t in text:
            font = functions.get_font(30)
            text = font.render(t, 1, (0, 0, 0))
            screen.blit(text, (60, y))
            y += 30

    def open_theory(self, screen, text):
        """Открывает окно с теорией"""
        last_capt = pg.display.get_caption()[0]
        functions.title("Немного теории")
        run = True
        self.fon(screen)
        self.draw_text(text, screen)
        while run:
            self.fon(screen)
            self.draw_text(text, screen)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP or event.type == pg.QUIT or event.type == pg.KEYUP \
                        and event.key == pg.K_ESCAPE:
                    functions.title(last_capt)
                    run = False
            pg.display.flip()
