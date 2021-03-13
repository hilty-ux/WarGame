import pygame as pg


class PopUpGold:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((250, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Gold Usage", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [
            self.main_explanation_font.render("Gold is needed to buy special troops", True, (255, 255, 255)),
            self.main_explanation_font.render("You can also use gold to trade with", True, (255, 255, 255)),
            self.main_explanation_font.render("other players or buy boosts for your", True, (255, 255, 255)),
            self.main_explanation_font.render("country.", True, (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (240, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)


class PopUpIron:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((250, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Iron Usage", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [self.main_explanation_font.render("Iron is needed to train troops", True, (255, 255, 255)),
                            self.main_explanation_font.render("Iron is also needed to build", True, (255, 255, 255)),
                            self.main_explanation_font.render("infrastructures like barracks,", True, (255, 255, 255)),
                            self.main_explanation_font.render("walls or houses.", True, (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (240, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)


class PopUpFood:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((250, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Food Usage", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [self.main_explanation_font.render("Food is needed to train troops", True, (255, 255, 255)),
                            self.main_explanation_font.render("Food is also needed to feed all your", True,
                                                              (255, 255, 255)),
                            self.main_explanation_font.render("cities and inhabitants.", True, (255, 255, 255)),
                            self.main_explanation_font.render("You'll have a turnly deficit of food.", True,
                                                              (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (240, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)


class PopUpWF:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((300, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Work Force Usage", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [
            self.main_explanation_font.render("Work force value tell about your build capacity", True, (255, 255, 255)),
            self.main_explanation_font.render("More you have work force, faster your", True, (255, 255, 255)),
            self.main_explanation_font.render("infrastructures will be build.", True, (255, 255, 255)),
            self.main_explanation_font.render("Work force growth depends on your lands.", True, (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (290, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)


class PopUpWood:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((280, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Wood Usage", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [
            self.main_explanation_font.render("Wood is needed to build defenses", True, (255, 255, 255)),
            self.main_explanation_font.render("You'll need wood to build walls,", True, (255, 255, 255)),
            self.main_explanation_font.render("defensive infrastructures, mines...", True, (255, 255, 255)),
            self.main_explanation_font.render("Gain wood with wood forests exploiting.", True, (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (270, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)


class PopUpLand:

    def __init__(self, screen):

        self.screen = screen

        self.main_surf = pg.Surface((300, 150))
        self.main_surf.fill((100, 100, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.title = self.font_title.render("Land Count", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left = 10
        self.title_rect.top = 10

        self.main_explanation_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.explanation = [
            self.main_explanation_font.render("This number tells how many land(s) you own", True, (255, 255, 255)),
            self.main_explanation_font.render("To gain lands, attack other players,", True, (255, 255, 255)),
            self.main_explanation_font.render("colonize unknown lands or annex weaker", True, (255, 255, 255)),
            self.main_explanation_font.render("players.", True, (255, 255, 255))]

        self.explanation_rect = [i.get_rect() for i in self.explanation]
        self.explanation_rect[0].left, self.explanation_rect[0].top = 10, 50

        for i in range(1, 4):
            self.explanation_rect[i].left = 10
            self.explanation_rect[i].top = 60 + i * 17

        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (10, 40), (290, 40))
        for i in range(4):
            self.main_surf.blit(self.explanation[i], self.explanation_rect[i])

    def update_(self, coordinates):
        self.screen.blit(self.main_surf, coordinates)

