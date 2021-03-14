import pygame as pg
import popup as pu
import display_countries as dc
import map_display as md


class MainDisplay:

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.width = screen_width
        self.height = screen_height

        self.main_surface = pg.image.load("ressources/Maps/world_map.jpg")
        self.main_surface = pg.transform.scale(self.main_surface, (self.width, self.height))

        self.resources_bar = ResourcesBar(screen, screen_width, screen_height)
        self.turn_options = TurnOptions(screen, screen_width, screen_height)
        self.map_display = md.MainMap(screen, screen_width, screen_height)

        self.france = dc.France(screen, screen_width, screen_height)
        self.france_surf = pg.Surface((300, 300))
        self.france_rect = self.france_surf.get_rect()
        self.france_surf.fill((255, 0, 0))
        self.france_rect.center = self.width // 2, self.height // 2

        self.player_gold = 0
        self.player_iron = 0
        self.player_food = 0
        self.player_work_force = 0
        self.player_wood = 0
        self.player_land = 0

        # values telling if the game is watching to a country, so that the game can display in function of this
        self.watching_country = False
        self.country_watched = None

    def update_resources(self, resources=list):
        self.player_gold = resources[0]
        self.player_iron = resources[1]
        self.player_food = resources[2]
        self.player_work_force = resources[3]
        self.player_wood = resources[4]
        self.player_land = resources[5]

    def main_display(self, current_turn, prod_w_eu):

        """Manage all the screen during the game"""

        self.screen.fill((255, 255, 255))

        if self.watching_country:
            if self.country_watched == "france":
                self.france.update(prod_w_eu)
        else:
            self.map_display.update()

        self.turn_options.update(current_turn)

        self.resources_bar.update(self.player_gold, self.player_iron,
                                  self.player_food, self.player_work_force,
                                  self.player_wood, self.player_land)


