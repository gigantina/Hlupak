from functions import *
from gases import start_gases
from lever import start_lever
from realistic_gases import start_realistic_gases
from magnet import start_magnet
import functions

menu_group = pg.sprite.Group()


class ObjectMenu(pg.sprite.Sprite):
    """Класс объекта меню"""

    def __init__(self, x, y, image_path, desc, page, func):
        super().__init__()
        image = functions.load_image(image_path)
        image = pg.transform.scale(image, (350, 250))
        self.image = pg.Surface((500, 300),
                                pg.SRCALPHA, 32)
        self.image.blit(image, (0, 20))
        self.rect = pg.Rect(x, y, 500, 300)
        self.func = func
        font = get_font(30)
        text = font.render(desc, 1, (201, 37, 237))
        self.image.blit(text, (40, 0))
        self.page = page

    def update(self, pos, music) -> None:
        x, y = pos
        if self.rect.collidepoint(x, y):
            music.stop()
            self.func()
            music.play(-1)



