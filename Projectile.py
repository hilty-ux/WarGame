import pygame as pg
import math
from random import randint


class SniperBullet(pg.sprite.Sprite):

    def __init__(self, pos, target_pos):
        super().__init__()

        self.image = pg.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.velocity = 25

        angle = math.atan2(target_pos[1]-pos[1], target_pos[0]-pos[0])

        self.dx = math.cos(angle)*self.velocity
        self.dy = math.sin(angle)*self.velocity

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x > 1920 or self.rect.x < 0 or self.rect.y < 0 or self.rect.y > 1080:
            self.kill()


class ArtilleryShot(pg.sprite.Sprite):

    def __init__(self, pos, target_pos):
        super().__init__()

        self.image = pg.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.begin_pos = pos

        self.velocity = 10

        angle = math.atan2(target_pos[1]-pos[1], target_pos[0]-pos[0])

        self.dx = math.cos(angle)*self.velocity
        self.dy = math.sin(angle)*self.velocity

        self.target_pos = target_pos

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        dist = math.sqrt((self.begin_pos[0] - self.target_pos[0])**2 + (self.begin_pos[1] - self.target_pos[1])**2)
        if dist > 900:
            self.kill()


class InfantryShooting(pg.sprite.Sprite):

    def __init__(self, pos, target_pos):
        super().__init__()

        self.image = pg.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.begin_pos = pos

        self.velocity = 25

        angle = math.atan2(target_pos[1] + randint(-50, 50) - pos[1], target_pos[0] + randint(-50, 50) - pos[0])

        self.dx = math.cos(angle) * self.velocity
        self.dy = math.sin(angle) * self.velocity

        self.target_pos = target_pos

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        dist = math.sqrt((self.begin_pos[0] - self.target_pos[0]) ** 2 + (self.begin_pos[1] - self.target_pos[1])**2)
        if dist > 900:
            self.kill()


class CavalryShot(pg.sprite.Sprite):

    def __init__(self, pos, target_pos):
        super().__init__()

        self.image = pg.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.begin_pos = pos

        self.velocity = 50

        angle = math.atan2(target_pos[1] - pos[1], target_pos[0] - pos[0])

        self.dx = math.cos(angle)*self.velocity
        self.dy = math.sin(angle)*self.velocity

        self.target_pos = target_pos

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        dist = math.sqrt((self.begin_pos[0] - self.target_pos[0])**2 + (self.begin_pos[1] - self.target_pos[1])**2)
        if dist > 900:
            self.kill()
