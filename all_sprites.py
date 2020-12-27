import pygame as pg
import sys

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


