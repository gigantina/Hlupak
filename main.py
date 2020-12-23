import pygame as pg
import pygame_gui

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

class ScoreDisplay(pg.sprite.Sprite):
    #TODO Сделать так, чтобы значение внутри него менялось
    """Этот класс будет изображать счетчик очков"""
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Счет", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=20)
        self.image.blit(self.text, (width // 5, height // 7))
        self.text_score = "0"
        self.score =  self.font.render(self.text_score, 1, (0, 0, 0))
        self.image.blit(self.score, (width //5, height //2))

        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print("Есть контакт")

class Menu(pg.sprite.Sprite):
    #TODO сделать главное меню
    """Этот класс - кнопка главного меню, чуть позже ее реализую"""
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Меню", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=10)
        self.image.blit(self.text, (width // 4, height // 4))


        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print("Есть контакт")

class Leaders(pg.sprite.Sprite):
    #TODO сделать базу данных с таблицей лидеров всех
    """Этот класс переводит нас на список всех лидеров"""
    def __init__(self, all_sprites, x, y, width, height):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pg.Surface((width, height), pg.SRCALPHA, 32)

        self.font = pg.font.Font(None, 25)
        self.text = self.font.render("Лидеры", 1, (0, 0, 0))
        pg.draw.rect(self.image, (255, 125, 0), (0, 0, width, height), border_radius=10)
        self.image.blit(self.text, (width // 7, height // 4))


        self.rect = pg.Rect(x, y, width, height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print("Есть контакт")

def draw_logo():
    text_logo = "2048"
    font = pg.font.Font(None, 60)
    text = font.render(text_logo, 1, (0, 200, 0))
    screen.blit(text, (10, 10))

all_sprites = pg.sprite.Group()

def draw_all_ui():
    draw_logo()
    ScoreDisplay(all_sprites, 123, 10, 100, 70)
    Menu(all_sprites, 230, 10, 100, 30)
    Leaders(all_sprites, 230, 50, 100, 30)



while run:
    screen.fill(pg.Color(color))
    time_delta = clock.tick(60) / 1000.0
    draw_all_ui()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos)

        if event.type == pg.MOUSEBUTTONUP:
            coords = event.pos
    all_sprites.draw(screen)
    all_sprites.update(event)

    pg.display.flip()  # Обновление кадра
pg.quit()
