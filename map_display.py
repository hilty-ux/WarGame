import pygame as pg


class MainMap:

    def __init__(self, screen, width, height):

        self.screen, self.width, self.height = screen, width, height

        self.basic_map = pg.image.load("ressources/MainMap/Map.png")
        self.basic_map = pg.transform.scale(self.basic_map, (width, height))

        self.all_neons = [USA(width, height),
                          Canada(width, height),
                          Peru(width, height),
                          Brazil(width, height),
                          Argentina(width, height),
                          Alaska(width, height),
                          Mexico(width, height),
                          Groenland(width, height),
                          Iceland(width, height),
                          GreatBritain(width, height),
                          France(width, height),
                          Germany(width, height),
                          Spain(width, height),
                          Yugoslavia(width, height),
                          Italy(width, height),
                          MiddleEast(width, height),
                          Polska(width, height),
                          Switzerland(width, height),
                          Scandinavia(width, height),
                          Russia(width, height),
                          China(width, height),
                          India(width, height),
                          Kotmenistan(width, height),
                          Japan(width, height),
                          Australia(width, height),
                          WesternAfrica(width, height),
                          EasternAfrica(width, height),
                          CentralAfrica(width, height),
                          SouthernAfrica(width, height),
                          Indonesia(width, height),
                          Thai(width, height),
                          Madagascar(width, height)]

        self.pos = pg.mouse.get_pos()
        self.all_pos = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.all_neons]
        self.touching = [
            self.all_neons[i].rect.collidepoint(*self.pos) and self.all_neons[i].mask.get_at(self.all_pos[i]) for i in
            range(len(self.all_neons))]

        self.neon = USA(width, height)
        self.pos = pg.mouse.get_pos()
        self.pos_in_mask = self.pos[0] - self.neon.rect.x, self.pos[1] - self.neon.rect.y

        self.neon_top_left = [Alaska(width, height), USA(width, height), Canada(width, height), Mexico(width, height),
                              Groenland(width, height), Iceland(width, height), France(width, height),
                              GreatBritain(width, height),
                              Spain(width, height), Italy(width, height), WesternAfrica(width, height),
                              Switzerland(width, height), Germany(width, height), Scandinavia(width, height)]
        self.neon_top_right = [Scandinavia(width, height), Russia(width, height), CentralAfrica(width, height),
                               MiddleEast(width, height), Polska(width, height), Yugoslavia(width, height),
                               Kotmenistan(width, height), China(width, height), India(width, height),
                               Thai(width, height), Japan(width, height)]
        self.neon_bot_left = [Mexico(width, height), Peru(width, height), Brazil(width, height),
                              Argentina(width, height), WesternAfrica(width, height), CentralAfrica(width, height),
                              SouthernAfrica(width, height)]
        self.neon_bot_right = [MiddleEast(width, height), CentralAfrica(width, height), EasternAfrica(width, height),
                               WesternAfrica(width, height), SouthernAfrica(width, height),
                               Madagascar(width, height), India(width, height), Thai(width, height),
                               Australia(width, height), Indonesia(width, height)]
        self.all_pos_top_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_right]
        self.touching_top_right = [
            self.neon_top_right[i].rect.collidepoint(*self.pos) and self.neon_top_right[i].mask.get_at(
                self.all_pos_top_right[i]) for i in range(len(self.neon_top_right))]

        self.all_pos_top_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_left]
        self.touching_top_left = [
            self.neon_top_left[i].rect.collidepoint(*self.pos) and self.neon_top_left[i].mask.get_at(
                self.all_pos_top_left[i]) for i in range(len(self.neon_top_left))]

        self.all_pos_bot_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_left]
        self.touching_bot_left = [
            self.neon_bot_left[i].rect.collidepoint(*self.pos) and self.neon_bot_left[i].mask.get_at(
                self.all_pos_bot_left[i]) for i in range(len(self.neon_bot_left))]

        self.all_pos_bot_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_right]
        self.touching_bot_right = [
            self.neon_bot_right[i].rect.collidepoint(*self.pos) and self.neon_bot_right[i].mask.get_at(
                self.all_pos_bot_right[i]) for i in range(len(self.neon_bot_right))]

        self.condition_france = self.touching_top_right[6]
        self.condition_alaska = self.touching_top_right[0]
        self.condition_canada = self.touching_top_right[2]

    def update(self):

        self.pos = pg.mouse.get_pos()

        self.screen.blit(self.basic_map, (0, 0))

        if self.pos[0] <= self.width // 2:
            if self.pos[1] <= self.height // 2:
                self.all_pos_top_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_left]
                self.touching_top_left = [
                    self.neon_top_left[i].rect.collidepoint(*self.pos) and self.neon_top_left[i].mask.get_at(
                        self.all_pos_top_left[i]) for i in range(len(self.neon_top_left))]
                for i in range(len(self.neon_top_left)):
                    if self.touching_top_left[i]:
                        self.screen.blit(self.neon_top_left[i].image, self.neon_top_left[i].rect)
            elif self.pos[1] >= self.height // 2:
                self.all_pos_bot_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_left]
                self.touching_bot_left = [
                    self.neon_bot_left[i].rect.collidepoint(*self.pos) and self.neon_bot_left[i].mask.get_at(
                        self.all_pos_bot_left[i]) for i in range(len(self.neon_bot_left))]
                for i in range(len(self.neon_bot_left)):
                    if self.touching_bot_left[i]:
                        self.screen.blit(self.neon_bot_left[i].image, self.neon_bot_left[i].rect)
        elif self.pos[0] >= self.width // 2:
            if self.pos[1] <= self.height // 2:
                self.all_pos_top_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_right]
                self.touching_top_right = [
                    self.neon_top_right[i].rect.collidepoint(*self.pos) and self.neon_top_right[i].mask.get_at(
                        self.all_pos_top_right[i]) for i in range(len(self.neon_top_right))]
                for i in range(len(self.neon_top_right)):
                    if self.touching_top_right[i]:
                        self.screen.blit(self.neon_top_right[i].image, self.neon_top_right[i].rect)
            elif self.pos[1] >= self.height // 2:
                self.all_pos_bot_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_right]
                self.touching_bot_right = [
                    self.neon_bot_right[i].rect.collidepoint(*self.pos) and self.neon_bot_right[i].mask.get_at(
                        self.all_pos_bot_right[i]) for i in range(len(self.neon_bot_right))]

                for i in range(len(self.neon_bot_right)):
                    if self.touching_bot_right[i]:
                        self.screen.blit(self.neon_bot_right[i].image, self.neon_bot_right[i].rect)

    def click(self):
        pos = pg.mouse.get_pos()

        self.all_pos_top_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_right]
        self.touching_top_right = [
            self.neon_top_right[i].rect.collidepoint(*self.pos) and self.neon_top_right[i].mask.get_at(
                self.all_pos_top_right[i]) for i in range(len(self.neon_top_right))]

        self.all_pos_top_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_top_left]
        self.touching_top_left = [
            self.neon_top_left[i].rect.collidepoint(*self.pos) and self.neon_top_left[i].mask.get_at(
                self.all_pos_top_left[i]) for i in range(len(self.neon_top_left))]

        self.all_pos_bot_left = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_left]
        self.touching_bot_left = [
            self.neon_bot_left[i].rect.collidepoint(*self.pos) and self.neon_bot_left[i].mask.get_at(
                self.all_pos_bot_left[i]) for i in range(len(self.neon_bot_left))]

        self.all_pos_bot_right = [(self.pos[0] - i.rect.x, self.pos[1] - i.rect.y) for i in self.neon_bot_right]
        self.touching_bot_right = [
            self.neon_bot_right[i].rect.collidepoint(*self.pos) and self.neon_bot_right[i].mask.get_at(
                self.all_pos_bot_right[i]) for i in range(len(self.neon_bot_right))]

        self.condition_france = self.touching_top_left[6]
        self.condition_alaska = self.touching_top_left[0]
        self.condition_canada = self.touching_top_left[2]
        print(self.condition_france)


