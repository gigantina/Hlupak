import pygame as pg
import os
import sys
from functions import *
import functions

from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody

PPM = 20.0
SPEED = 60

TIME_STEP = 1.0 / SPEED

pg.init()

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

"""А вот тут будет волшебство)"""
clock = pg.time.Clock()

RED = (255, 0, 0)

BLACK = (0, 0, 0)


world = world(gravity=(0, -10)) # создание поля

ground_body = world.CreateStaticBody(
    position=(0, 10),
    shapes=polygonShape(box=(20, 0.5)),
)
ground_body2 = world.CreateStaticBody(
    position=(37, 10),
    shapes=polygonShape(box=(10, 0.5)),
)

ground_body3 = world.CreateStaticBody(
    position=(0, 0),
    shapes=polygonShape(box=(50, 1))

)

body = world.CreateStaticBody(position=(20, 15))
circle = body.CreateCircleFixture(radius=1, density=1, friction=0.3)


def create_circle():
    for i in range(5, 40, 5):
        """Создаем круги"""
        body = world.CreateDynamicBody(position=(i, 20))
        circle = body.CreateCircleFixture(radius=1, density=1, friction=0.3)

def create_polygons():
    for x in range(5, 40, 4):
        """Создаем прямоугольники"""
        body = world.CreateDynamicBody(position=(x, 30), angle=x)
        box = body.CreatePolygonFixture(box=(2, 1), density=1, friction=0.3)


create_circle()
colors = {
    staticBody: (255, 0, 255, 255),
    dynamicBody: (127, 127, 127, 255)
}

def my_draw_polygon(polygon, body, fixture):
    """Отрисовка прямоугольников"""
    vertices = [(body.transform * v) * PPM for v in polygon.vertices]
    vertices = [(v[0], height - v[1]) for v in vertices]
    pg.draw.polygon(screen, colors[body.type], vertices)

polygonShape.draw = my_draw_polygon

def my_draw_circle(circle, body, fixture):
    """Отрисовка круга"""
    position = body.transform * circle.pos* PPM
    position = (position[0], height - position[1])
    pg.draw.circle(screen, colors[body.type], [int(x) for x in position], int(circle.radius * PPM) )

circleShape.draw = my_draw_circle





def fon():
    fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    screen.blit(fon, (0, 0))


def start_balls():
    global run
    fon()
    while run:
        fon()

        time_delta = clock.tick(SPEED) / 1000.0

        for body in world.bodies:
            for fixture in body.fixtures:
                fixture.shape.draw(body, fixture)

        world.Step(TIME_STEP, 10, 10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    create_circle()
                elif event.button == 3:
                    create_polygons()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    pass
                if event.key == pg.K_UP:
                    pass

        pg.display.flip()  # Обновление кадра

start_balls()

