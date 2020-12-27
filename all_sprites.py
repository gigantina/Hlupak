import pygame as pg
import sys
import os

tile_width = tile_height = 100

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class Grass(pg.sprite.Sprite):
    def __init__(self, all_sprites, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = pg.transform.scale(load_image('grass2.png'), (tile_width, tile_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)




def terminate():
    pg.quit()
    sys.exit()

def menu_screen(screen):
    intro_text = ''

    menu = pg.Surface((360, 540), pg.SRCALPHA, 32)
    font = pg.font.Font(None, 30)
    text_coord = 50
    menu.blit(screen, (0, 0))
    for line in intro_text:
       pass
    run = True
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pg.display.flip()


