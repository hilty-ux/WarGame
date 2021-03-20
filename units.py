import pygame as pg
import math
import random
import Projectile as Pr
import Game_Animations as Ga


class Sniper:

    def __init__(self, screen, level):

        self.screen = screen

        self.image = pg.Surface((25, 25))
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

    def draw_direction(self):
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
        dist = math.sqrt((self.rect.x-obj.rect.x)**2 + (self.rect.y-obj.rect.y)**2)
        if not self.moving:
            if dist < 300:
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
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), 150, width=1)
            else:
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), 300, width=1)
            self.image.fill((0, 50, 255))
        else:
            self.image.fill((0, 255, 0))

        if self.reach_point[0] - 10 < self.rect.x < self.reach_point[0] + 10 and \
                self.reach_point[1] - 10 < self.rect.y < self.reach_point[1] + 10:
            self.moving = False
            self.movement = [0, 0]

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.level, self.level_rect)
        self.all_enemies_group.draw(self.screen)
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

        self.shot_button = pg.Surface((100, 100))
        self.shot_button.fill((255, 0, 0))
        self.shot_button_rect = self.shot_button.get_rect()
        self.shot_button_rect.left = 0
        self.shot_button_rect.y = self.height - 100

        self.velocity = 0.45

        self.all_enemies_group = pg.sprite.Group()

        self.projectile_group = pg.sprite.Group()
        self.shoot_projectile = lambda x, y: self.projectile_group.add(Pr.ArtilleryShot(
            (self.rect.centerx, self.rect.centery), (x, y)))

        self.artillery_sound = pg.mixer.Sound("ressources/Sounds/artillery.wav")
        self.artillery_sound.set_volume(0.15)

        self.selecting_fire = True

        self.group_explosions = pg.sprite.Group()
        self.call_explosion = lambda x, y: self.group_explosions.add(Ga.SimpleExplosion((x, y)))

    def draw_direction(self):
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
        if self.selecting_fire:
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
        dist = math.sqrt((self.rect.x-obj.rect.centerx)**2 + (self.rect.y-obj.rect.centery)**2)
        if not self.moving:
            if dist < 800:
                return True
        return False

    def point_reachable(self, pos):
        dist = math.sqrt((self.rect.x - pos[0]) ** 2 + (self.rect.y - pos[1]) ** 2)
        if not self.moving:
            if dist < 800:
                return True
        return False

    def shoot(self):
        self.shoot_projectile(self.target[0] + random.randint(-1, 1), self.target[1] + random.randint(-1, 1))
        self.artillery_sound.play()

    def hit(self):
        for sprite in self.all_enemies_group:
            for explosion in self.group_explosions:
                if explosion.rect.colliderect(sprite.rect):
                    sprite.update(80)
                    return True

    def update(self, coordinates, enemies_group):
        self.rect.center = coordinates
        self.level_rect.center = coordinates
        self.all_enemies_group = enemies_group

        if self.clicked:
            if self.moving:
                pass
            else:
                pg.draw.circle(self.screen, (50, 50, 255), (self.rect.centerx, self.rect.centery), 800, width=1)
            self.image.fill((0, 50, 255))
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
                    break

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
