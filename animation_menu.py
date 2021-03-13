import pygame as pg
from random import randint


class Anim:

    def __init__(self, screen, width, height, selection):
        self.screen = screen
        self.width = width
        self.height = height

        self.selection = selection

        if selection == 0:
            self.main_surf = pg.Surface((250, 35))
            self.square_group = pg.sprite.Group()
            for i in range(6):
                self.square_group.add(
                    WhiteSquare((i * 40 + 10,
                                 randint(0, 35) + (self.height // 3 + (self.height // 9 * selection + 50))),
                                self.main_surf, selection, self.height))
        elif selection == 1:
            self.main_surf = pg.Surface((590, 35))
            self.square_group = pg.sprite.Group()
            for i in range(15):
                self.square_group.add(
                    WhiteSquare((i * 40 + 10,
                                 randint(0, 35) + (self.height // 3 + (self.height // 9 * selection + 50))),
                                self.main_surf, selection, self.height))
        elif selection == 2:
            self.main_surf = pg.Surface((410, 35))
            self.square_group = pg.sprite.Group()
            for i in range(10):
                self.square_group.add(
                    WhiteSquare((i * 40 + 10,
                                 randint(0, 35) + (self.height // 3 + (self.height // 9 * selection + 50))),
                                self.main_surf, selection, self.height))
        elif selection == 3:
            self.main_surf = pg.Surface((330, 35))
            self.square_group = pg.sprite.Group()
            for i in range(9):
                self.square_group.add(
                    WhiteSquare((i * 40 + 10,
                                 randint(0, 35) + (self.height // 3 + (self.height // 9 * selection) + 50)),
                                self.main_surf, selection, self.height))

        self.main_surf.fill((255, 255, 255))
        self.main_surf.set_alpha(100)
        self.main_rect = self.main_surf.get_rect()
        self.main_rect.left = 0
        self.main_rect.centery = self.height // 3 + (self.height // 9 * selection) + 70

        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

    def animate_here(self):

        self.current_time = pg.time.get_ticks()

        self.screen.blit(self.main_surf, self.main_rect)
        self.square_group.draw(self.screen)
        if self.current_time - self.delay > 25:
            self.delay = self.current_time
            self.square_group.update()


class WhiteSquare(pg.sprite.Sprite):

    def __init__(self, coordinates, surf_inside, selection, height):
        super().__init__()

        self.surf_inside = surf_inside

        self.image = pg.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.image.set_alpha(200)
        self.rect = self.image.get_rect()

        self.rect.center = coordinates

        self.selection = selection
        self.height = height

    def update(self):
        if self.rect.x > self.surf_inside.get_width() + 5:
            self.rect.center = (10, randint(0, 30) + (self.height // 3 + (self.height // 9 * self.selection) + 50))

        self.rect.x += 3
