import pygame as pg
import math
import random
from random import randint
import Projectile as Pr
import Game_Animations as Ga


class Sniper:

    def __init__(self, screen, level, width, height):

        self.screen, self.width, self.height = screen, width, height

        self.life = 100

        self.image = pg.Surface((self.width * (25/self.width), self.height * (25/self.height)))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.level_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.level = self.level_font.render(str(level), True, (0, 0, 0))
        self.level_rect = self.level.get_rect()

        self.clicked = False
        self.moving = False
        self.movement = [0, 0]
        self.reach_point = (self.rect.x, self.rect.y)
        self.target = None

        self.velocity = 1.1

        self.all_enemies_group = pg.sprite.Group()

        self.projectile_group = pg.sprite.Group()
        self.shoot_projectile = lambda x, y: self.projectile_group.add(Pr.SniperBullet(
            (self.rect.centerx, self.rect.centery), (x, y)))

        self.sniper_sound = pg.mixer.Sound("ressources/Sounds/514228__superphat__sniper-rifle.wav")
        self.sniper_sound.set_volume(0.5)

        self.reach_len = self.width * (300/self.width)

    def draw_life_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                              self.image.get_width(), 5])
        pg.draw.rect(self.screen, (0, 255, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                                (self.image.get_width() / 100)*self.life, 5])

    def draw_direction(self):
        pg.draw.line(self.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), self.reach_point, width=2)

    def define_movement(self, pos):

        angle = math.atan2(pos[1]-self.rect.y, pos[0]-self.rect.x)

        self.movement[0] = math.cos(angle)*self.velocity
        self.movement[1] = math.sin(angle)*self.velocity

        self.reach_point = pos

    def click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True
        else:
            if self.clicked:
                self.clicked = False

    def right_click(self):

        clicked_enemy = self.find_clicked_enemy()

        if self.clicked:
            if clicked_enemy is not None:
                if self.reachable(clicked_enemy):
                    self.target = clicked_enemy
                    self.shoot()
            else:
                self.define_movement(pg.mouse.get_pos())
                self.moving = True

    def find_clicked_enemy(self):
        for i in self.all_enemies_group:
            if i.rect.collidepoint(pg.mouse.get_pos()):
                return i
        return None

    def ctrl_click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True

    def reachable(self, obj):
        dist = math.sqrt((self.rect.centerx-obj.rect.x)**2 + (self.rect.centery-obj.rect.y)**2)
        if not self.moving:
            if dist < self.reach_len:
                return True
        return False

    def shoot(self):
        if self.target is not None:
            self.shoot_projectile(self.target.rect.centerx + random.randint(-1, 1), self.target.rect.centery + random.randint(-1, 1))
        self.sniper_sound.play()

    def update(self, coordinates, enemies_group):
        self.rect.center = coordinates
        self.level_rect.center = coordinates
        self.all_enemies_group = enemies_group

        if self.clicked:
            if self.moving:
                pass
            else:
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), self.reach_len, width=1)
            self.image.fill((0, 50, 255))
            self.draw_life_bar()
        else:
            self.image.fill((0, 255, 0))

        if self.reach_point[0] - 10 < self.rect.x < self.reach_point[0] + 10 and \
                self.reach_point[1] - 10 < self.rect.y < self.reach_point[1] + 10:
            self.moving = False
            self.movement = [0, 0]

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.level, self.level_rect)
        self.all_enemies_group.draw(self.screen)
        self.all_enemies_group.update(None)
        self.projectile_group.draw(self.screen)
        self.projectile_group.update()

        if self.target is not None:
            print(self.target)
            for i in self.projectile_group:
                if i.rect.colliderect(self.target.rect):
                    self.target.update(25)
                    i.kill()

        if self.moving:
            if self.clicked:
                self.draw_direction()
            self.rect.x += self.movement[0]
            self.rect.y += self.movement[1]
            return self.movement


