
import pygame

class Ship:
    
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.game_screen_rect = game_screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.game_screen_rect.midbottom

    def blitme(self):
        self.game_screen.blit(self.image, self.rect)
