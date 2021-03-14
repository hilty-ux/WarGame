import pygame as pg


class France:

    def __init__(self, screen, screen_width, screen_height):
        self.screen, self.width, self.height = screen, screen_width, screen_height
        self.owner = "Player"

        self.main_surf = pg.Surface((screen_width // 2 - 100, screen_height - 200))
        self.main_surf.fill((110, 110, 255))

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 75)
        self.title = self.font_title.render("France", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.left, self.title_rect.top = 25, 25
        self.main_surf.blit(self.title, self.title_rect)
        pg.draw.line(self.main_surf, (255, 255, 255), (25, 125), (self.main_surf.get_width() - 25, 125))

        self.exit_font = pg.font.Font("ressources/Fonts/f014015d.woff", 50)
        self.exit = self.exit_font.render("Exit", True, (0, 0, 0))
        self.exit_rect = self.exit.get_rect()
        self.exit_rect.left, self.exit_rect.top = 25, 75

        self.upgrade_font = pg.font.Font("ressources/Fonts/f014015d.woff", 30)

        self.upgrade_tabs = [self.upgrade_font.render("Infrastructures", True, (255, 255, 255)),
                             self.upgrade_font.render("Produce Troops", True, (255, 255, 255)),
                             self.upgrade_font.render("Yield stats", True, (255, 255, 255)),
                             self.upgrade_font.render("Defense statue", True, (255, 255, 255))]
        self.upgrade_tabs_rect = [i.get_rect() for i in self.upgrade_tabs]
        self.upgrade_tabs_rect[0].left = self.width // 2 + 100
        self.upgrade_tabs_rect[1].left = self.width // 2 + 100 + self.upgrade_tabs[0].get_width() + 25
        self.upgrade_tabs_rect[2].left = self.width // 2 + 100 + self.upgrade_tabs[0].get_width() + 25 + \
                                         self.upgrade_tabs[1].get_width() + 25
        self.upgrade_tabs_rect[3].left = self.width // 2 + 100 + self.upgrade_tabs[0].get_width() + 25 + \
                                         self.upgrade_tabs[1].get_width() + 25 + self.upgrade_tabs[2].get_width() + 25
        for i in range(4):
            self.upgrade_tabs_rect[i].centery = 260

        self.current_tab = 0

        self.level_workers_housing = 1
        self.level_mines = 0
        self.level_fields = 0
        self.level_sawmill = 1

        # tab infrastructures :

        self.surf_workers_housings = pg.Surface((screen_width // 2 - 200, (self.height - 460) // 4))
        self.surf_workers_housings.fill((0, 0, 0))
        self.surf_workers_housings.set_alpha(128)
        self.surf_workers_housings_rect = self.surf_workers_housings.get_rect()
        self.surf_workers_housings_rect.left, self.surf_workers_housings_rect.centery = self.width // 2 + 100, 380

        self.surf_mine = pg.Surface((screen_width // 2 - 200, (self.height - 460) // 4))
        self.surf_mine.fill((0, 0, 0))
        self.surf_mine.set_alpha(128)
        self.surf_mine_rect = self.surf_mine.get_rect()
        self.surf_mine_rect.left, self.surf_mine_rect.centery = self.width // 2 + 100, 380 + (self.height - 460) // 4 + 10

        self.surf_fields = pg.Surface((screen_width // 2 - 200, (self.height - 460) // 4))
        self.surf_fields.fill((0, 0, 0))
        self.surf_fields.set_alpha(128)
        self.surf_fields_rect = self.surf_fields.get_rect()
        self.surf_fields_rect.left, self.surf_fields_rect.centery = self.width // 2 + 100, 380 + ((self.height - 460) // 4 + 10) * 2

        self.surf_sawmill = pg.Surface((screen_width // 2 - 200, (self.height - 460) // 4))
        self.surf_sawmill.fill((0, 0, 0))
        self.surf_sawmill.set_alpha(128)
        self.surf_sawmill_rect = self.surf_sawmill.get_rect()
        self.surf_sawmill_rect.left, self.surf_sawmill_rect.centery = self.width // 2 + 100, 380 + ((self.height - 460) // 4 + 10) * 3

        self.font_title_infra = pg.font.Font("ressources/Fonts/f014015d.woff", 40)
        self.titles_infra = [self.font_title_infra.render("Worker housings", True, (255, 255, 255)),
                             self.font_title_infra.render("Mines", True, (255, 255, 255)),
                             self.font_title_infra.render("Fields", True, (255, 255, 255)),
                             self.font_title_infra.render("Sawmills", True, (255, 255, 255))]
        self.titles_infra_rect = [i.get_rect() for i in self.titles_infra]
        for i in range(4):
            self.titles_infra_rect[i].left = self.width // 2 + 110
            self.titles_infra_rect[i].centery = 325 + ((self.height - 460) // 4 + 10) * i

        self.font_prods = pg.font.Font("ressources/Fonts/f014015d.woff", 20)
        self.prods = [self.font_prods.render("+ 0 work force/turn", True, (255, 255, 255)),
                      self.font_prods.render("+ 0 iron/turn, + 0 gold/turn", True, (255, 255, 255)),
                      self.font_prods.render("+ 0 food/turn", True, (255, 255, 255)),
                      self.font_prods.render("+ 0 wood/turn", True, (255, 255, 255))]
        self.prods_rect = [i.get_rect() for i in self.prods]
        for i in range(4):
            self.prods_rect[i].right, self.prods_rect[i].centery = self.width - 110, 325 + ((self.height - 460) // 4 + 10) * i

        self.font_buttons = pg.font.Font("ressources/Fonts/f014015d.woff", 50)
        self.buttons_upgrade = [self.font_buttons.render(f"Buy upgrade: {50*(self.level_workers_housing+1)} wood", True, (255, 255, 255)),
                                self.font_buttons.render(f"Buy upgrade: {50*(self.level_mines+1)} wood, {10*(self.level_mines+1)} gold", True, (255, 255, 255)),
                                self.font_buttons.render(f"Buy upgrade: {25*(self.level_fields+1)} wood, {5*(self.level_mines+1)} gold", True, (255, 255, 255)),
                                self.font_buttons.render(f"Buy upgrade: {100*(self.level_sawmill+1)} food", True, (255, 255, 255))]
        self.buttons_upgrade_rect = [i.get_rect() for i in self.buttons_upgrade]
        for i in range(4):
            self.buttons_upgrade_rect[i].right, self.buttons_upgrade_rect[i].centery = self.width - 110, 340 + ((self.height - 460) // 4 + 10) * i

        self.upgrading_font = pg.font.Font("ressources/Fonts/f014015d.woff", 25)
        self.upgrading = [self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255)),
                          self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255)),
                          self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255)),
                          self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255))]
        self.upgrading_rect = [i.get_rect() for i in self.upgrading]
        for i in range(4):
            self.upgrading_rect[i].left, self.upgrading_rect[i].centery = self.width // 2 + 110, 370 + ((self.height - 460) // 4 + 10) * i

    def update_prods(self):
        self.prods = [self.font_prods.render(f"+ {10*self.level_workers_housing} work force/turn", True, (255, 255, 255)),
                      self.font_prods.render(f"+ {25*self.level_mines} iron/turn, + {5*self.level_mines} gold/turn", True, (255, 255, 255)),
                      self.font_prods.render(f"+ {75*self.level_fields} food/turn", True, (255, 255, 255)),
                      self.font_prods.render(f"+ {60*self.level_sawmill} wood/turn", True, (255, 255, 255))]
        self.prods_rect = [i.get_rect() for i in self.prods]
        for i in range(4):
            self.prods_rect[i].right, self.prods_rect[i].centery = self.width - 110, 325 + (
                        (self.height - 460) // 4 + 10) * i

    def update_buttons_upgrade(self, prod):
        mouse_coo = pg.mouse.get_pos()

        self.font_buttons = pg.font.Font("ressources/Fonts/f014015d.woff", 20)
        self.buttons_upgrade = [
            self.font_buttons.render(f"Buy upgrade: {50 * (self.level_workers_housing + 1)} wood", True,
                                     (255, 255, 255)),
            self.font_buttons.render(
                f"Buy upgrade: {50 * (self.level_mines + 1)} wood, {10 * (self.level_mines + 1)} gold", True,
                (255, 255, 255)),
            self.font_buttons.render(
                f"Buy upgrade: {25 * (self.level_fields + 1)} wood, {5 * (self.level_mines + 1)} gold", True,
                (255, 255, 255)),
            self.font_buttons.render(f"Buy upgrade: {100 * (self.level_sawmill + 1)} food", True, (255, 255, 255))]
        self.buttons_upgrade_rect = [i.get_rect() for i in self.buttons_upgrade]

        for i in range(4):
            self.buttons_upgrade_rect[i].right, self.buttons_upgrade_rect[i].centery = self.width - 110, 380 + (
                        (self.height - 460) // 4 + 10) * i

        if prod["Housings"][0]:
            pg.draw.rect(self.screen, (255, 0, 0), self.buttons_upgrade_rect[0])
        else:
            pg.draw.rect(self.screen, (0, 255, 0), self.buttons_upgrade_rect[0])

        if prod["Mines"][0]:
            pg.draw.rect(self.screen, (255, 0, 0), self.buttons_upgrade_rect[1])
        else:
            pg.draw.rect(self.screen, (0, 255, 0), self.buttons_upgrade_rect[1])

        if prod["Fields"][0]:
            pg.draw.rect(self.screen, (255, 0, 0), self.buttons_upgrade_rect[2])
        else:
            pg.draw.rect(self.screen, (0, 255, 0), self.buttons_upgrade_rect[2])

        if prod["Sawmill"][0]:
            pg.draw.rect(self.screen, (255, 0, 0), self.buttons_upgrade_rect[3])
        else:
            pg.draw.rect(self.screen, (0, 255, 0), self.buttons_upgrade_rect[3])

        for i in range(4):
            self.screen.blit(self.buttons_upgrade[i], self.buttons_upgrade_rect[i])

    def update_upgrading(self, prod):

        if prod["Housings"][0]:
            self.upgrading[0] = self.upgrading_font.render(f"Upgrading: {prod['Housings'][1]} turn(s) left.", True, (255, 255, 255))
        else:
            self.upgrading[0] = self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255))
        if prod["Mines"][0]:
            self.upgrading[1] = self.upgrading_font.render(f"Upgrading: {prod['Mines'][1]} turn(s) left.", True, (255, 255, 255))
        else:
            self.upgrading[1] = self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255))
        if prod["Fields"][0]:
            self.upgrading[2] = self.upgrading_font.render(f"Upgrading: {prod['Fields'][1]} turn(s) left.", True, (255, 255, 255))
        else:
            self.upgrading[2] = self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255))
        if prod["Sawmill"][0]:
            self.upgrading[3] = self.upgrading_font.render(f"Upgrading: {prod['Sawmill'][1]} turn(s) left.", True, (255, 255, 255))
        else:
            self.upgrading[3] = self.upgrading_font.render(f"Upgrading: None", True, (255, 255, 255))

        self.upgrading_rect = [i.get_rect() for i in self.upgrading]
        for i in range(4):
            self.upgrading_rect[i].left, self.upgrading_rect[i].centery = self.width // 2 + 110, 370 + (
                        (self.height - 460) // 4 + 10) * i
            self.screen.blit(self.upgrading[i], self.upgrading_rect[i])

    def update(self, prod):
        mouse_coo = pg.mouse.get_pos()

        self.screen.blit(self.main_surf, (self.width // 2 + 50, 100))
        if self.exit_rect.collidepoint(mouse_coo):
            pg.draw.rect(self.screen, (255, 0, 0), self.exit_rect)
        self.screen.blit(self.exit, self.exit_rect)

        pg.draw.rect(self.screen, (0, 255, 0), self.upgrade_tabs_rect[self.current_tab])

        for i in range(4):
            self.screen.blit(self.upgrade_tabs[i], self.upgrade_tabs_rect[i])

        if self.current_tab == 0:
            self.screen.blit(self.surf_workers_housings, self.surf_workers_housings_rect)
            self.screen.blit(self.surf_mine, self.surf_mine_rect)
            self.screen.blit(self.surf_fields, self.surf_fields_rect)
            self.screen.blit(self.surf_sawmill, self.surf_sawmill_rect)

            for i in range(4):
                self.screen.blit(self.titles_infra[i], self.titles_infra_rect[i])
                pg.draw.line(self.screen, (255, 255, 255),
                             (self.width // 2 + 110, 350 + ((self.height - 460) // 4 + 10) * i),
                             (self.width - 110, 350 + ((self.height - 460) // 4 + 10) * i))
                self.update_prods()
                self.screen.blit(self.prods[i], self.prods_rect[i])
            self.update_buttons_upgrade(prod)
            self.update_upgrading(prod)