class USA:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)

        self.image = pg.image.load("ressources/Neon/USA.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)

class Canada:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Canadian Empire.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Alaska:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Alaskan Republic.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Mexico:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Mexican federation.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Peru:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Peruvian Empire.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Brazil:
    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Braziliana.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Argentina:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/ACU Argentino-chilian union.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Groenland:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Groënland.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Iceland:
    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Iceland.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class France:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/France.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class GreatBritain:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Great Britain.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Spain:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Spanish union.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Italy:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Italy.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Germany:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/German republic.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Yugoslavia:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Polska.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class MiddleEast:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Middle east.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Polska:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Yougoslav.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Switzerland:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Switzerland (suisse).png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Scandinavia:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Scandinavian union.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Russia:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Russian federation.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class China:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/China.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Japan:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Japan.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class India:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Indian republic.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Kotmenistan:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Kotmenistan.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Thai:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Thaï-union.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Indonesia:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Indonesia.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Australia:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Australia.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class WesternAfrica:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Western africa.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class CentralAfrica:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Central Africa.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class EasternAfrica:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Eastern Africa.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class SouthernAfrica:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Southern Africa.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)


class Madagascar:

    def __init__(self, width, height):
        ratiow = 1920 // int(width)
        ratioh = 1080 // int(height)
        self.image = pg.image.load("ressources/Neon/Democracy of Madagascar.png")
        self.image = pg.transform.scale(self.image, (1920 // ratiow, 1080 // ratioh))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