class Artillery:

    def __init__(self, screen, level, width, height):
        self.screen = screen

        self.width, self.height = width, height

        self.life = 150

        self.image = pg.Surface((50, 25))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.level_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.level = self.level_font.render(str(level), True, (0, 0, 0))
        self.level_rect = self.level.get_rect()

        self.clicked = False
        self.moving = False
        self.movement = [0, 0]
        self.reach_point = (self.rect.x, self.rect.y)
        self.target = None
        self.hit_once = False
        self.reloading = False

        self.shot_button = pg.Surface((100, 100))
        self.shot_button.fill((255, 0, 0))
        self.shot_button_rect = self.shot_button.get_rect(left=0, y=self.height-100)

        self.velocity = 0.45

        self.all_enemies_group = pg.sprite.Group()

        self.projectile_group = pg.sprite.Group()
        self.shoot_projectile = lambda x, y: self.projectile_group.add(Pr.ArtilleryShot(
            (self.rect.centerx, self.rect.centery), (x, y)))

        self.artillery_sound = pg.mixer.Sound("ressources/Sounds/artillery.wav")
        self.artillery_sound.set_volume(0.15)

        self.selecting_fire = False

        self.group_explosions = pg.sprite.Group()
        self.call_explosion = lambda x, y: self.group_explosions.add(Ga.SimpleExplosion((x, y)))

        self.hit_enemies = []

        self.current_time = pg.time.get_ticks()
        self.reload_delay = pg.time.get_ticks()

        self.rdy_font = pg.font.Font("ressources/Fonts/f014015d.woff", 10)
        self.rdy = self.rdy_font.render("ready !", True, (0, 0, 0))
        self.rdy_rect = self.rdy.get_rect()

        self.reach_len = self.width * (800/self.width)

    def reload_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                              self.image.get_width(), 5])
        if self.reloading:
            delay = self.current_time - self.reload_delay
            pg.draw.rect(self.screen, (0, 200, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                                    (self.image.get_width() / 10000)*delay, 5])
        else:
            pg.draw.rect(self.screen, (0, 200, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                                    self.image.get_width(), 5])
            self.rdy_rect.center = self.rect.x + 25, self.rect.y + 37
            self.screen.blit(self.rdy, self.rdy_rect)

    def draw_life_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                              self.image.get_width(), 5])
        pg.draw.rect(self.screen, (0, 255, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                                (self.image.get_width()/150)*self.life, 5])

    def draw_direction(self):
        pg.draw.line(self.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), self.reach_point, width=2)

    def define_movement(self, pos):

        angle = math.atan2(pos[1]-self.rect.y, pos[0]-self.rect.x)

        self.movement[0] = math.cos(angle)*self.velocity
        self.movement[1] = math.sin(angle)*self.velocity

        self.reach_point = pos

    def click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True
        else:
            if self.clicked and not self.shot_button_rect.collidepoint(pg.mouse.get_pos()):
                self.clicked = False
            if self.selecting_fire:
                self.selecting_fire = False

        if self.clicked:
            if self.shot_button_rect.collidepoint(pg.mouse.get_pos()):
                self.selecting_fire = True

    def right_click(self):

        if self.clicked and not self.selecting_fire:
            self.define_movement(pg.mouse.get_pos())
            self.moving = True
        if self.selecting_fire and not self.reloading:
            if self.point_reachable(pg.mouse.get_pos()):
                self.target = [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]
                self.shoot()
                self.selecting_fire = False

    def find_clicked_enemy(self):
        for i in self.all_enemies_group:
            if i.rect.collidepoint(pg.mouse.get_pos()):
                return i
        return None

    def ctrl_click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True

    def reachable(self, obj):
        dist = math.sqrt((self.rect.centerx - obj.rect.centerx) ** 2 + (self.rect.centery - obj.rect.centery) ** 2)
        if not self.moving:
            if dist < self.reach_len:
                return True
        return False

    def point_reachable(self, pos):
        dist = math.sqrt((self.rect.centerx - pos[0]) ** 2 + (self.rect.centery - pos[1]) ** 2)
        if not self.moving:
            if dist < self.reach_len:
                return True
        return False

    def shoot(self):
        self.reloading = True
        self.reload_delay = self.current_time
        self.shoot_projectile(self.target[0] + random.randint(-1, 1), self.target[1] + random.randint(-1, 1))
        self.artillery_sound.play()

    def hit(self):
        for sprite in self.all_enemies_group:
            for explosion in self.group_explosions:
                if explosion.rect.colliderect(sprite.rect):
                    if sprite not in self.hit_enemies:
                        sprite.update(80)
                        self.hit_enemies.append(sprite)

    def update(self, coordinates, enemies_group):

        self.current_time = pg.time.get_ticks()

        self.rect.center = coordinates
        self.level_rect.center = coordinates
        self.all_enemies_group = enemies_group

        if self.clicked:
            if self.moving:
                pass
            else:
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), self.reach_len, width=1)
            self.image.fill((0, 50, 255))
            self.draw_life_bar()
            self.reload_bar()
        else:
            self.image.fill((0, 255, 0))

        if self.selecting_fire and self.point_reachable(pg.mouse.get_pos()):
            pg.draw.circle(self.screen, (255, 0, 0, 10), pg.mouse.get_pos(), 50, width=5)
            self.shot_button.fill((0, 0, 255))
        else:
            self.shot_button.fill((255, 0, 0))

        if self.reach_point[0] - 10 < self.rect.x < self.reach_point[0] + 10 and \
                self.reach_point[1] - 10 < self.rect.y < self.reach_point[1] + 10:
            self.moving = False
            self.movement = [0, 0]

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.shot_button, self.shot_button_rect)
        self.screen.blit(self.level, self.level_rect)
        self.all_enemies_group.draw(self.screen)
        self.all_enemies_group.update(None)
        self.projectile_group.draw(self.screen)
        self.projectile_group.update()

        if self.target is not None:
            dist = math.sqrt((self.rect.centerx - self.target[0])**2 + (self.rect.centery - self.target[1])**2)
            for i in self.projectile_group:
                dist_bullet = math.sqrt((self.rect.x - i.rect.x)**2 + (self.rect.y - i.rect.y)**2)
                if dist < dist_bullet:
                    i.kill()
                    self.call_explosion(i.rect.centerx, i.rect.centery)
                    self.hit_once = False
                    self.hit_enemies = []
                    break

        if self.reloading:
            if self.current_time - self.reload_delay > 10000:
                self.reloading = False

        if self.moving:
            if self.clicked:
                self.draw_direction()
            self.rect.x += self.movement[0]
            self.rect.y += self.movement[1]
            return self.movement

        self.group_explosions.draw(self.screen)
        self.group_explosions.update()
        if not self.hit_once:
            self.hit()
            self.hit_once = True