class ResourcesBar:

    def __init__(self, screen, width, height):
        self.main_surf = pg.Surface((width, 50))
        self.main_surf.fill((0, 100, 255))

        self.screen, self.width, self.height = screen, width, height

        self.resources_font = pg.font.Font("ressources/Fonts/f014015d.woff", 25)

        self.resources = [self.resources_font.render("Gold: 0", True, (255, 255, 255)),
                          self.resources_font.render("Iron: 0", True, (255, 255, 255)),
                          self.resources_font.render("Food: 0", True, (255, 255, 255)),
                          self.resources_font.render("Work Force: 0", True, (255, 255, 255)),
                          self.resources_font.render("Wood: 0", True, (255, 255, 255)),
                          self.resources_font.render("Land: 0", True, (255, 255, 255))]
        self.resources_rect = [i.get_rect() for i in self.resources]

        self.resources_rect[0].left = 25
        self.resources_rect[1].left = 25 + self.resources[0].get_width() + 25
        self.resources_rect[2].left = 25 + self.resources[0].get_width() + 25 + \
                                      self.resources[1].get_width() + 25
        self.resources_rect[3].left = 25 + self.resources[0].get_width() + 25 + \
                                      self.resources[1].get_width() + 25 + self.resources[2].get_width() + 25
        self.resources_rect[4].left = 25 + self.resources[0].get_width() + 25 + self.resources[1].get_width() + 25 + \
                                      self.resources[2].get_width() + 25 + self.resources[3].get_width() + 25
        self.resources_rect[5].left = 25 + self.resources[0].get_width() + 25 + self.resources[1].get_width() + 25 + \
                                      self.resources[2].get_width() + 25 + self.resources[3].get_width() + 25 + \
                                      self.resources[4].get_width() + 25

        for i in range(6):
            self.resources_rect[i].centery = 25
            self.screen.blit(self.resources[i], self.resources_rect[i])

        # all classes which will contain resources explanations
        self.pop_up_gold = pu.PopUpGold(screen)
        self.pop_up_iron = pu.PopUpIron(screen)
        self.pop_up_food = pu.PopUpFood(screen)
        self.pop_up_wf = pu.PopUpWF(screen)
        self.pop_up_wood = pu.PopUpWood(screen)
        self.pop_up_land = pu.PopUpLand(screen)

    def update_resources(self, gold, iron, food, work_force, wood, land):

        self.resources = [self.resources_font.render(f"Gold: {gold}", True, (255, 255, 255)),
                          self.resources_font.render(f"Iron: {iron}", True, (255, 255, 255)),
                          self.resources_font.render(f"Food: {food}", True, (255, 255, 255)),
                          self.resources_font.render(f"Work Force: {work_force}", True, (255, 255, 255)),
                          self.resources_font.render(f"Wood: {wood}", True, (255, 255, 255)),
                          self.resources_font.render(f"Land: {land}", True, (255, 255, 255))]
        self.resources_rect = [i.get_rect() for i in self.resources]

        self.resources_rect[0].left = 25
        self.resources_rect[1].left = 25 + self.resources[0].get_width() + 25
        self.resources_rect[2].left = 25 + self.resources[0].get_width() + 25 + \
                                      self.resources[1].get_width() + 25
        self.resources_rect[3].left = 25 + self.resources[0].get_width() + 25 + \
                                      self.resources[1].get_width() + 25 + self.resources[2].get_width() + 25
        self.resources_rect[4].left = 25 + self.resources[0].get_width() + 25 + self.resources[1].get_width() + 25 + \
                                      self.resources[2].get_width() + 25 + self.resources[3].get_width() + 25
        self.resources_rect[5].left = 25 + self.resources[0].get_width() + 25 + self.resources[1].get_width() + 25 + \
                                      self.resources[2].get_width() + 25 + self.resources[3].get_width() + 25 + \
                                      self.resources[4].get_width() + 25

        for i in range(6):
            self.resources_rect[i].centery = 25
            self.screen.blit(self.resources[i], self.resources_rect[i])

    def update(self, gold, iron, food, work_force, wood, land):

        mouse_coo = pg.mouse.get_pos()

        self.screen.blit(self.main_surf, (0, 0))
        self.update_resources(gold, iron, food, work_force, wood, land)

        if self.resources_rect[0].collidepoint(mouse_coo):
            self.pop_up_gold.update_(mouse_coo)
        if self.resources_rect[1].collidepoint(mouse_coo):
            self.pop_up_iron.update_(mouse_coo)
        if self.resources_rect[2].collidepoint(mouse_coo):
            self.pop_up_food.update_(mouse_coo)
        if self.resources_rect[3].collidepoint(mouse_coo):
            self.pop_up_wf.update_(mouse_coo)
        if self.resources_rect[4].collidepoint(mouse_coo):
            self.pop_up_wood.update_(mouse_coo)
        if self.resources_rect[5].collidepoint(mouse_coo):
            self.pop_up_land.update_(mouse_coo)


class TurnOptions:

    def __init__(self, screen, width, height):

        self.screen, self.width, self.height = screen, width, height
        self.button_next_turn = pg.Surface((150, 150))
        self.button_next_turn.fill((0, 255, 0))
        self.button_next_turn_rect = self.button_next_turn.get_rect()
        self.button_next_turn_rect.bottom = self.height
        self.button_next_turn_rect.right = self.width

        self.font_actual_turn = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.current_turn = self.font_actual_turn.render("Turn: 0", True, (0, 0, 0))
        self.current_turn_rect = self.current_turn.get_rect()
        self.current_turn_rect.bottom = self.height - 160
        self.current_turn_rect.right = self.width - 10

    def update_turn(self, turn):
        self.font_actual_turn = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.current_turn = self.font_actual_turn.render(f"Turn: {turn}", True, (0, 0, 0))
        self.current_turn_rect = self.current_turn.get_rect()
        self.current_turn_rect.bottom = self.height - 160
        self.current_turn_rect.right = self.width - 10

    def update(self, current_turn):
        self.screen.blit(self.button_next_turn, self.button_next_turn_rect)
        self.update_turn(current_turn)
        self.screen.blit(self.current_turn, self.current_turn_rect)
