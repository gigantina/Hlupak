import pygame as pg
import pygame_gui
from all_sprites import Leaders
from all_sprites import Menu
from all_sprites import ScoreDisplay
from all_sprites import menu_screen

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

manager = pygame_gui.UIManager((width, height))

def draw_logo():
    text_logo = "2048"
    font = pg.font.Font(None, 60)
    text = font.render(text_logo, 1, (0, 200, 0))
    screen.blit(text, (10, 10))


ui_sprites = pg.sprite.Group()

score = "0"
score_board = ''
def draw_all_ui():
    global score_board
    score_board = ScoreDisplay(ui_sprites, 123, 10, 100, 70, score)
    Menu(ui_sprites, 230, 10, 100, 30, screen)
    Leaders(ui_sprites, 230, 50, 100, 30)
    draw_logo()


def update_score(delta):
    global score
    score = int(score)
    score += delta
    score = str(score)

draw_all_ui()

while run:
    screen.fill(pg.Color(color))
    draw_logo()
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
            update_score(100)
            score_board = ScoreDisplay(ui_sprites, 123, 10, 100, 70, score)
            coords = event.pos
            ui_sprites.update(event)
    ui_sprites.draw(screen)

    pg.display.flip()  # Обновление кадра
pg.quit()
