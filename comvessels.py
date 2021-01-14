from functions import *
from all_sprites import Border, load_image, theory_group, Theory, all_sprites_group
from comvessels_sprites import Vessels, Button, Liquid, Vessel, choice_group

pg.init()

pg.display.set_caption("Симулятор сообщающихся сосудов")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

clock = pg.time.Clock()

RED = (255, 0, 0)

r1, h1 = 0, 1.5
r2, h2 = 0, 1.5
p = 0

changing_pos = False
BLACK = (0, 0, 0)

THEORY_TEXT = theory('vessels.txt')


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def show_parametrs():
    font = pg.font.Font(None, 30)
    text = font.render(str(f"Давление пр. сосуда: {p / 1000}КПа"), 1, BLACK)
    screen.blit(text, (width - 400, 10))
    text = font.render(str(f"Плот. пр. жидкости: {r2}г/см3"), 1,
                       BLACK)
    screen.blit(text, (width - 400, 40))
    text = font.render(str(f"Высота пр. жикости: {round(h2, 2)}м"), 1,
                       BLACK)
    screen.blit(text, (width - 400, 70))
    text = font.render(str(f"Давление лев. сосуда: {p / 1000}КПа"), 1,
                       BLACK)
    screen.blit(text, (10, 10))
    text = font.render(str(f"Плот. лев. жидкости: {r1}г/см3"), 1,
                       BLACK)
    screen.blit(text, (10, 40))
    text = font.render(str(f"Высота лев. жидкости: {round(h1, 2)}м"), 1,
                       BLACK)
    screen.blit(text, (10, 70))


def calculating_h1():
    global p, r1
    h = p / r1 / 10000
    return h


def calculating_h2():
    global p, r2
    h = p / r2 / 10000
    return h


def start_vessel():
    global r1, r2, h1, h2, p
    clear_group(all_sprites_group)
    run = True
    title("Симулятор сообщающихся сосудов")
    fon()
    SPEED = 60
    theory = Theory(10, height - 50, 20, "#00ff00")
    vessels = Vessels(380, 100)
    water = Liquid(pg.Color("#1CA3EC"), 1)
    mercury = Liquid(pg.Color("#DBCECA"), 13.6)
    oil = Liquid(pg.Color("#373A36"), 0.8)

    first_vessel = Vessel(400, 109, water, h1)
    second_vessel = Vessel(690, 110, water, h2)

    r1 = first_vessel.liquid.r
    r2 = second_vessel.liquid.r

    p = r1 * h1 * 10000
    WHITE = pg.Color(255, 255, 255)

    water_button_1 = Button(10, 120, WHITE, water, 1, "Вода")
    mercury_button_1 = Button(120, 120, WHITE, mercury, 1, "Ртуть")
    oil_button_1 = Button(230, 120, WHITE, oil, 1, "Нефть")

    water_button_2 = Button(10, 420, WHITE, water, 2, "Вода")
    mercury_button_2 = Button(120, 420, WHITE, mercury, 2, "Ртуть")
    oil_button_2 = Button(230, 420, WHITE, oil, 2, "Нефть")
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
                    for button in choice_group:
                        if button.rect.collidepoint(event.pos):
                            if button.side == 1:
                                first_vessel.liquid = button.liquid

                                r1 = button.liquid.r
                                h1 = calculating_h1()
                                first_vessel.height_liquid = h1 * 100
                                first_vessel.draw_liquid()
                            else:
                                second_vessel.liquid = button.liquid
                                r2 = button.liquid.r
                                h2 = calculating_h2()
                                second_vessel.height_liquid = h2 * 100
                                second_vessel.draw_liquid()

            if event.type == pg.MOUSEBUTTONUP:
                if theory.rect.collidepoint(event.pos):
                    theory.open_theory(screen, THEORY_TEXT)

        show_parametrs()

        pg.display.flip()  # Обновление кадра