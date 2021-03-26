import pygame as pg
import sys
from random import randint

import units as u
import Players as Pls
import Game_Animations as Ga
import Background_manager as Bm
import Enemy as En


class AttackDisplay:

    def __init__(self, screen, width, height, player1, player2):
        self.screen, self.width, self.height, self.player1, self.player2 = screen, width, height, player1, player2

        self.running_attack = True
        self.preparing = True
        self.attacking = False

        self.troops_p1 = self.player1.troops
        self.troops_p2 = self.player2.troops

        self.preparing_dp = DisplayPreparing(self.screen, self.troops_p1)

        self.new_troops1 = self.preparing_dp.new_troops_effective

        self.units_group1 = []
        self.units_group1_coo = []

        self.enemy_group = pg.sprite.Group()

        self.attacking_dp = DisplayAttacking(self.screen,
                                             self.screen.get_width(),
                                             self.screen.get_height(),
                                             self.units_group1,
                                             self.units_group1_coo,
                                             self.enemy_group)

        self.explosions_group = pg.sprite.Group()
        self.call_explosion = lambda x, y: self.explosions_group.add(Ga.SimpleExplosion((x, y)))
        self.call_explosion1 = lambda x, y: self.explosions_group.add(Ga.Explosion1((x, y)))
        self.call_explosion2 = lambda x, y: self.explosions_group.add(Ga.Explosion2((x, y)))
        self.call_explosion3 = lambda x, y: self.explosions_group.add(Ga.Explosion3((x, y)))
        self.call_explosion4 = lambda x, y: self.explosions_group.add(Ga.Explosion4((x, y)))
        self.call_explosion5 = lambda x, y: self.explosions_group.add(Ga.Explosion5((x, y)))
        self.call_nuke = lambda x, y: self.explosions_group.add(Ga.Nuke((x, y)))

        self.clock = pg.time.Clock()

    def __call__(self):
        self.main_display()

    def cancel(self):
        """Function to cancel current movement of the selected unity(ies)"""

        for i in self.units_group1:
            if i.clicked:
                i.moving = False
                i.movement = [0, 0]
                i.target = None
                i.last_target = None

    def fill_groups(self):

        """Function to complete the selection of the player's troops. This fill a group with the player's chosen
        troops (by the limit of his effective)"""

        self.new_troops1 = self.preparing_dp.new_troops_effective

        for i in range(self.new_troops1["snipers"][0]):
            self.units_group1.append(u.Sniper(self.screen, self.new_troops1["snipers"][1], self.width, self.height))
            self.units_group1_coo.append([randint(self.width // 4, self.width // 2), randint(self.height // 2, self.height - 25)])

        for i in range(self.new_troops1["artillery"][0]):
            self.units_group1.append(u.Artillery(self.screen, self.new_troops1["artillery"][1], self.width, self.height))
            self.units_group1_coo.append([randint(self.width // 4, self.width // 3), randint(self.height // 2 + 300, self.height - 25)])

        for i in range(self.new_troops1["infantry"][0]):
            self.units_group1.append(u.Infantry(self.screen, self.new_troops1["infantry"][1], self.width, self.height))
            self.units_group1_coo.append([randint(self.width // 4, self.width // 3), randint(self.height // 2 + 300, self.height - 25)])

        for i in range(self.new_troops1["cavalry"][0]):
            self.units_group1.append(u.Cavalry(self.screen, self.new_troops1["cavalry"][1], self.width, self.height))
            self.units_group1_coo.append([randint(self.width // 4, self.width // 3), randint(self.height // 2 + 300, self.height - 25)])

        for i in range(7):
            self.enemy_group.add(En.SniperEnemy(self.screen, 2, [randint(self.width // 2, self.width // 2 + self.width // 4),
                                                                 randint(self.height // 2, self.height - 25)]))

        self.attacking_dp = DisplayAttacking(self.screen,
                                             self.screen.get_width(),
                                             self.screen.get_height(),
                                             self.units_group1,
                                             self.units_group1_coo,
                                             self.enemy_group)

    def main_display(self):

        while self.running_attack:

            while self.preparing:

                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        self.running_attack = False
                        self.preparing = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.running_attack = False
                            self.preparing = False

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.preparing_dp.click(event.pos) == "switch":
                                self.preparing = False
                                self.attacking = True
                                self.fill_groups()
                                for i in self.units_group1:
                                    i.clicked = False
                                    try:
                                        i.selecting_fire = False
                                    except Exception as e:
                                        print(e)

                self.screen.fill((0, 0, 0))
                self.preparing_dp()

                self.clock.tick(60)
                pg.display.flip()

            while self.attacking:

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.attacking = False
                        self.running_attack = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.attacking = False
                            self.running_attack = False
                        if event.key == pg.K_SPACE:
                            self.cancel()

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1 and pg.key.get_mods() & pg.KMOD_SHIFT:
                            self.attacking_dp.ctrl_click()
                        elif event.button == 1:

                            self.attacking_dp.click()

                            self.attacking_dp.clicking = True
                            self.attacking_dp.dep_pos = pg.mouse.get_pos()

                        if event.button == 3:
                            self.attacking_dp.right_click()

                    if event.type == pg.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.attacking_dp.clicking = False
                            self.attacking_dp.dep_pos = (0, 0)
                            self.attacking_dp.find_selected()

                self.screen.fill((0, 0, 0))

                self.attacking_dp()
                self.explosions_group.draw(self.screen)
                self.explosions_group.update()

                pg.display.flip()
                self.clock.tick(60)


class DisplayPreparing:

    def __init__(self, mscreen, effective):
        self.screen = mscreen
        self.width = mscreen.get_width()
        self.height = mscreen.get_height()

        self.new_troops_effective = {
            "infantry": [0, effective["infantry"][1]],
            "cavalry": [0, effective["cavalry"][1]],
            "snipers": [0, effective["snipers"][1]],
            "artillery": [0, effective["artillery"][1]]
        }

        self.police = pg.font.Font("ressources/Fonts/f014015d.woff", 50)

        self.troops = [self.police.render("Infantry", True, (0, 0, 0)),
                       self.police.render("Cavalry", True, (0, 0, 0)),
                       self.police.render("Artillery", True, (0, 0, 0)),
                       self.police.render("Snipers Squad", True, (0, 0, 0))]
        self.troops_rect = [i.get_rect() for i in self.troops]

        self.troops_images = [pg.Surface(((self.width // 2) // 4 - 30, self.height // 2 - 50)),
                              pg.Surface(((self.width // 2) // 4 - 30, self.height // 2 - 50)),
                              pg.Surface(((self.width // 2) // 4 - 30, self.height // 2 - 50)),
                              pg.Surface(((self.width // 2) // 4 - 30, self.height // 2 - 50))]
        self.troops_images2 = [pg.Surface(((self.width // 2) // 4 - 30, (self.height // 2 - 50) * 1.1)),
                               pg.Surface(((self.width // 2) // 4 - 30, (self.height // 2 - 50) * 1.1)),
                               pg.Surface(((self.width // 2) // 4 - 30, (self.height // 2 - 50) * 1.1)),
                               pg.Surface(((self.width // 2) // 4 - 30, (self.height // 2 - 50) * 1.1))]

        for i in self.troops_images:
            i.fill((0, 0, 255))
        for i in self.troops_images2:
            i.fill((50, 255, 50))
        self.troops_rect = [i.get_rect() for i in self.troops_images]
        self.troops_rect2 = [i.get_rect() for i in self.troops_images2]
        for i in range(4):
            self.troops_rect[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2, \
                                         self.height // 4 + (self.height // 2 - 50) // 2
            self.troops_rect2[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2, \
                                          self.height // 4 + (self.height // 2 - 50) * 1.1 // 2

        self.font_effective = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.effective = [self.font_effective.render("Infantry battalion(s): 0", True, (0, 0, 0)),
                          self.font_effective.render("Cavalry detachment(s): 0", True, (0, 0, 0)),
                          self.font_effective.render("Artillery squadron(s): 0", True, (0, 0, 0)),
                          self.font_effective.render("Snipers squad(s): 0", True, (0, 0, 0))]
        self.effective_rect = [i.get_rect() for i in self.effective]
        for i in range(4):
            self.effective_rect[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2, self.height // 4 + 40

        self.font_effective = pg.font.Font("ressources/Fonts/f014015d.woff", 20)
        self.effective2 = [self.font_effective.render("Infantry battalion(s): 0", True, (0, 0, 0)),
                           self.font_effective.render("Cavalry detachment(s): 0", True, (0, 0, 0)),
                           self.font_effective.render("Artillery squadron(s): 0", True, (0, 0, 0)),
                           self.font_effective.render("Snipers squad(s): 0", True, (0, 0, 0))]
        self.effective_rect2 = [i.get_rect() for i in self.effective]
        for i in range(4):
            self.effective_rect2[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2, self.height // 4 + 40

        self.font_title = pg.font.Font("ressources/Fonts/f014015d.woff", 75)
        self.title = self.font_title.render("Select your troops for the battle !", True, (0, 0, 0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.width // 2, self.height // 5

        self.buttons_filled = [
            [pg.image.load("ressources/Icons/plus.png"), pg.image.load("ressources/Icons/moins.png")],
            [pg.image.load("ressources/Icons/plus.png"), pg.image.load("ressources/Icons/moins.png")],
            [pg.image.load("ressources/Icons/plus.png"), pg.image.load("ressources/Icons/moins.png")],
            [pg.image.load("ressources/Icons/plus.png"), pg.image.load("ressources/Icons/moins.png")]]
        self.buttons_filled_rect = [[self.buttons_filled[0][0].get_rect(),
                                     self.buttons_filled[0][1].get_rect()],
                                    [self.buttons_filled[1][0].get_rect(),
                                     self.buttons_filled[1][1].get_rect()],
                                    [self.buttons_filled[2][0].get_rect(),
                                     self.buttons_filled[2][1].get_rect()],
                                    [self.buttons_filled[3][0].get_rect(),
                                     self.buttons_filled[3][1].get_rect()]]

        self.buttons_unfilled = [[pg.image.load("ressources/Icons/plus-blank.png"),
                                  pg.image.load("ressources/Icons/moins-blank.png")],
                                 [pg.image.load("ressources/Icons/plus-blank.png"),
                                  pg.image.load("ressources/Icons/moins-blank.png")],
                                 [pg.image.load("ressources/Icons/plus-blank.png"),
                                  pg.image.load("ressources/Icons/moins-blank.png")],
                                 [pg.image.load("ressources/Icons/plus-blank.png"),
                                  pg.image.load("ressources/Icons/moins-blank.png")]]
        self.buttons_unfilled_rect = [[self.buttons_unfilled[0][0].get_rect(),
                                       self.buttons_unfilled[0][1].get_rect()],
                                      [self.buttons_unfilled[1][0].get_rect(),
                                       self.buttons_unfilled[1][1].get_rect()],
                                      [self.buttons_unfilled[2][0].get_rect(),
                                       self.buttons_unfilled[2][1].get_rect()],
                                      [self.buttons_unfilled[3][0].get_rect(),
                                       self.buttons_unfilled[3][1].get_rect()]]

        for i in range(4):
            for z in range(2):
                if z == 0:
                    self.buttons_filled_rect[i][z].center = (self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                            (self.width // 2) // 4 - 30) // 2) - 50, \
                                                            ((self.height // 2 - 50) * 1.1) + self.height // 4 - 50
                    self.buttons_unfilled_rect[i][z].center = self.buttons_filled_rect[i][z].center
                else:
                    self.buttons_filled_rect[i][z].center = (self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                            (self.width // 2) // 4 - 30) // 2) + 50, \
                                                            ((self.height // 2 - 50) * 1.1) + self.height // 4 - 50
                    self.buttons_unfilled_rect[i][z].center = self.buttons_filled_rect[i][z].center

        self.confirm_button = self.font_title.render("confirm", True, (0, 0, 0))
        self.confirm_button_rect = self.confirm_button.get_rect(center=(self.width//2, self.height-50))

    def __call__(self):
        self.main_display()

    def update_font(self):

        self.font_effective = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.effective = [self.font_effective.render(f"Infantry battalion(s): {self.new_troops_effective['infantry'][0]}",
                                                     True, (0, 0, 0)),
                          self.font_effective.render(f"Cavalry detachment(s): {self.new_troops_effective['cavalry'][0]}",
                                                     True, (0, 0, 0)),
                          self.font_effective.render(f"Artillery squadron(s): {self.new_troops_effective['artillery'][0]}",
                                                     True, (0, 0, 0)),
                          self.font_effective.render(f"Snipers squad(s): {self.new_troops_effective['snipers'][0]}",
                                                     True, (0, 0, 0))]
        self.effective_rect = [i.get_rect() for i in self.effective]
        for i in range(4):
            self.effective_rect[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2, self.height // 4 + 40

        self.font_effective = pg.font.Font("ressources/Fonts/f014015d.woff", 20)
        self.effective2 = [self.font_effective.render(f"Infantry battalion(s): {self.new_troops_effective['infantry'][0]}",
                                                      True, (0, 0, 0)),
                           self.font_effective.render(f"Cavalry detachment(s): {self.new_troops_effective['cavalry'][0]}",
                                                      True, (0, 0, 0)),
                           self.font_effective.render(f"Artillery squadron(s): {self.new_troops_effective['artillery'][0]}",
                                                      True, (0, 0, 0)),
                           self.font_effective.render(f"Snipers squad(s): {self.new_troops_effective['snipers'][0]}",
                                                      True, (0, 0, 0))]
        self.effective_rect2 = [i.get_rect() for i in self.effective]
        for i in range(4):
            self.effective_rect2[i].center = self.width // 4 + (self.width // 2 // 4 + 5) * i + 5 + (
                    (self.width // 2) // 4 - 30) // 2 - 25, self.height // 4 + 40

    def click(self, pos):
        if self.buttons_filled_rect[0][0].collidepoint(pos):
            if self.new_troops_effective["infantry"][0] < Player1.troops["infantry"][0]:
                self.new_troops_effective["infantry"][0] += 1
        if self.buttons_filled_rect[0][1].collidepoint(pos):
            if self.new_troops_effective["infantry"][0] > 0:
                self.new_troops_effective["infantry"][0] -= 1

        if self.buttons_filled_rect[1][0].collidepoint(pos):
            if self.new_troops_effective["cavalry"][0] < Player1.troops["cavalry"][0]:
                self.new_troops_effective["cavalry"][0] += 1
        if self.buttons_filled_rect[1][1].collidepoint(pos):
            if self.new_troops_effective["cavalry"][0] > 0:
                self.new_troops_effective["cavalry"][0] -= 1

        if self.buttons_filled_rect[2][0].collidepoint(pos):
            if self.new_troops_effective["artillery"][0] < Player1.troops["artillery"][0]:
                self.new_troops_effective["artillery"][0] += 1
        if self.buttons_filled_rect[2][1].collidepoint(pos):
            if self.new_troops_effective["artillery"][0] > 0:
                self.new_troops_effective["artillery"][0] -= 1

        if self.buttons_filled_rect[3][0].collidepoint(pos):
            if self.new_troops_effective["snipers"][0] < Player1.troops["snipers"][0]:
                self.new_troops_effective["snipers"][0] += 1
        if self.buttons_filled_rect[3][1].collidepoint(pos):
            if self.new_troops_effective["snipers"][0] > 0:
                self.new_troops_effective["snipers"][0] -= 1

        if self.confirm_button_rect.collidepoint(pos):
            return "switch"

    def main_display(self):

        mouse_coo = pg.mouse.get_pos()

        self.screen.fill((100, 100, 100))
        pg.draw.rect(self.screen, (255, 255, 255),
                     [self.width // 4, self.height // 4, self.width // 2, self.height // 2])

        for i in range(4):
            if self.troops_rect2[i].collidepoint(mouse_coo):
                self.screen.blit(self.troops_images2[i], self.troops_rect2[i])
                self.screen.blit(self.effective2[i], self.effective_rect2[i])
                for z in range(2):
                    if not self.buttons_filled_rect[i][z].collidepoint(mouse_coo):
                        self.screen.blit(self.buttons_filled[i][z], self.buttons_filled_rect[i][z])
                    else:
                        self.screen.blit(self.buttons_unfilled[i][z], self.buttons_unfilled_rect[i][z])
            else:
                self.screen.blit(self.troops_images[i], self.troops_rect[i])
                self.screen.blit(self.effective[i], self.effective_rect[i])

        if self.confirm_button_rect.collidepoint(mouse_coo):
            pg.draw.rect(self.screen, (255, 0, 0), self.confirm_button_rect)
        else:
            pg.draw.rect(self.screen, (255, 255, 255), self.confirm_button_rect)
        self.screen.blit(self.confirm_button, self.confirm_button_rect)

        self.screen.blit(self.title, self.title_rect)
        self.update_font()


class DisplayAttacking:

    def __init__(self, screen, width, height, group1, group1_coo, enemies_group):
        self.screen, self.width, self.height = screen, width, height
        self.un_group1 = group1
        self.un_group1_coo = group1_coo

        self.enemies_group = enemies_group

        self.clicking = False
        self.dep_pos = (0, 0)
        self.select_rect = pg.Rect(0, 0, 1, 1)

        self.background_moon = Bm.Moon(self.screen, self.width, self.height)

    def __call__(self):
        self.main_display()

    def polygon_stuff(self):
        pg.draw.polygon(self.screen, (180, 110, 0), [(0, self.height),
                                                     (self.width // 4, self.height // 3),
                                                     (self.width // 2, self.height // 3),
                                                     (self.width // 2, self.height)])
        pg.draw.polygon(self.screen, (180, 110, 0), [(self.width // 2, self.height // 3),
                                                    (self.width - self.width // 4, self.height // 3),
                                                    (self.width, self.height),
                                                    (self.width // 2, self.height)])
        pg.draw.line(self.screen, (180, 110, 0), (self.width // 4, self.height // 3), (self.width // 4, 0))
        pg.draw.line(self.screen, (180, 110, 0), (self.width - self.width // 4, self.height // 3),
                     (self.width - self.width // 4, 0))

    def draw_selection(self):
        coo = pg.mouse.get_pos()

        if coo[0]-self.dep_pos[0] > 0 and coo[1]-self.dep_pos[1] > 0:
            self.select_rect = pg.Rect(self.dep_pos[0], self.dep_pos[1], coo[0]-self.dep_pos[0], coo[1]-self.dep_pos[1])
        elif coo[0]-self.dep_pos[0] > 0 and coo[1]-self.dep_pos[1] < 0:
            self.select_rect = pg.Rect(self.dep_pos[0], coo[1], coo[0]-self.dep_pos[0], self.dep_pos[1]-coo[1])
        elif coo[0]-self.dep_pos[0] < 0 and coo[1]-self.dep_pos[1] > 0:
            self.select_rect = pg.Rect(coo[0], self.dep_pos[1], abs(self.dep_pos[0] - coo[0]), abs(self.dep_pos[1] - coo[1]))
        elif coo[0]-self.dep_pos[0] < 0 and coo[1] - self.dep_pos[1] < 0:
            self.select_rect = pg.Rect(coo[0], coo[1], abs(self.dep_pos[0] - coo[0]), abs(self.dep_pos[1] - coo[1]))

        surf = pg.Surface((self.select_rect.width, self.select_rect.height))
        surf.fill((0, 0, 255))
        surf.set_alpha(100)
        self.screen.blit(surf, self.select_rect)

    def find_selected(self):
        for i in range(len(self.un_group1)):
            if self.un_group1[i].rect.colliderect(self.select_rect):
                self.un_group1[i].clicked = True
        self.select_rect = pg.Rect(0, 0, 1, 1)

    def click(self):
        for i in range(len(self.un_group1)):
            self.un_group1[i].click()

    def right_click(self):
        for i in range(len(self.un_group1)):
            self.un_group1[i].right_click()

    def ctrl_click(self):
        for i in range(len(self.un_group1)):
            self.un_group1[i].ctrl_click()

    def main_display(self):
        # self.polygon_stuff()
        self.background_moon()

        self.enemies_group.draw(self.screen)
        self.enemies_group.update(False)

        for i in range(len(self.un_group1)):
            self.un_group1[i].update(self.un_group1_coo[i], self.enemies_group)
            try:
                self.un_group1_coo[i][0] += self.un_group1[i].update(self.un_group1_coo[i], self.enemies_group)[0]
                self.un_group1_coo[i][1] += self.un_group1[i].update(self.un_group1_coo[i], self.enemies_group)[1]
            except TypeError:
                pass

        if self.clicking:
            self.draw_selection()


if __name__ == '__main__':
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    Player1 = Pls.Player1()
    Player2 = Pls.Player2()

    pg.init()
    display = AttackDisplay(screen, 1920, 1080, Player1, Player2)
    display()
    pg.quit()
    sys.exit()