class Infantry:

    def __init__(self, screen, level, width, height):

        self.screen, self.width, self.height = screen, width, height

        self.life = 300

        self.image = pg.Surface((self.width * (75 / self.width), self.height * (75 / self.height)))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.reach_len = self.width * (300/self.width)

        self.level_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.level = self.level_font.render(str(level), True, (0, 0, 0))
        self.level_rect = self.level.get_rect()

        self.clicked = False
        self.moving = False
        self.movement = [0, 0]
        self.reach_point = (self.rect.x, self.rect.y)
        self.target = None
        self.hit_once = False
        self.hit_enemies = []

        self.velocity = 1.05

        self.all_enemies_group = pg.sprite.Group()

        self.projectile_group = pg.sprite.Group()

        self.infantry_sound = pg.mixer.Sound("ressources/Sounds/infantry.mp3")
        self.infantry_sound.set_volume(0.5)

        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()

        self.last_target = None

    def shoot_projectile(self, x, y):
        for i in range(40):
            self.projectile_group.add(Pr.InfantryShooting((self.rect.centerx + randint(-25, 25),
                                                           self.rect.centery + randint(-25, 25)),
                                                          (x, y)))

    def draw_life_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                              self.image.get_width(), 5])
        pg.draw.rect(self.screen, (0, 255, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                                (self.image.get_width() / 300)*self.life, 5])

    def draw_direction(self):
        pg.draw.line(self.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), self.reach_point, width=2)

    def define_movement(self, pos):

        angle = math.atan2(pos[1]-self.rect.centery, pos[0]-self.rect.centerx)

        self.movement[0] = math.cos(angle)*self.velocity
        self.movement[1] = math.sin(angle)*self.velocity

        self.reach_point = pos

    def click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True
        else:
            if self.clicked:
                self.clicked = False

    def right_click(self):

        clicked_enemy = self.find_clicked_enemy()

        if self.clicked:
            if clicked_enemy is not None:
                if self.reachable(clicked_enemy):
                    self.target = clicked_enemy
                    self.shoot()
            else:
                self.define_movement(pg.mouse.get_pos())
                self.moving = True
                self.last_target = None

    def find_clicked_enemy(self):
        for i in self.all_enemies_group:
            if i.rect.collidepoint(pg.mouse.get_pos()):
                return i
        return None

    def ctrl_click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True

    def reachable(self, obj):
        dist = math.sqrt((self.rect.centerx-obj.rect.x)**2 + (self.rect.centery-obj.rect.y)**2)
        if not self.moving:
            if dist < self.reach_len:
                return True
        return False

    def shoot(self):
        if self.target is not None:
            self.shoot_projectile(self.target.rect.centerx, self.target.rect.centery)
        self.infantry_sound.play()

    def update(self, coordinates, enemies_group):
        self.current_time = pg.time.get_ticks()

        self.rect.center = coordinates
        self.level_rect.center = coordinates
        self.all_enemies_group = enemies_group

        if self.clicked:
            if self.moving:
                pass
            else:
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), self.reach_len, width=1)
            self.image.fill((0, 50, 255))
            self.draw_life_bar()
        else:
            self.image.fill((0, 255, 0))

        if self.reach_point[0] - 10 < self.rect.centerx < self.reach_point[0] + 10 and \
                self.reach_point[1] - 10 < self.rect.centery < self.reach_point[1] + 10:
            self.moving = False
            self.movement = [0, 0]

        self.projectile_group.draw(self.screen)
        self.projectile_group.update()
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.level, self.level_rect)
        self.all_enemies_group.draw(self.screen)
        self.all_enemies_group.update(None)

        if self.target is not None:
            for bullet in self.projectile_group:
                dist_bullet = math.sqrt((bullet.rect.x - self.rect.x)**2 + (bullet.rect.y - self.rect.y)**2)
                if dist_bullet > 1000:
                    bullet.kill()
                for enemy in self.all_enemies_group:
                    if enemy.rect.colliderect(bullet.rect):
                        enemy.update(1)
                        bullet.kill()
            self.last_target = self.target

        if self.current_time - self.delay > 750:
            self.delay = self.current_time
            if self.last_target is not None:
                self.shoot()
                for bullet in self.projectile_group:
                    dist_bullet = math.sqrt((bullet.rect.x - self.rect.x)**2 + (bullet.rect.y - self.rect.y)**2)
                    if dist_bullet > 1000:
                        bullet.kill()
                    for enemy in self.all_enemies_group:
                        if enemy.rect.colliderect(bullet.rect):
                            enemy.update(0.25)
                            bullet.kill()

        # check if the target died
        if self.target not in self.all_enemies_group:
            self.target = None
            self.last_target = None

        if self.moving:
            self.target = None
            self.last_target = None
            if self.clicked:
                self.draw_direction()
            self.rect.centerx += self.movement[0]
            self.rect.centery += self.movement[1]
            return self.movement


