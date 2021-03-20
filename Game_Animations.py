import pygame as pg


class SimpleExplosion(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/Frame Explosion/tile000.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile001.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile002.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile003.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile004.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile005.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile006.png"),
                       pg.image.load("ressources/Assets/Frame Explosion/tile007.png")]
        self.images = [pg.transform.scale(i, (150, 150)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 75:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Explosion1(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion1/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0020.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0021.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0022.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0023.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0024.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0025.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0026.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0027.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0028.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0029.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0030.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0031.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0032.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0033.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0034.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0035.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion1/0036.png")]

        self.images = [pg.transform.scale(i, (50, 50)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 50:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Explosion2(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion2/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion2/0020.png")]

        self.images = [pg.transform.scale(i, (75, 75)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 75:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Explosion3(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion3/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0020.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0021.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0022.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0023.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0024.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0025.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0026.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0027.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0028.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0029.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion3/0030.png")]

        self.images = [pg.transform.scale(i, (75, 75)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 50:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Explosion4(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion4/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0020.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0021.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0022.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0023.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0024.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion4/0025.png")]

        self.images = [pg.transform.scale(i, (75, 75)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 50:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Explosion5(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0020.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0021.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion5[64x64]/0022.png")]

        self.images = [pg.transform.scale(i, (75, 75)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 50:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


class Nuke(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.images = [pg.image.load("ressources/Assets/New Explosions/Explosion6/0001.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0002.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0003.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0004.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0005.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0006.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0007.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0008.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0009.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0010.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0011.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0012.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0013.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0014.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0015.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0016.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0018.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0019.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0020.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0021.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0022.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0023.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0024.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0025.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0026.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0027.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0028.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0029.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0030.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0031.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0032.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0033.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0034.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0035.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0036.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0037.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0038.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0039.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0040.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0041.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0042.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0043.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0044.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0045.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0046.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0047.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0048.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0049.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0050.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0051.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0052.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0053.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0054.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0055.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0056.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0057.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0058.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0059.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0060.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0061.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0062.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0063.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0064.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0065.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0066.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0067.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0068.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0069.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0070.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0071.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0072.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0073.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0074.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0075.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0076.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0077.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0078.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0079.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0080.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0081.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0082.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0083.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0084.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0085.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0086.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0087.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0088.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0089.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0090.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0091.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0092.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0093.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0094.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0095.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0096.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0097.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0098.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0099.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0100.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0101.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0102.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0103.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0104.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0105.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0106.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0107.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0108.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0109.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0110.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0111.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0112.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0113.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0114.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0115.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0116.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0118.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0119.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0120.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0121.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0122.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0123.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0124.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0125.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0126.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0127.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0128.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0129.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0130.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0131.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0132.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0133.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0134.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0135.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0136.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0137.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0138.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0139.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0140.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0141.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0142.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0143.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0144.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0145.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0146.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0147.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0148.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0149.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0150.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0151.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0152.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0153.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0154.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0155.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0156.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0157.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0158.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0159.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0160.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0161.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0162.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0163.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0164.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0165.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0166.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0167.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0168.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0169.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0170.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0171.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0172.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0173.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0174.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0175.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0176.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0177.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0178.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0179.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0180.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0181.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0182.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0183.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0184.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0185.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0186.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0187.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0188.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0189.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0190.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0191.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0192.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0193.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0194.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0195.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0196.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0197.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0198.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0199.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0200.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0201.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0202.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0203.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0204.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0205.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0206.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0207.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0208.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0209.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0210.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0211.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0212.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0213.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0214.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0215.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0216.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0217.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0218.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0219.png"),
                       pg.image.load("ressources/Assets/New Explosions/Explosion6/0220.png")
                       ]

        self.images = [pg.transform.scale(i, (600, 600)) for i in self.images]
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.index_anim = 0
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.rect.center = coordinates

    def update(self):
        self.current_time = pg.time.get_ticks()

        if self.current_time - self.delay > 40:
            self.delay = self.current_time
            if self.index_anim < len(self.images)-1:
                self.index_anim += 1
            else:
                self.index_anim = 0
                self.kill()

        self.image = self.images[self.index_anim]


