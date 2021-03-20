import pygame as pg


class SniperEnemy(pg.sprite.Sprite):

    def __init__(self, screen, level, coordinates):
        super().__init__()

        self.screen = screen

        self.life = 100

        self.image = pg.Surface((25, 25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

        self.level_font = pg.font.Font("ressources/Fonts/f014015d.woff", 15)
        self.level = self.level_font.render(str(level), True, (0, 0, 0))
        self.level_rect = self.level.get_rect()
        self.level_rect.center = coordinates

        self.moving = False
        self.movement = [0, 0]
        self.reach_point = (self.rect.x, self.rect.y)

        self.velocity = 0.2

    def draw_life_bar(self):
        pg.draw.rect(self.screen, (0, 0, 0), [self.rect.x, self.rect.y + 30,
                                              25, 5])
        pg.draw.rect(self.screen, (255, 0, 0), [self.rect.x, self.rect.y + 30,
                                                (25/100)*self.life, 5])

    def update(self, life):

        self.draw_life_bar()

        if life is not None:
            self.life -= life
            return

        if self.life <= 0:
            self.kill()

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.level, self.level_rect)
