import pygame as pg


class MainMap:

    def __init__(self, screen, screen_width, screen_height):

        self.screen, self.width, self.height = screen, screen_width, screen_height

        self.basic_map = pg.image.load("ressources/MainMap/Map.png")
        self.basic_map = pg.transform.scale(self.basic_map, (screen_width, screen_height))

        self.all_neons = [USA(),
                          Canada(),
                          Peru(),
                          Brazil(),
                          Argentina(),
                          Alaska(),
                          Mexico(),
                          Groenland(),
                          Iceland(),
                          GreatBritain(),
                          France(),
                          Germany(),
                          Spain(),
                          Yugoslavia(),
                          Italy(),
                          MiddleEast(),
                          Polska(),
                          Switzerland(),
                          Scandinavia(),
                          Russia(),
                          China(),
                          India(),
                          Kotmenistan(),
                          Japan(),
                          Australia(),
                          WesternAfrica(),
                          EasternAfrica(),
                          CentralAfrica(),
                          SouthernAfrica(),
                          Indonesia(),
                          Thai(),
                          Madagascar()]

        self.pos = pg.mouse.get_pos()
        self.all_pos = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.all_neons]
        self.touching = [self.all_neons[i].rect.collidepoint(*self.pos) and self.all_neons[i].mask.get_at(self.all_pos[i]) for i in range(len(self.all_neons))]

        self.neon = USA()
        self.pos = pg.mouse.get_pos()
        self.pos_in_mask = self.pos[0] - self.neon.rect.x, self.pos[1] - self.neon.rect.y

    def update(self):

        self.pos = pg.mouse.get_pos()
        self.all_pos = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.all_neons]
        self.touching = [self.all_neons[i].rect.collidepoint(*self.pos) and self.all_neons[i].mask.get_at(self.all_pos[i]) for i in range(len(self.all_neons))]

        self.screen.blit(self.basic_map, (0, 0))

        for i in range(len(self.all_neons)):
            if self.touching[i]:
                self.screen.blit(self.all_neons[i].image, self.all_neons[i].rect)


class USA:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/USA.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Canada:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Canadian Empire.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Alaska:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Alaskan Republic.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Mexico:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Mexican federation.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Peru:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Peruvian Empire.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Brazil:
    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Braziliana.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Argentina:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/ACU Argentino-chilian union.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Groenland:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Groënland.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Iceland:
    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Iceland.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class France:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/France.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class GreatBritain:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Great Britain.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Spain:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Spanish union.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Italy:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Italy.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Germany:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/German republic.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Yugoslavia:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Polska.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class MiddleEast:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Middle east.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Polska:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Yougoslav.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Switzerland:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Switzerland (suisse).png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Scandinavia:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Scandinavian union.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Russia:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Russian federation.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class China:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/China.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Japan:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Japan.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class India:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Indian republic.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Kotmenistan:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Kotmenistan.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Thai:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Thaï-union.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Indonesia:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Indonesia.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Australia:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Australia.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class WesternAfrica:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Western africa.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class CentralAfrica:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Central Africa.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class EasternAfrica:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Eastern Africa.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class SouthernAfrica:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Southern Africa.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
class Madagascar:

    def __init__(self):
        self.image = pg.image.load("ressources/Neon/Democracy of Madagascar.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