class Cavalry:

    def __init__(self, screen, level, width, height):
        self.screen = screen

        self.width, self.height = width, height

        self.life = 700

        self.reach_len = self.width * (500/self.width)

        self.image = pg.Surface((self.width * (50/self.width), self.height * (50 / self.height)))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.level_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.level = self.level_font.render(str(level), True, (0, 0, 0))
        self.level_rect = self.level.get_rect()

        self.clicked = False
        self.moving = False
        self.movement = [0, 0]
        self.reach_point = (self.rect.x, self.rect.y)
        self.target = None
        self.hit_once = False
        self.reloading = False

        self.shot_button = pg.Surface((100, 100))
        self.shot_button.fill((255, 0, 0))
        self.shot_button_rect = self.shot_button.get_rect(left=0, y=self.height-self.shot_button.get_height())

        self.velocity = 1.75

        self.all_enemies_group = pg.sprite.Group()

        self.projectile_group = pg.sprite.Group()
        self.shoot_projectile = lambda x, y: self.projectile_group.add(Pr.CavalryShot(
            (self.rect.centerx, self.rect.centery), (x, y)))

        self.artillery_sound = pg.mixer.Sound("ressources/Sounds/tank.mp3")
        self.artillery_sound.set_volume(0.25)

        self.selecting_fire = False

        self.group_explosions = pg.sprite.Group()
        self.call_explosion = lambda x, y: self.group_explosions.add(Ga.Explosion2((x, y)))

        self.hit_enemies = []

        self.current_time = pg.time.get_ticks()
        self.reload_delay = pg.time.get_ticks()

        self.rdy_font = pg.font.Font("ressources/Fonts/f014015d.woff", 10)
        self.rdy = self.rdy_font.render("ready !", True, (0, 0, 0))
        self.rdy_rect = self.rdy.get_rect()

    def reload_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                              self.image.get_width(), 5])
        if self.reloading:
            delay = self.current_time - self.reload_delay
            pg.draw.rect(self.screen, (0, 200, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                                    (50 / 2500)*delay, 5])
        else:
            pg.draw.rect(self.screen, (0, 200, 0), [self.rect.x, self.rect.y + self.image.get_height() + 10,
                                                    self.image.get_width(), 5])
            self.rdy_rect.center = self.rect.x + 25, self.rect.y + 62
            self.screen.blit(self.rdy, self.rdy_rect)

    def draw_life_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                              self.image.get_width(), 5])
        pg.draw.rect(self.screen, (0, 255, 0), [self.rect.x, self.rect.y + self.image.get_height() + 5,
                                                (self.image.get_width()/700)*self.life, 5])

    def draw_direction(self):
        if self.moving:
            pg.draw.line(self.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), self.reach_point, width=2)

    def define_movement(self, pos):

        angle = math.atan2(pos[1]-self.rect.y, pos[0]-self.rect.x)

        self.movement[0] = math.cos(angle)*self.velocity
        self.movement[1] = math.sin(angle)*self.velocity

        print(self.movement)

        self.reach_point = pos

    def click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True
        else:
            if self.clicked and not self.shot_button_rect.collidepoint(pg.mouse.get_pos()):
                self.clicked = False
            if self.selecting_fire:
                self.selecting_fire = False

        if self.clicked:
            if self.shot_button_rect.collidepoint(pg.mouse.get_pos()):
                self.selecting_fire = True

    def right_click(self):

        if self.clicked and not self.selecting_fire:
            self.define_movement(pg.mouse.get_pos())
            self.moving = True
        if self.selecting_fire and not self.reloading:
            if self.point_reachable(pg.mouse.get_pos()):
                self.target = [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]
                self.shoot()
                self.selecting_fire = False

    def find_clicked_enemy(self):
        for i in self.all_enemies_group:
            if i.rect.collidepoint(pg.mouse.get_pos()):
                return i
        return None

    def ctrl_click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.clicked = True

    def reachable(self, obj):
        dist = math.sqrt((self.rect.centerx - obj.rect.centerx) ** 2 + (self.rect.centery - obj.rect.centery) ** 2)
        if dist < self.reach_len:
            return True
        return False

    def point_reachable(self, pos):
        dist = math.sqrt((self.rect.centerx - pos[0]) ** 2 + (self.rect.centery - pos[1]) ** 2)
        if dist < self.reach_len:
            return True
        return False

    def shoot(self):
        self.reloading = True
        self.reload_delay = self.current_time
        self.shoot_projectile(self.target[0] + random.randint(-1, 1), self.target[1] + random.randint(-1, 1))
        self.artillery_sound.play()

    def hit(self):
        for sprite in self.all_enemies_group:
            for explosion in self.group_explosions:
                if explosion.rect.colliderect(sprite.rect):
                    if sprite not in self.hit_enemies:
                        sprite.update(50)
                        self.hit_enemies.append(sprite)

    def update(self, coordinates, enemies_group):

        self.current_time = pg.time.get_ticks()

        self.rect.center = coordinates
        self.level_rect.center = coordinates
        self.all_enemies_group = enemies_group

        if self.clicked:
            pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), self.reach_len, width=1)
            self.image.fill((0, 50, 255))
            self.draw_life_bar()
            self.reload_bar()
        else:
            self.image.fill((0, 255, 0))

        if self.selecting_fire and self.point_reachable(pg.mouse.get_pos()):
            pg.draw.circle(self.screen, (255, 0, 0, 10), pg.mouse.get_pos(), 50, width=5)
            self.shot_button.fill((0, 0, 255))
        else:
            self.shot_button.fill((255, 0, 0))

        if self.reach_point[0] - 10 < self.rect.x < self.reach_point[0] + 10 and \
                self.reach_point[1] - 10 < self.rect.y < self.reach_point[1] + 10:
            self.moving = False
            self.movement = [0, 0]

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.shot_button, self.shot_button_rect)
        self.screen.blit(self.level, self.level_rect)
        self.all_enemies_group.draw(self.screen)
        self.all_enemies_group.update(None)
        self.projectile_group.draw(self.screen)
        self.projectile_group.update()

        if self.target is not None:
            dist = math.sqrt((self.rect.centerx - self.target[0])**2 + (self.rect.centery - self.target[1])**2)
            for i in self.projectile_group:
                dist_bullet = math.sqrt((self.rect.x - i.rect.x)**2 + (self.rect.y - i.rect.y)**2)
                if dist < dist_bullet:
                    i.kill()
                    self.call_explosion(i.rect.centerx, i.rect.centery)
                    self.hit_once = False
                    self.hit_enemies = []
                    break

        if self.reloading:
            if self.current_time - self.reload_delay > 2500:
                self.reloading = False

        self.group_explosions.draw(self.screen)
        self.group_explosions.update()
        if not self.hit_once:
            self.hit()
            self.hit_once = True

        if self.clicked:
            self.draw_direction()
        self.rect.x += self.movement[0]
        self.rect.y += self.movement[1]
        return self.movement
