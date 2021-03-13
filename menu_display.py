import pygame as pg
import animation_menu as am


class MenuDisplay:

    def __init__(self, screen, screen_width, screen_height):

        self.screen = screen
        self.width = screen_width
        self.height = screen_height

        self.background = pg.image.load("ressources/Maps/world_map.jpg")
        self.background = pg.transform.scale(self.background, (screen_width, screen_height))

        self.main_font = pg.font.Font("ressources/Fonts/bignoodletoo.woff", 160)

        self.main_title = self.main_font.render("WarGame", True, (243, 192, 38))
        self.main_title_rect = self.main_title.get_rect()
        self.main_title_rect.left = 38
        self.main_title_rect.centery = self.height // 6 + 50

        self.main_font_highlight = pg.font.Font("ressources/Fonts/bignoodletoo.woff", 175)
        self.main_title_highlight = self.main_font_highlight.render("WarGame", True, (243, 192, 38))
        self.main_title_highlight_rect = self.main_title_highlight.get_rect()
        self.main_title_highlight_rect.left = 38
        self.main_title_highlight_rect.centery = self.height // 6 + 50

        self.buttons_font = pg.font.Font("ressources/Fonts/f014015d.woff", 90)
        self.buttons = [self.buttons_font.render("Play", True, (255, 255, 255)),
                        self.buttons_font.render("Load Game", True, (255, 255, 255)),
                        self.buttons_font.render("Settings", True, (255, 255, 255)),
                        self.buttons_font.render("Leave", True, (255, 255, 255))]
        self.buttons_rect = [i.get_rect() for i in self.buttons]

        self.buttons_font_highlighted = pg.font.Font("ressources/Fonts/f014015d.woff", 110)
        self.buttons_highlighted = [self.buttons_font_highlighted.render("Play", True, (255, 255, 255)),
                                    self.buttons_font_highlighted.render("Load Game", True, (255, 255, 255)),
                                    self.buttons_font_highlighted.render("Settings", True, (255, 255, 255)),
                                    self.buttons_font_highlighted.render("Leave", True, (255, 255, 255))]
        self.buttons_highlighted_rect = [i.get_rect() for i in self.buttons_highlighted]

        for i in range(4):
            self.buttons_rect[i].left = 30
            self.buttons_rect[i].centery = self.height // 3 + (self.height // 9 * i) + 50

        for i in range(4):
            self.buttons_highlighted_rect[i].left = 30
            self.buttons_highlighted_rect[i].centery = self.height // 3 + (self.height // 9 * i) + 50

        self.anim = [am.Anim(self.screen, self.width, self.height, i) for i in range(4)]

    def main_display(self):

        mouse_coo = pg.mouse.get_pos()

        self.screen.blit(self.background, (0, 0))

        if not self.main_title_highlight_rect.collidepoint(mouse_coo):
            self.screen.blit(self.main_title, self.main_title_rect)
        else:
            self.screen.blit(self.main_title_highlight, self.main_title_highlight_rect)

        for i in range(4):
            if not self.buttons_highlighted_rect[i].collidepoint(mouse_coo):
                self.screen.blit(self.buttons[i], self.buttons_rect[i])
            else:
                self.anim[i].animate_here()
                self.screen.blit(self.buttons_highlighted[i], self.buttons_highlighted_rect[i])
