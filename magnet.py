from functions import *
from all_sprites import Border, load_image, theory_group, Theory, all_sprites_group
from magnet_sprites import Lode, lode_group, Compass, compass_group, Arrow, arrow_group

pg.init()

pg.display.set_caption("Симулятор магнитной стрелки")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)

THEORY_TEXT = theory('lever.txt')


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def show_parametrs():
    font = pg.font.Font(None, 30)
    text = font.render(str(f""), 1, BLACK)
    screen.blit(text, (10, 40))
    text = font.render(str(""), 1,
                       BLACK)
    screen.blit(text, (10, 10))


def start_magnet():
    global N, T
    clear_group(all_sprites_group)
    run = True
    title("Симулятор магнитной стрелки")
    offset_x = 0
    offset_y = 0
    fon()
    SPEED = 60
    LENGHT = 50
    last_angle = 0
    lode = Lode(20, 20)
    compass = Compass(550, 200)
    arrow = Arrow(625, 245, 50)
    moving = False
    theory = Theory(10, height - 50, 20, "#00ff00")
    while run:
        fon()
        all_sprites_group.update()
        all_sprites_group.draw(screen)
        x, y, w, h = lode.rect
        point = x+w, y+(lode.rect.h // 2)
        radius, angle = arrow.polar(point)

        if radius < 250:
            arrow.rotate(-angle-90)
            last_angle = angle-90
        else:
                arrow.rotate(0)
            # TODO плавный переход стрелки на исходную позицию
        time_delta = clock.tick(SPEED) / 1000.0
        theory_group.draw(screen)

        show_parametrs()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lode.rect.collidepoint(event.pos):
                        moving = True
                        mouse_x, mouse_y = event.pos
                        offset_x = lode.rect.x - mouse_x
                        offset_y = lode.rect.y - mouse_y
                        break

            if event.type == pg.MOUSEBUTTONUP:
                if theory.rect.collidepoint(event.pos):
                    theory.open_theory(screen, THEORY_TEXT)
                if event.button == 1:
                    moving = False
                else:
                    lode.rotate()
                    arrow.change()
            if event.type == pg.MOUSEMOTION:
                if moving:
                    mouse_x, mouse_y = event.pos
                    lode.rect.x = mouse_x + offset_x
                    lode.rect.y = mouse_y + offset_y




        pg.display.flip()  # Обновление кадра
