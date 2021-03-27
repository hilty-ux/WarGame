import pygame as pg


class FakeInfantry(pg.sprite.Sprite):
    """Just a class to show the infantry on the screen while the player is placing units on the battlefield"""

    def __init__(self, coordinates, width, height):

        super().__init__()

        self.image = pg.Surface((width * (75 / width), height * (75 / height)))
        self.rect = self.image.get_rect(center=coordinates)
        self.image.fill((0, 255, 0))

        self.name = "infantry"
        self.clicked = False

    def click(self):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.clicked = True
        else:
            self.clicked = False

    def right_click(self):
        pos = pg.mouse.get_pos()

        if self.clicked:
            self.rect.center = pos

    def update(self, click, right_click, return_pos):

        if click:
            self.click()
            return self.clicked

        if right_click:
            self.right_click()
            return

        if return_pos:
            return self.rect.center

        if self.clicked:
            self.image.fill((0, 50, 255))
        else:
            self.image.fill((0, 255, 0))


class FakeSniper(pg.sprite.Sprite):
    """Just a class to show the infantry on the screen while the player is placing units on the battlefield"""

    def __init__(self, coordinates, width, height):

        super().__init__()

        self.image = pg.Surface((width * (25 / width), height * (25 / height)))
        self.rect = self.image.get_rect(center=coordinates)
        self.image.fill((0, 255, 0))

        self.name = "sniper"
        self.clicked = False

    def click(self):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.clicked = True
        else:
            self.clicked = False

    def right_click(self):
        pos = pg.mouse.get_pos()

        if self.clicked:
            self.rect.center = pos

    def update(self, click, right_click, return_pos):

        if click:
            self.click()
            return self.clicked

        if right_click:
            self.right_click()
            return

        if return_pos:
            return self.rect.center

        if self.clicked:
            self.image.fill((0, 50, 255))
        else:
            self.image.fill((0, 255, 0))


class FakeArtillery(pg.sprite.Sprite):
    """Just a class to show the infantry on the screen while the player is placing units on the battlefield"""

    def __init__(self, coordinates, width, height):

        super().__init__()

        self.image = pg.Surface((width * (50 / width), height * (25 / height)))
        self.rect = self.image.get_rect(center=coordinates)
        self.image.fill((0, 255, 0))

        self.name = "artillery"
        self.clicked = False

    def click(self):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.clicked = True
        else:
            self.clicked = False

    def right_click(self):
        pos = pg.mouse.get_pos()

        if self.clicked:
            self.rect.center = pos

    def update(self, click, right_click, return_pos):

        if click:
            self.click()
            return self.clicked

        if right_click:
            self.right_click()
            return

        if return_pos:
            return self.rect.center

        if self.clicked:
            self.image.fill((0, 50, 255))
        else:
            self.image.fill((0, 255, 0))


class FakeCavalry(pg.sprite.Sprite):
    """Just a class to show the infantry on the screen while the player is placing units on the battlefield"""

    def __init__(self, coordinates, width, height):

        super().__init__()

        self.image = pg.Surface((width * (50 / width), height * (50 / height)))
        self.rect = self.image.get_rect(center=coordinates)
        self.image.fill((0, 255, 0))

        self.name = "cavalry"
        self.clicked = False

    def click(self):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.clicked = True
        else:
            self.clicked = False

    def right_click(self):
        pos = pg.mouse.get_pos()

        if self.clicked:
            self.rect.center = pos

    def update(self, click, right_click, return_pos):

        if click:
            self.click()
            return self.clicked

        if right_click:
            self.right_click()
            return

        if return_pos:
            return self.rect.center

        if self.clicked:
            self.image.fill((0, 50, 255))
        else:
            self.image.fill((0, 255, 0))