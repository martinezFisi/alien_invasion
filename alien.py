
import pygame

class Alien:

    def __init__(self, game, order):
        self.game = game
        self.game_screen = game.screen
        self.game_screen_rect = game.screen.get_rect()
        self.init_pos = game.alien_init_pos
        self.horizontal_distance = game.horizontal_distance_beetwen_aliens
        self.order = order

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.topleft = self.init_pos
        self.rect.x = self.rect.x + self.horizontal_distance*self.order

    def blitme(self):
        self.game_screen.blit(self.image, self.rect)
