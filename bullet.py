
import pygame

class Bullet:

    def __init__(self, game):
        self.game = game
        self.rect = pygame.Rect(game.ship.rect.midtop, (5, 10))

    def blitme(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.rect)

    def update(self):
        self.rect.y -= 5