import pygame as pg
import pygame_gui
from all_sprites import Leaders
from all_sprites import Menu
from all_sprites import ScoreDisplay

pg.init()

pg.display.set_caption("2048 2.0")  # заголовок

size = width, height = 360, 540

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


def draw_logo():
    text_logo = "2048"
    font = pg.font.Font(None, 60)
    text = font.render(text_logo, 1, (0, 200, 0))
    screen.blit(text, (10, 10))


ui_sprites = pg.sprite.Group()

score = "0"
def draw_all_ui():
    ScoreDisplay(ui_sprites, 123, 10, 100, 70, score)
    Menu(ui_sprites, 230, 10, 100, 30)
    Leaders(ui_sprites, 230, 50, 100, 30)
    draw_logo()


def update_score(delta):
    global score
    score = int(score)
    score += delta
    score = str(score)

while run:
    screen.fill(pg.Color(color))
    draw_all_ui()

    time_delta = clock.tick(60) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            update_score(100)
            ui_sprites.update(event)
            coords = event.pos
    ui_sprites.draw(screen)

    pg.display.flip()  # Обновление кадра
pg.quit()
