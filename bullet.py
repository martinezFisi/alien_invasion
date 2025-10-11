
import pygame

class Bullet:

    count = 0

    def __init__(self, game):
        Bullet.count += 1
        self.id = Bullet.count
        self.game = game
        self.rect = pygame.Rect(game.ship.rect.midtop, (5, 10))
        self.velocity = game.bullet_velocity
        self.color = game.bullet_color

    def blitme(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)

    def update(self):
        self.rect.y -= self.velocity
        
        if self.rect.y < 0:
            self.game.bullets.remove(self)
            print(f'Nuevo numero de bullets: {len(self.game.bullets)}')

    def __eq__(self, other):
        if isinstance(other, Bullet):
            return self.id == other.id
        return False 