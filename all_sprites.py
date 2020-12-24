import pygame as pg


class Leaders(pg.sprite.Sprite):
    # TODO сделать базу данных с таблицей лидеров всех
    """Этот класс переводит нас на список всех лидеров"""

    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Лидеры", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=10)
        self.image.blit(self.text, (width // 7, height // 4))

        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            print("Таблицы лидеров")


class Menu(pg.sprite.Sprite):
    # TODO сделать главное меню
    """Этот класс - кнопка главного меню, чуть позже ее реализую"""

    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Меню", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=10)
        self.image.blit(self.text, (width // 4, height // 4))

        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            print("Меню")


class ScoreDisplay(pg.sprite.Sprite):
    # TODO Сделать так, чтобы значение внутри него менялось
    """Этот класс будет изображать счетчик очков"""

    def __init__(self, all_sprites, x, y, width, height, text):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Счет", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=20)
        self.image.blit(self.text, (width // 5, height // 7))
        self.text_score = text
        self.score = self.font.render(self.text_score, 1, (0, 0, 0))
        self.image.blit(self.score, (width // 5, height // 2))

        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            print("Счетчик")
