from functions import *
from all_sprites import Border, theory_group, Theory, all_sprites_group
from lever_sprites import Lever, Point, Fulcrum, Weight, weights_group, lever_group, fulcrum_group, points_group
import functions

pg.init()

pg.display.set_caption("Симулятор рычага")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)
lever = {}

THEORY_TEXT = theory('lever.txt')


def fon():
    fon = pg.transform.scale(load_image('green.png'), (width, height))
    screen.blit(fon, (0, 0))


def clear_group():
    global all_sprites_group
    for i in all_sprites_group:
        i.kill()


def left_moment():
    F = 0
    for id in lever:
        if lever[id][0]:
            F += (lever[id][1] * lever[id][2] / 10)
    return F


def right_moment():
    F = 0
    for id in lever:
        if not lever[id][0]:
            F += (lever[id][1] * lever[id][2] / 10)
    return F


def show_parametrs():
    font = get_font(30)
    text = font.render(str(f"Момент силы правого плеча: {right_moment()}Н*м"), 1, BLACK)
    screen.blit(text, (10, 40))
    text = font.render(str(f"Момент силы левого плеча: {left_moment()}Н*м"), 1,
                       BLACK)
    screen.blit(text, (10, 10))


# TODO исправить баг, что когда рычаг поворачивается, а точки нет
def start_lever():
    global N, T
    clear_group()
    run = True
    title("Симулятор рычага")
    offset_x = 0
    offset_y = 0
    fon()
    SPEED = 60
    BORDER = 10
    theory = Theory(10, height - 50, 20, "#00ff00")
    lever_sprite = Lever(BORDER, 250)
    fulcrum = Fulcrum(393, 225)
    orient = True
    for i in range(20):
        Point((BORDER - 1) + 40 * i + 10, 250, i, orient)
        if i == 9:
            orient = False
    for point in points_group:
        if point.orientation:
            lever[point.id] = [point.orientation, 10 - point.id, 0]
        else:
            lever[point.id] = [point.orientation, point.id - 9, 0]
    moving = False
    Weight(40, 100, 'weight_5kg.png', 5)
    Weight(80, 100, 'weight_10kg.png', 10)
    Weight(120, 100, 'weight_3kg.png', 3)
    Weight(160, 100, 'weight_20kg.png', 20)
    Weight(200, 100, 'weight_2kg.png', 2)
    while run:
        fon()
        all_sprites_group.update()
        all_sprites_group.draw(screen)

        time_delta = clock.tick(SPEED) / 1000.0
        theory_group.draw(screen)

        show_parametrs()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_title()
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                for weight in weights_group:
                    if weight.rect.collidepoint(event.pos):
                        moving = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weight.rect.x - mouse_x
                        offset_y = weight.rect.y - mouse_y
                        break
                print(event.pos)

            if event.type == pg.MOUSEBUTTONUP:
                if theory.rect.collidepoint(event.pos):
                    theory.open_theory(screen, THEORY_TEXT)
                if event.button == 1:
                    moving = False
                for point in points_group:
                    hits = pg.sprite.spritecollide(point, weights_group, False)
                    if hits:
                        weight_all = 0
                        for sprite in hits:
                            weight_all += sprite.weight
                        lever[point.id][2] = weight_all
                    else:
                        lever[point.id][2] = 0

            if event.type == pg.MOUSEMOTION:
                if moving:
                    mouse_x, mouse_y = event.pos
                    weight.rect.x = mouse_x + offset_x
                    weight.rect.y = mouse_y + offset_y
        m1 = left_moment()
        m2 = right_moment()
        if m1 == m2:
            lever_sprite.equal()
        elif m1 > m2:
            lever_sprite.left()
        else:
            lever_sprite.right()
            for point_sprite in points_group:
                point_sprite.right()
        pg.display.flip()  # Обновление кадра
