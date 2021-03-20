import pygame as pg


class Moon:

    def __init__(self, screen, width, height):

        self.screen, self.width, self.height = screen, width, height

        self.ground_group = pg.sprite.Group()
        self.add_mountains = lambda x, y: self.ground_group.add(Mountains((x, y)))
        self.add_ground = lambda x, y: self.ground_group.add(Ground((x, y)))
        self.add_crater1 = lambda x, y: self.ground_group.add(Crater1((x, y)))
        self.add_crater2 = lambda x, y: self.ground_group.add(Crater2((x, y)))

        self.ground_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            ]

        self.read()

    def __call__(self):
        self.ground_group.draw(self.screen)

    def read(self):
        for row in range(len(self.ground_list)):
            for col in range(len(self.ground_list[row])):
                if self.ground_list[row][col] == 1:
                    self.add_ground(col*128, row*32)
                elif self.ground_list[row][col] == 2:
                    self.add_mountains(col*128, row*32)
                elif self.ground_list[row][col] == 3:
                    self.add_crater1(col*128, row*32)
                elif self.ground_list[row][col] == 4:
                    self.add_crater2(col*128, row*32)


class Mountains(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()
        self.image = pg.image.load("ressources/Background/Surface_Layer1.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coordinates


class Crater1(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()
        self.image = pg.image.load("ressources/Background/Surface_Layer2.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coordinates


class Crater2(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()
        self.image = pg.image.load("ressources/Background/Surface_Layer3.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coordinates


class Ground(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()
        self.image = pg.image.load("ressources/Background/Surface_Layer4.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coordinates
