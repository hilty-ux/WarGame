import pygame as pg
import sys
import screeninfo

import game_display as gd
import menu_display as md


class WarGame:

    def __init__(self, main_screen, screen_width, screen_height):

        # getting all variables inputted at the class initialization
        self.screen = main_screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        # defining my main loop's condition
        self.running = True
        self.game = False
        self.menu = True
        self.current_time = 0

        # initializing main_display class which manage all the screen display during game
        self.main_display = gd.MainDisplay(self.screen, self.screen_width, self.screen_height)

        # initializing menu_display class which manage all the screen display during menu
        self.menu_display = md.MenuDisplay(self.screen, self.screen_width, self.screen_height)

        # all values of the player at the beginning of the game
        self.current_turn = 1
        self.delay_changing_turn = pg.time.get_ticks()
        self.turn_able = True

        self.player_gold = 100
        self.player_iron = 0
        self.player_food = 50
        self.player_work_force = 5
        self.player_wood = 200
        self.player_land = 0

        # all incomes of the player
        self.gold_income = 5
        self.iron_income = 0
        self.food_income = 0
        self.work_force_income = 0
        self.wood_income = 0

        self.production_france = {
            "Housings": [False, 0],
            "Mines": [False, 0],
            "Fields": [False, 0],
            "Sawmill": [False, 0]
        }

        self.main_display.update_resources([self.player_gold, self.player_iron,
                                            self.player_food, self.player_work_force,
                                            self.player_wood, self.player_land])

    def production(self):

        self.gold_income = 1
        self.iron_income = 0
        self.food_income = 0
        self.work_force_income = 0
        self.wood_income = 0

        if self.production_france["Housings"][0]:
            self.production_france["Housings"][1] -= 1
            if self.production_france["Housings"][1] == 0:
                self.main_display.france.level_workers_housing += 1
                if self.production_france["Housings"][1] < 5:
                    self.production_france["Housings"][0] = False
                else:
                    self.production_france["Housings"][0] = True

        if self.production_france["Mines"][0]:
            self.production_france["Mines"][1] -= 1
            if self.production_france["Mines"][1] == 0:
                self.main_display.france.level_mines += 1
                self.production_france["Mines"][0] = False

        if self.production_france["Fields"][0]:
            self.production_france["Fields"][1] -= 1
            if self.production_france["Fields"][1] == 0:
                self.main_display.france.level_fields += 1
                self.production_france["Fields"][0] = False

        if self.production_france["Sawmill"][0]:
            self.production_france["Sawmill"][1] -= 1
            if self.production_france["Sawmill"][1] == 0:
                self.main_display.france.level_sawmill += 1
                self.production_france["Sawmill"][0] = False

        if self.main_display.france.owner == "Player":
            self.gold_income += self.main_display.france.level_mines * 5
            self.iron_income += self.main_display.france.level_mines * 25
            self.food_income += self.main_display.france.level_fields * 75
            self.work_force_income += self.main_display.france.level_workers_housing * 10
            self.wood_income += self.main_display.france.level_sawmill * 60

        self.main_display.france.update_buttons_upgrade(self.production_france)
        self.main_display.france.update_upgrading(self.production_france)

    def change_turn(self):
        self.current_turn += 1

        self.production()

        self.player_gold += self.gold_income
        self.player_iron += self.iron_income
        self.player_food += self.food_income
        self.player_work_force += self.work_force_income
        self.player_wood += self.wood_income

        self.main_display.update_resources([self.player_gold, self.player_iron,
                                            self.player_food, self.player_work_force,
                                            self.player_wood, self.player_land])

        self.main_display.watching_country = False
        self.main_display.country_watched = None

    def manage_buttons_zoom(self, event):

        if self.main_display.watching_country and self.main_display.country_watched == "france":
            if self.main_display.france.exit_rect.collidepoint(event.pos):
                self.main_display.watching_country = False
                self.main_display.country_watched = None

            if self.main_display.france.buttons_upgrade_rect[0].collidepoint(event.pos) and self.player_wood > 50 * (
                    self.main_display.france.level_workers_housing + 1) and not self.production_france["Housings"][0]:
                self.production_france["Housings"][0] = True
                self.production_france["Housings"][1] = (
                                                                    self.main_display.france.level_workers_housing + 1) * 10 // self.player_work_force + 1
                self.player_wood -= 50 * (self.main_display.france.level_workers_housing + 1)
                self.main_display.france.update_buttons_upgrade(self.production_france)
                self.main_display.france.update_upgrading(self.production_france)

            if self.main_display.france.buttons_upgrade_rect[1].collidepoint(event.pos) and self.player_wood >= 50 * (
                    self.main_display.france.level_mines + 1) and self.player_gold >= 10 * (
                    self.main_display.france.level_mines + 1) and not self.production_france["Mines"][0]:
                self.production_france["Mines"][0] = True
                self.production_france["Mines"][1] = (self.main_display.france.level_mines + 1) * 50 // self.player_work_force + 1
                self.player_wood -= 50 * (self.main_display.france.level_mines + 1)
                self.player_gold -= 10 * (self.main_display.france.level_mines + 1)
                self.main_display.france.update_buttons_upgrade(self.production_france)
                self.main_display.france.update_upgrading(self.production_france)

            if self.main_display.france.buttons_upgrade_rect[2].collidepoint(event.pos) and self.player_wood >= 25 * (
                    self.main_display.france.level_fields + 1) and self.player_gold > 5 * (
                    self.main_display.france.level_fields + 1) and not self.production_france["Fields"][0]:
                self.production_france["Fields"][0] = True
                self.production_france["Fields"][1] = (self.main_display.france.level_fields + 1) * 25 // self.player_work_force + 1
                self.player_wood -= 25 * (self.main_display.france.level_fields + 1)
                self.player_gold -= 5 * (self.main_display.france.level_fields + 1)
                self.main_display.france.update_buttons_upgrade(self.production_france)
                self.main_display.france.update_upgrading(self.production_france)

            if self.main_display.france.buttons_upgrade_rect[3].collidepoint(event.pos) and self.player_food >= 100 * (
                    self.main_display.france.level_sawmill + 1) and not self.production_france["Sawmill"][0]:
                self.production_france["Sawmill"][0] = True
                self.production_france["Sawmill"][1] = (
                                                                   self.main_display.france.level_sawmill + 1) * 15 // self.player_work_force + 1
                self.player_food -= 100 * (self.main_display.france.level_sawmill + 1)
                self.main_display.france.update_buttons_upgrade(self.production_france)
                self.main_display.france.update_upgrading(self.production_france)

        self.main_display.update_resources([self.player_gold, self.player_iron,
                                            self.player_food, self.player_work_force,
                                            self.player_wood, self.player_land])
        self.main_display.france.update_buttons_upgrade(self.production_france)
        self.main_display.france.update_upgrading(self.production_france)
        self.main_display.resources_bar.update(self.player_gold, self.player_iron,
                                               self.player_food, self.player_work_force,
                                               self.player_wood, self.player_land)

    def main_loop(self):

        while self.running:

            while self.game:

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.game = False
                        self.running = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.game = False
                            self.running = False

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:

                            if not self.main_display.watching_country:
                                self.main_display.map_display.click()

                            if self.main_display.turn_options.button_next_turn_rect.collidepoint(event.pos) and self.turn_able:
                                self.change_turn()
                                self.delay_changing_turn = self.current_time

                            if self.main_display.map_display.condition_france and not self.main_display.watching_country and self.main_display.france.owner == "Player":
                                self.main_display.watching_country = True
                                self.main_display.country_watched = "france"

                            self.manage_buttons_zoom(event)

                            for i in range(4):
                                if self.main_display.france.upgrade_tabs_rect[i].collidepoint(event.pos):
                                    self.main_display.france.current_tab = i

                if self.current_time - self.delay_changing_turn < 1000:
                    self.main_display.turn_options.button_next_turn.fill((255, 0, 0))
                    self.turn_able = False
                else:
                    self.main_display.turn_options.button_next_turn.fill((0, 255, 0))
                    self.turn_able = True

                self.main_display.main_display(self.current_turn, self.production_france)
                self.current_time = pg.time.get_ticks()

                pg.display.flip()

            while self.menu:

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.menu = False
                        self.running = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.menu = False
                            self.running = False

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.menu_display.buttons_highlighted_rect[3].collidepoint(event.pos):
                                self.menu = False
                                self.running = False

                            if self.menu_display.buttons_highlighted_rect[0].collidepoint(event.pos):
                                self.menu = False
                                self.game = True

                self.menu_display.main_display()

                pg.display.flip()


if __name__ == '__main__':
    # get all screens_sizes
    # (thanks to 'rr-'(stackoverflow user) who created the 'screeninfo' module which is really useful)
    list_monitors_sizes = [str(monitors).split(",") for monitors in screeninfo.get_monitors()]

    print(list_monitors_sizes[0])

    # transform size values into computer readable values
    for i in range(len(list_monitors_sizes)):
        for b in range(len(list_monitors_sizes[i])):
            actual_num = ''
            for z in list_monitors_sizes[i][b]:
                if z.isdigit():
                    actual_num += str(z)
            list_monitors_sizes[i][b] = actual_num

    # screen is completely filling the screen (full screen) so we don't set precise values to size the screen '(0, 0)'
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.init()  # initialize pygame
    # initialize the game class with screen object, and screen sizes values
    war_game = WarGame(screen, int(list_monitors_sizes[0][2]), int(list_monitors_sizes[0][3]))
    # playing the game loop (infinite until the player stop it manually by pressing ESCAPE or quiting in the menu)
    war_game.main_loop()
    pg.quit()  # quit the pygame module
    sys.exit()  # exit from the code
