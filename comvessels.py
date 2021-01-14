from functions import *
from all_sprites import Border, load_image, theory_group, Theory, all_sprites_group
from comvessels_sprites import Vessel

pg.init()

pg.display.set_caption("Симулятор сообщающихся сосудов")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)

THEORY_TEXT = theory('vessels.txt')


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def show_parametrs():
    font = pg.font.Font(None, 30)
    text = font.render(str(""), 1, BLACK)
    screen.blit(text, (10, 40))


def start_vessel():
    global N, T
    clear_group(all_sprites_group)
    run = True
    title("Симулятор сообщающихся сосудов")
    fon()
    SPEED = 60
    theory = Theory(10, height - 50, 20, "#00ff00")
    while run:
        fon()
        all_sprites_group.update()
        all_sprites_group.draw(screen)

        time_delta = clock.tick(SPEED) / 1000.0
        theory_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(1)

            if event.type == pg.MOUSEBUTTONUP:
                if theory.rect.collidepoint(event.pos):
                    theory.open_theory(screen, THEORY_TEXT)

        pg.display.flip()  # Обновление кадра
