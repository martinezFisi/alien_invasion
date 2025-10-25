
import pygame

class Bullet:

    count = 0

    def __init__(self, game, isSpecial=False):
        special_bullet_rect = pygame.Rect(((game.ship.rect.x - game.special_bullet_width/3, game.ship.rect.y)), (250, 5))

        Bullet.count += 1
        self.id = Bullet.count
        self.game = game
        self.rect = special_bullet_rect if isSpecial else pygame.Rect(game.ship.rect.midtop, (5, 10))
        self.velocity = game.bullet_velocity
        self.color = game.bullet_color
        self.isSpecial = isSpecial

    def blitme(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)

    def update(self):
        self.rect.y -= self.velocity
        
        if self.rect.y < 0:
            self.game.bullets.remove(self)

    def __eq__(self, other):
        if isinstance(other, Bullet):
            return self.id == other.id
        return False 