import pygame as pg
import pygame_gui
import os
import sys
from all_sprites import menu_screen

pg.init()

pg.display.set_caption(" ")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size, pg.RESIZABLE)
color = "white"
screen.fill(pg.Color(color))
pg.display.update()
count = 0
run = True  # переменна, с помощью ее можно выходить из цикла

"""А вот тут будет волшебство)"""
clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False

manager = pygame_gui.UIManager((width, height))

ui_sprites = pg.sprite.Group()
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image



def fon():
    fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    screen.blit(fon, (0, 0))


while run:
    fon()
    time_delta = clock.tick(60) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                rect=pg.Rect((250, 200), (300, 200)),
                manager=manager,
                window_title="Подтверждение",
                action_long_desc="Вы точно хотите выйти?",
                action_short_name="Ok",
                blocking=True
            )
            run = False

        if event.type == pg.USEREVENT:
            if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                run = False
        if event.type == pg.MOUSEBUTTONUP:
            pass
    ui_sprites.draw(screen)

    pg.display.flip()  # Обновление кадра
pg.quit()
